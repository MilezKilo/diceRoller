from random import randrange
# Create by Maxim Ponizov and Alexandr Volodkin, group BVT 2152


#  Функция броска кубиков без доп числа
def throwWithoutAdditionalNumber(innerDice):
    innerValue = innerDice.split('d')
    inputedDices, inputedEdges = innerValue[0], innerValue[1]

    x, y = [], 0  # х - список выпавших граней, у - итоговое число

    for i in range(1, int(inputedDices) + 1):  # Добавляем случайные значения в х
        x.append(randrange(1, int(inputedEdges)))
    for i in x:  # Складываем в у выпавшие случайные значения
        y += i

    printedList = str(x).replace('[', '(').replace(']', ')')  # Преобразовываем х из [число, число] в "(число, число)", при этом лист станет строкой
    print(y, printedList)  # Вывод в консоль результата


#  Функция броска кубиков с доп числом
def throwWithAdditionalNumber(innerDice):
    innerValue = innerDice.split('d')
    inputedDices, inputedEdges = innerValue[0], innerValue[1]
    dividedEdgesAndAdditionalNumber = 0
    x, y, lastDigit = [], 0, ''
    dice = int(inputedDices)

    if '+' in innerDice:
        dividedEdgesAndAdditionalNumber = inputedEdges.split(
            "+")  # Разделяем количество граней и дополнительное положительное число
        additionalNumber = int(dividedEdgesAndAdditionalNumber[-1])  # Дополнительное число
        y += additionalNumber  # Прибавляем дополнительное число к у
        lastDigit = '+' + str(additionalNumber)  # Преобразовываем доп число в "+ДопЧисло"
    elif '-' in innerDice:
        dividedEdgesAndAdditionalNumber = inputedEdges.split("-")  # Разделяем количество граней и дополнительное отрицательное число
        additionalNumber = int(dividedEdgesAndAdditionalNumber[-1])  # Дополнительное число
        y -= additionalNumber  # Прибавляем дополнительное число к у
        lastDigit = '-' + str(additionalNumber)  # Преобразовываем доп число в "+ДопЧисло"

    edges = int(dividedEdgesAndAdditionalNumber[0])  # Количество граней

    for i in range(1, dice + 1):  # Добавляем случайные значения в х
        x.append(randrange(1, edges))
    for i in x:  # Складываем в у выпавшие случайные значения
        y += i

    printableList = str(x).replace('[', '').replace(']', '')  # Преобразовываем х из [число, число] в "число, число", при этом список станет строкой

    print(y, ' (', printableList, ", ", lastDigit, ')', sep='')  # Вывод в консоль результата


#  Функция броска кубиков
def throwDices():
    dices = input('Please throw some dices like 3d6: ')  # Ввод значения

    while 'd' not in list(dices[1]):  # Пока в конвертированном в список значений не будет d под индексом 1, будет продолжаться ввод и проверка значений
        dices = input('Wrong entry, please enter something like 3d6 or 3d6+2 or 3d6-5: ')

    if 'd' in list(dices[1]):  # Простая проверка ввода
        if '+' in dices or '-' in dices:  # Даннный кейс выполняется если есть доп число со знаком - или +
            throwWithAdditionalNumber(dices)

        else:  # Данный кейс выполняется если нет доп числа со знаком
            throwWithoutAdditionalNumber(dices)


throwDices()
