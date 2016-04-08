import json
import urllib2

data = {'text': open('README.md').read(), 'mode': 'markdown'}
html = urllib2.urlopen('https://api.github.com/markdown', json.dumps(data)).read()
open('help.html', 'w').write(html)
