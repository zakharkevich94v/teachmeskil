choice = None
while choice != "0":
    print(
        """
        0 - Выйти
        1 - Ввести число
        """
    )
    choice = input("Ваш выбор: ")
    print()
    # Выход из цикла
    if choice == "0":
        print("До свидания")
    
    # Проверка числа
    elif choice == "1":
        number = int(input("Введите число: "))
        if number % 1000 == 0:
            print("millenium")
        else:
            print("Введите число которое делится на 1000 без остатка")

    # Выход из программы
    input("\n\nНажмите Enter, чтобы выйти")