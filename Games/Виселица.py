# Игра Виселица
def hangman(word):
    wrong = 0  #сколько неправильных предположений сделано
    stages = ["_____________            ",
              "|            |           ",
              "|            |           ",
              "|            O           ",
              "|          / | \         ",
              "|           / \          ",
              "|                        ",
              ]
    rletters = list(word)
    board = ["__"] * len(word) #визуал - какие буквы уже угаданы (или ничего: __ __ __)
    win = False #победил ли уже игрок?
    print("Добро пожаловать на казнь")
    while wrong < len(stages):
        print("\n") #для лучшего отображения
        msg = "Введите букву: "
        char = input(msg)
        if char in rletters:            #если значение буквы-догадки содержится в загаданном слове
            cind = rletters.index(char) #находим индекс этой буквы в загаданном слове
            board[cind] = char          #обновляем board-вывод визуального отображения
            rletters[cind] = '$'        #заменяем правильно угаданный символ в слове знаком $ (чтобы в случае повторяющихся букв, алгоритм не выводил один и тот же индекс)
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))
        if "__" not in board:
            print("Вы выиграли! Было загадано слово:")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("ВЫ проиграли! Было загадано слово: {}.".format(word))
