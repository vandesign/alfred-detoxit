import json

MainBaseRu = {}
MainBaseEn = {}
AlfredSetup = {}
MainSetup = {'items': [AlfredSetup]}

with open('RULES.ru.md', encoding="utf8") as FullPageRu:
    AllLinesRu = FullPageRu.readlines()
    Counter = 0
    for OneLine in AllLinesRu[4:]:
        OneRow = OneLine.split(' | ')
        DeleteLink = OneRow[1].split('(..')
        OneRow[1] = DeleteLink[0]
        OneRow[1] = OneRow[1].replace('[', '').replace(']', '')
        OneRow[5] = OneRow[5].replace('✓ |\n', 'True')
        OneRow[5] = OneRow[5].replace(' |\n', '')
        OneRow[5] = bool(OneRow[5])
        Unit = {'description': '', 'isEnabled': ''}
        Unit['description'] = OneRow[2]
        Unit['isEnabled'] = OneRow[5]
        Counter += 1
        MainBaseRu[OneRow[1]] = Unit
        if OneRow[5] is True:
            AlfredSetup = {'uid': OneRow[1], 'title': OneRow[2],
                           'subtitle': 'Выключить',
                           'arg': OneRow[1], 'autocomplete': OneRow[2],
                           'icon': {'path': 'detoxit-on.png'}}
        else:
            AlfredSetup = {'uid': OneRow[1], 'title': OneRow[2],
                           'subtitle': 'Включить',
                           'arg': OneRow[1], 'autocomplete': OneRow[2],
                           'icon': {'path': 'detoxit-off.png'}}
        MainSetup['items'].append(AlfredSetup)

with open('typograf-setup.json', 'w') as OutJson:
    json.dump(MainBaseRu, OutJson, sort_keys=False,
              indent=4, ensure_ascii=False)

with open('detoxit-setup.json', 'w') as OutJson:
    json.dump(MainSetup, OutJson, sort_keys=False,
              indent=4, ensure_ascii=False)
