# 具身智能 · 30 天基础训练营

面向大四本科生的学习 Wiki：Linux、Python、机器学习、视觉、ROS 2、GNN 与具身智能。包含逐日日程、学习资料、8 次作业验收、导师手册和学生模板。

## 首次发布到 shishunzhang1995 的 GitHub Pages

1. 登录 GitHub，新建公开仓库 `embodied-ai-bootcamp`，默认分支为 `main`。
2. 解压交付 ZIP，将**本目录内部全部文件和目录**上传到仓库根目录。不要上传 ZIP 文件本身，也不要多包一层 `embodied-ai-github/`。务必包含 `.github/workflows/pages.yml`；Windows 资源管理器中它可能不显眼。
3. 在仓库 **Settings → Pages → Build and deployment → Source** 选择 **GitHub Actions**。
4. 打开 **Actions → Publish course wiki → Run workflow**，选择 `main`。首次上传可能在启用 Pages 之前触发运行而失败，配置后重新运行即可。
5. 等待 build 和 deploy 均成功。使用 **Settings → Pages** 显示的网址确认部署，而不是仅凭地址格式判断已上线。

如果仓库名称按上述设置，预期地址为：

https://shishunzhang1995.github.io/embodied-ai-bootcamp/

该地址在完成部署前不代表可访问。GitHub Pages 是境外托管，学生网络下的可达性需要实际测试。

## 后续更新

编辑 `content/` 中的 Markdown 并提交到 `main`，工作流会自动构建、校验并部署。不需要手动修改 `dist/` 的 HTML。样式在 `style.css`，搜索／阅读标记等交互在 `app.js`。

## 本地构建

```bash
python -m pip install -r requirements.txt
python build.py
python check.py
python -m http.server 8765 --directory dist
```

浏览器访问 http://localhost:8765 。网页使用相对链接，可以部署在仓库子路径下。阅读进度仅保存在当前浏览器中。

本交付不含其他托管平台的项目标识、认证信息或 Git 历史。原有在线 Wiki 不受影响。
