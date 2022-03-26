from random import randrange

# 6 - Выбрасыватель игральных костей
# Dungeons & Dragons и других настольных ролевых играх используются специальные игральные кости с 4, 8, 10, 12 или даже 20 гранями.
# В этих играх есть также специальные обозначения для бросков различных костей.
# Например, 3d6 означает выбрасывание трех шестигранных костей, а 1d10+2 — выбрасывание одной десятигранной кости с добавлением к броску бонуса в два очка.
# Представленная ниже программа моделирует подобные броски костей на случай, если вы забыли захватить с собой свои.
# Она также моделирует выбрасывание не существующих физически костей, например 38-гранных.
# Программа в действии.
# Результат выполнения diceroller.py выглядит следующим образом:
# --сокращено--
# >	3d6
# 7 (3, 2, 2)
# >	1d10+2
# 9 (7, +2)
# >	2d38-1
# 32 (20, 13, -1)

dices = input().split('d')


def throwDices(inputedDices, inputedEdges):
    if '+' in "".join(dices):  # Выполняется при введенном отрицательном доп числе
        # Количество кубиков
        dice = int(inputedDices)
        # Разделяем количество граней и дополнительное число
        dividedEdgesAndAdditionalNumber = inputedEdges.split("+")

        # Количество граней
        edges = int(dividedEdgesAndAdditionalNumber[0])
        # Дополнительное число
        additionalNumber = int(dividedEdgesAndAdditionalNumber[-1])

        # х - список выпавших граней, у - итоговое число
        x, y = [], 0
        # Добавляем случайные значения в х
        for i in range(1, dice + 1):
            x.append(randrange(1, edges))
        # Складываем в у выпавшие случайные значения
        for i in x:
            y += i

        # Прибавляем дополнительное число к у
        y += additionalNumber

        # Преобразовываем доп число в "+ДопЧисло"
        lastDigit = '+' + str(additionalNumber)

        # Преобразовываем х из [число, число] в "число, число", при этом список станет строкой
        printableList = str(x).replace('[', '').replace(']', '')

        # Вывод в консоль результата
        print(y, ' (', printableList, ", ", lastDigit, ')', sep='')

    elif '-' in ''.join(dices):  # Выполняется при введенном отрицательном доп числе
        # Количество кубиков
        dice = int(inputedDices)
        # Разделяем количество граней и дополнительное число
        dividedEdgesAndAdditionalNumber = inputedEdges.split("-")

        # Количество граней
        edges = int(dividedEdgesAndAdditionalNumber[0])
        # Дополнительное число
        additionalNumber = int(dividedEdgesAndAdditionalNumber[-1])

        # х - список выпавших граней, у - итоговое число
        x, y = [], 0
        # Добавляем случайные значения в х
        for i in range(1, dice + 1):
            x.append(randrange(1, edges))
        # Складываем в у выпавшие случайные значения
        for i in x:
            y += i

        # Отнимаем дополнительное число к у
        y -= additionalNumber
        # Добавляем доп отрицательное число в список
        x.append(-additionalNumber)
        # Преобразовываем х из [число, число] в "(число, число)", при этом лист станет строкой
        printedList = str(x).replace('[', '(').replace(']', ')')
        # Вывод в консоль результата
        print(y, printedList)

    else:  # Кейс выполняется в случае, если нет Дополнительного числа
        # х - список выпавших граней, у - итоговое число
        x, y = [], 0
        # Добавляем случайные значения в х
        for i in range(1, int(inputedDices) + 1):
            x.append(randrange(1, int(inputedEdges)))
        # Складываем в у выпавшие случайные значения
        for i in x:
            y += i
        # Преобразовываем х из [число, число] в "(число, число)", при этом лист станет строкой
        printedList = str(x).replace('[', '(').replace(']', ')')
        # Вывод в консоль результата
        print(y, printedList)


throwDices(dices[0], dices[1])
