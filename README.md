# Ближайшие бары

На сайте data.mos.ru есть много разных данных, в том числе список московских баров. Его можно скачать в формате JSON. Для этого нужно:
* зарегистрироваться на сайте и получить ключ API;
* скачать файл по ссылке вида https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}.

Либо скачать [тут](https://devman.org/fshare/1503831681/4/)

Далее, положив файл в директорию со скриптом, мы можем выполнить поиск баров по параметрам:
* самый большой бар
* самый маленький бар
* ближайший бар

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py # possibly requires call of python3 executive instead of just python
The biggest bar is  Спорт бар «Красная машина»
The smallest bar is  БАР. СОКИ
Insert longitude: 4
Insert latitude: a
Please insert correct latitude: 1
The closest bar is  Staropramen

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
