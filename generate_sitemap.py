from pathlib import Path
from xml.sax.saxutils import escape
import sys
base=sys.argv[1].rstrip('/') if len(sys.argv)>1 else ''
if not base.startswith('https://'): raise SystemExit('사용법: python generate_sitemap.py https://내도메인')
p=Path(__file__).parent
urls=[f'{base}/{f.relative_to(p).as_posix()}' for f in p.rglob('*.html')]
xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('  <url><loc>'+escape(u)+'</loc></url>\n' for u in urls)+'</urlset>\n'
(p/'sitemap.xml').write_text(xml,encoding='utf-8')
(p/'robots.txt').write_text('User-agent: *\nAllow: /\nSitemap: '+base+'/sitemap.xml\n',encoding='utf-8')
print(len(urls),'개 URL 생성 완료')
