while True:
    print('~~~~~~~~ Выбери номер задачи ~~~~~~~~')
    print('1. Сумма цифр')
    print('2. Журавлики')
    print('3. Билетики')
    print('4. Шоколад')
    print('5. Убить')
    choice = input('Ввод: ')
    if choice == '1':
        while True:
            num = int(input('Введите трёхзначное число: '))
            if len(str(num)) == 3:
                s = 0
                while num > 0:
                    digit = num % 10
                    s += digit
                    num //= 10
                print(s)
                break
            else:
                print('Ты не очень умненький, да?')
                print()
        print()
    elif choice == '2':
        s = int(input('Введите кол-во журавликов: '))
        kate = int(s / 1.5)
        guys = int(kate / 2)
        print('Петер: {} \nМари: {} \nСерж: {}'.format(guys, kate, guys))
        print()
    elif choice == '3':
        while True:
            num = int(input('Введите шестизначный номер: '))
            if len(str(num)) == 6:
                s1 = s2 = 0
                first = num // 1000
                last = num % 1000
                for i in range(6):
                    s1 += first % 10
                    s2 += last % 10
                    first //= 10
                    last //= 10
                if s1 == s2:
                    print('yes')
                else:
                    print('no')
                break
            else:
                print('Я просил шестизначное!')
                print()
    elif choice == '4':
        x = int(input('Введите длину шоколадки: '))
        y = int(input('Введите ширину шоколадки: '))
        k = int(input('Введите кол-во долей: '))
        if k % x == 0 or k % y == 0:
            print('yes')
        else:
            print('no')
        print('~ я ненавижу белый шоколад ~')
        print()
        print()
    elif choice == '5':
        print('Ну и пока.')
        exit()


