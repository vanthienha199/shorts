"""Fill template.html with videos.json and write index.html."""
import json
V = [{k: v for k, v in d.items() if k not in ('ar', 'mb')} for d in json.load(open('videos.json'))]
t = open('template.html').read()
assert '/*DATA*/' in t
open('index.html', 'w').write(t.replace('/*DATA*/', json.dumps(V, ensure_ascii=False)))
print('index.html with', len(V), 'videos')
