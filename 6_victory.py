again = 'Да'
while again =='Да':
        right: int = 0
        wrong: int = 0

        # 1
        age1 = int(input('Введите год рождения А.С. Пушкина: '))

        if age1 == 1799:
                print('Вы ввели верно, год рождения А.С. Пушкина', age1, 'г.')
                right += 1
        else:
                print('Вы ввели неверно, следующий вопрос.')
                wrong += 1

        # 2
        age2 = int(input('Введите год рождения М.В. Ломоносова: '))

        if age2 == 1711:
                print('Вы ввели верно, год рождения М.В. Ломоносова:', age2, 'г.')
                right += 1
        else:
                print('Вы ввели неверно, следующий вопрос.')
                wrong += 1

        # 3
        age3 = int(input('Введите год рождения А.В. Суворова: '))

        if age3 == 1730:
                print('Вы ввели верно, год рождения А.В. Суворова', age3, 'г.')
                right += 1
        else:
                print('Вы ввели неверно, следующий вопрос.')
                wrong += 1

        # 4
        age4 = int(input('Введите год рождения С.А. Есенина: '))

        if age4 == 1895:
                print('Вы ввели верно, год рождения С.А. Есенина', age4, 'г.')
                right += 1
        else:
                print('Вы ввели неверно, следующий вопрос.')
                wrong += 1

        # 5
        age5 = int(input('Введите год рождения В.В. Маяко́вского: '))

        if age5 == 1893:
                print('Вы ввели верно, год рождения В.В. Маяко́вского', age5, 'г.')
                right += 1
        else:
                print('Вы ввели неверно, попробуйте еще раз.')
                wrong += 1
        print('Верно', right)
        print('Ошибок', wrong)
        print('Верно', right * 100/5, 'процентов')
        print('Ошибок', wrong * 100/5, 'процентов')

        again = input('Если хотите начать игру занаво, то напишите  "Да", если нет то напишите  "Нет" ' )  # да/нет


