from pathlib import Path
import sys, re, json, html, shutil

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / '.build-deps'))
import markdown

PAGES = [
 ('README.md','index.html','开始学习','课程总览'),
 ('01-schedule.md','schedule.html','30 天日程','每天的学习目标'),
 ('02-foundations.md','foundations.html','Linux 与 Python','M1–M2 · 开发基础'),
 ('03-learning-vision.md','learning-vision.html','机器学习与视觉','M3–M5 · 实验基础'),
 ('04-robotics.md','robotics.html','ROS 2 与具身智能','M6–M8 · 系统实践'),
 ('05-resources.md','resources.html','学习资料','教材、文档与视频'),
 ('06-assessment.md','assessment.html','作业与验收','8 次阶段检查'),
 ('07-mentor.md','mentor.html','导师手册','分层与教学执行'),
 ('08-templates.md','templates.html','提交模板','日志、报告与交接'),
]
out = ROOT / 'dist'
out.mkdir(exist_ok=True)
for asset in ['style.css','app.js']:
 shutil.copyfile(ROOT / asset, out / asset)
search = []
for i,(source,target,title,subtitle) in enumerate(PAGES):
 text = (ROOT / 'content' / source).read_text(encoding='utf-8')
 if source == 'README.md':
  text = re.sub(r'这里将口述中的.*?\n\n','',text,flags=re.S)
  text = text[:text.index('## 使用与维护')] + '''## 使用与更新

通过左侧目录按阶段学习，或打开“30 天日程”查看当天目标。搜索支持关键词查找全部课程页面。页面顶部可标记阅读完成，进度仅保存在当前浏览器，不上传给导师；正式成绩以作业验收为准。

课程资料最近核对日期为 2026-10-26。部分 ROS 官方页面与 B 站播放器有自动访问限制，资料导航中已注明核验方式。安装命令属于教学配方，开课前由导师在本届设备上统一预演。
'''
 for md, dest, _, _ in PAGES:
  text = text.replace(']('+md+')',']('+dest+')')
 text = re.sub(r'^# .+\n', '', text, count=1)
 parser = markdown.Markdown(extensions=['tables','fenced_code','toc','sane_lists'],extension_configs={'toc':{'permalink':False}})
 body = parser.convert(text)
 body = re.sub(r'<h1.*?</h1>','',body,count=1,flags=re.S)
 body = re.sub(r'(<table>.*?</table>)',r'<div class="table-scroll" tabindex="0">\1</div>',body,flags=re.S)
 nav_parts = []
 for n,(_,dest,label,desc) in enumerate(PAGES):
  active = 'active' if n == i else ''
  current = 'aria-current="page"' if n == i else ''
  nav_parts.append(f'<a class="nav-link {active}" href="{dest}" {current}><span class="nav-num">{n+1:02}</span><span>{label}<small>{desc}</small></span><span class="read-dot" data-page="{dest}"></span></a>')
 nav = ''.join(nav_parts)
 hero = '''<section class="hero"><div class="eyebrow">EMBODIED AI / FOUNDATIONS</div><h1>从第一行命令，<br>到第一个机器人闭环。</h1><p>为大四本科生准备的任务驱动学习路径。每天一点实践，<br class="wide">把知识变成可以运行、解释和复现的成果。</p><div class="hero-actions"><a class="primary" href="schedule.html">查看 30 天学习日程 <span>↗</span></a><a class="secondary" href="assessment.html">了解验收方式 →</a></div><div class="stats"><div><strong>30<small>天</small></strong><span>循序渐进的学习周期</span></div><div><strong>95<small>小时</small></strong><span>含实践、验收与缓冲</span></div><div><strong>8<small>次</small></strong><span>可检查的阶段成果</span></div></div><div class="orbit" aria-hidden="true"><span>感知</span><span>学习</span><span>行动</span><b>↻</b></div></section>''' if i==0 else f'<header class="page-heading"><div class="eyebrow">FOUNDATIONS WIKI / {i+1:02}</div><h1>{title}</h1><p>{subtitle} · 目标驱动，动手验证</p></header>'
 prev = f'<a href="{PAGES[i-1][1]}">← {PAGES[i-1][2]}</a>' if i else '<span></span>'
 nxt = f'<a href="{PAGES[i+1][1]}">{PAGES[i+1][2]} →</a>' if i<len(PAGES)-1 else '<a href="index.html">回到课程总览 ↑</a>'
 page = f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="30 天具身智能基础训练 Wiki：Linux、Python、PyTorch、视觉、ROS 2 与任务验收。"><meta name="theme-color" content="#123c35"><title>{title} · 具身智能基础训练营</title><link rel="stylesheet" href="style.css"><script defer src="app.js"></script></head>
<body data-page="{target}"><a class="skip" href="#article">跳到正文</a><aside id="sidebar"><a class="brand" href="index.html"><span class="brand-mark">E<span>↗</span></span><span>具身智能<small>基础训练营 / WIKI</small></span></a><div class="sidebar-label">LEARNING PATH · 学习路径</div><nav aria-label="课程目录">{nav}</nav><div class="progress-box"><div>我的阅读进度 <b id="progress-text">0 / 9</b></div><progress id="progress" max="9" value="0"></progress><small>仅保存在本机 · 非验收成绩</small><button id="reset-progress">重置阅读进度</button></div><a class="sidebar-foot" href="mentor.html">面向大四本科生 · 导师指南 ↗</a></aside><div class="scrim" id="scrim"></div><div class="workspace"><header class="topbar"><button id="menu-toggle" aria-label="展开目录" aria-expanded="false">☰</button><span class="crumb">学习中心 <span>/</span> {title}</span><button id="search-open"><span>⌕</span> 搜索课程内容 <kbd>/</kbd></button></header><main><div class="main-column">{hero}<div class="reading-tools"><span>核心路线 · 普通笔记本可完成</span><button id="mark-read" aria-pressed="false">○ 标记本页已读</button></div><article id="article">{body}</article><div class="page-nav">{prev}{nxt}</div><footer>具身智能基础训练营 · 以实践建立理解<br><small>资料核对：2026-10-26 · 阅读进度不作为作业验收记录</small></footer></div><aside class="page-toc"><div>本页导航</div>{parser.toc}</aside></main></div><dialog id="search-dialog"><div class="search-head"><label for="search-input">搜索全部课程</label><button id="search-close" aria-label="关闭搜索">✕</button></div><input id="search-input" type="search" placeholder="例如：WSL、过拟合、A6、提交模板" autocomplete="off"><p id="search-status" aria-live="polite">输入关键词，查找课程中的内容。</p><div id="search-results"></div></dialog></body></html>'''
 (out / target).write_text(page,encoding='utf-8')
 plain = html.unescape(re.sub('<[^>]+>',' ',body))
 search.append({'title':title,'url':target,'text':re.sub(r'\s+',' ',plain)})
(out / 'search-index.json').write_text(json.dumps(search,ensure_ascii=False),encoding='utf-8')
(out / '.nojekyll').touch()
print(f'Built {len(PAGES)} pages in {out}')
