from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json

root = Path(__file__).resolve().parent / 'dist'
class Links(HTMLParser):
 def __init__(self):
  super().__init__(); self.links=[]; self.ids=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a:self.ids.append(a['id'])
  for key in ['href','src']:
   if key in a:self.links.append(a[key])
pages = list(root.glob('*.html'))
assert len(pages)==9
parsed={}
for p in pages:
 obj=Links(); obj.feed(p.read_text(encoding='utf-8')); parsed[p.name]=obj
 assert len(obj.ids)==len(set(obj.ids)), f'Duplicate ids: {p}'
for name,obj in parsed.items():
 for link in obj.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  dest=unquote(u.path) or name
  assert (root/dest).is_file(),f'Broken link: {name} -> {link}'
  if u.fragment and dest in parsed:
   assert unquote(u.fragment) in parsed[dest].ids, f'Broken anchor: {name} -> {link}'
index=json.loads((root/'search-index.json').read_text(encoding='utf-8'))
assert len(index)==9
for q in ['WSL','过拟合','A6','提交模板']:
 assert any(q.lower() in (p['title']+p['text']).lower() for p in index),q
assert not any('H:/000AAAI' in p.read_text(encoding='utf-8') for p in pages)
print('PASS: 9 pages; local links and anchors; search terms; no local workspace paths.')
