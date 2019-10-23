from io import open
import json
import sys

changeRule = '{query}'
sys.stdout.write(changeRule)
with open('detoxit-setup.json', encoding='utf-8') as readRules:
    rawRules = json.load(readRules)
    for i in rawRules[0:]:
        if i['id'] == changeRule:
            i['isEnabled'] = not i['isEnabled']

with open('detoxit-setup.json', 'wb') as OutJson:
    json.dump(rawRules, OutJson, sort_keys=False, indent=4, ensure_ascii=True, encoding='utf-8')
