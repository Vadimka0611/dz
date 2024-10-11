num1 = int(input("Enter your first number: "))  # Ожидаю первое число от пользователя

while True:
    while True:  # Цикл для ввода второго числа
        num2 = int(input("Enter your second number: "))
        if num2 == 0:
            print("You can't divide by 0! Try again.")
        else:
            break  # Если второе число корректное, выходим из внутреннего цикла

    # Выполняем расчеты
    result1 = num1 + num2
    result2 = num1 - num2
    result3 = num1 * num2
    result4 = num1 / num2

    # Выводим результаты
    print(f"{num1} + {num2} = {result1}")
    print(f"{num1} - {num2} = {result2}")
    print(f"{num1} * {num2} = {result3}")
    print(f"{num1} / {num2} = {result4}")

    # Спрашиваем пользователя, хочет ли он продолжить или выйти
    user_input = input("Enter 'n' to exit the program or 'y' to continue: ")
    if user_input == "n":  # Если пользователь вводит "n", выходим из цикла
        print("Goodbye")
        break  # Завершаем цикл и программу
