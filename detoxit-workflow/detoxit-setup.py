# -*- coding: utf-8 -*-

from io import open
import json

ruleSetup = {}
alfredSetup = {'items': [ruleSetup]}

with open('detoxit-setup.json', encoding='utf-8') as readRules:
    rawRules = json.load(readRules)
    for i in rawRules[1:]:
        if i['isEnabled'] is True:
            ruleSetup = {'uid': i['id'],
                         'title': i['name'],
                         'subtitle': 'Выключить',
                         'arg': i['id'],
                         'autocomplete': i['name'],
                         'icon': {'path': 'detoxit-on.png'}}
        else:
            ruleSetup = {'uid': i['id'],
                         'title': i['name'],
                         'subtitle': 'Включить',
                         'arg': i['id'],
                         'autocomplete': i['name'],
                         'icon': {'path': 'detoxit-off.png'}}
        alfredSetup['items'].append(ruleSetup)

alfredSetupOut = json.dumps(alfredSetup, sort_keys=False, indent=4, ensure_ascii=True, encoding='utf-8')

print(alfredSetupOut)
