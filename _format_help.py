import json
import urllib2

data = {'text': open('README.md').read(), 'mode': 'markdown'}
markdown_html = urllib2.urlopen('https://api.github.com/markdown', json.dumps(data)).read()

TEMPLATE = """
<html>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
<head>
<title>MooKoo</title>
<style>
%(style)s
</style>
</head>
<body>
%(markdown)s
</body>
</html>
"""

html = TEMPLATE % {
    'style': open('markdown.css').read(),
    'markdown': markdown_html,
}
open('help.html', 'w').write(html)
