Разработать ассемблер и интерпретатор для учебной виртуальной машины (УВМ). Система команд УВМ представлена далее. Для ассемблера необходимо разработать читаемое представление команд УВМ. Ассемблер принимает на вход файл с текстом исходной программы, путь к которой задается из командной строки. Результатом работы ассемблера является бинарный файл в виде последовательности байт, путь к которому задается из командной строки. Дополнительный ключ командной строки задает путь к файлулогу, в котором хранятся ассемблированные инструкции в духе списков “ключ=значение”, как в приведенных далее тестах.

Интерпретатор принимает на вход бинарный файл, выполняет команды УВМ и сохраняет в файле-результате значения из диапазона памяти УВМ. Диапазон также указывается из командной строки. Форматом для файла-лога и файла-результата является **xml**. Необходимо реализовать приведенные тесты для всех команд, а также написать и отладить тестовую программу.

Загрузка константы:

A        | B
Биты 0-4 | Биты 5-18
7        | Константа

Размер команды: 5 байт. Операнд: поле B. Результат: регистр-аккумулятор.

Тест (A=7, B=927): 
0xE7, 0x73, 0x00, 0x00, 0x00 


Чтение значения из памяти

A        | B
Биты 0-4 | Биты 5-30
5        | Адрес

Размер команды: 5 байт. Операнд: значение в памяти по адресу, которым является поле B. Результат: регистр-аккумулятор. 

Тест (A=5, B=475): 
0x65, 0x3B, 0x00, 0x00, 0x00


Запись значения в память

A        | B
Биты 0-4 | Биты 5-30
27       | Адрес

Размер команды: 5 байт. Операнд: регистр-аккумулятор. Результат: значение в памяти по адресу, которым является поле B.

Тест (A=27, B=1003): 
0x7B, 0x7D, 0x00, 0x00, 0x00

 
Бинарная операция: "==" 

| A         | B            |
|-----------|--------------|
| Биты 0-4 | Биты 5-30    |
| 19        | Адрес        |


Размер команды: 5 байт. Первый операнд: регистр-аккумулятор. Второй операнд: значение в памяти по адресу, которым является поле B. Результат: регистр-аккумулятор. 

Тест (A=19, B=361): 
0x33, 0x2D, 0x00, 0x00, 0x00
 
Тестовая программа 
Выполнить поэлементно операцию "==" над вектором длины 6 и числом 107. 
Результат записать в новый вектор.
