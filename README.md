<img align="right" width="128" src="./img/icon.png">

# Detoxit!
Workflow для [Alfred](https://www.alfredapp.com) c [Powerpack](https://buy.alfredapp.com/) на базе [Типографа на JavaScript](https://github.com/typograf/typograf)

## Привет!
Detoxit! помогает одним движением избавить текст от большинства «болячек» — неправильных кавычек, дефисов вместо тире, двойных пробелов и множественных переводов строки (всего [около 100 правил](https://github.com/typograf/typograf/blob/dev/docs/RULES.ru.md)).
<br />
<br />

![text-detox](./img/text-detox.png)
<br />
<br />

## Установка
- **[Скачать Detoxit!](https://github.com/vandesign/alfred-detoxit/releases/download/v0.0.5/Detoxit.alfredworkflow)**

- Импортировать двойным кликом Detoxit.alfredworkflow в Alfred.

- Настроить горячие клавиши. Хоткей по умолчанию (`Command + Shift + =`).
<br />
<br />

![hotkey](./img/hotkey.png)
<br />
<br />

- Detoxit! обрабатывает текст в буфере обмена. Копируем грязный текст (`Command + C`), нажимаем хоткей (`Command + Shift + =`), вставляем чистый текст (`Command + V`).

- Можно включать/выключать отдельные правила обработки текста. Начните набирать в Alfred `detoxitsetup`, нажмите `Return`.

![detoxit-workflow](./img/detoxit-workflow.png)

- Выберите правило и включите или выключите его.

![detoxit-setup](./img/detoxit-setup.png)

## Родители
Detoxit! работает на базе [Типограф на JavaScript](https://github.com/typograf/typograf).

Облачные функции — [typograf-now](https://github.com/tplk/typograf-now).

## Ближайшие планы
- Выбор локали.
- Дополнительная настройка отдельных правил.
- Обработка текста одним правилом.
- Предустановки для web-разработки.
- Сброс правил.
- Локальная Nodejs версия.
- **Принимаются предложения!**

## Лицензия
[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](./LICENSE)
