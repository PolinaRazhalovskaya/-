while True:
    a = input("Введите символ: ")
    if a.isdigit():
        print("Это цифра!")
    elif a.isalpha():
        print("Это буква!")
    else:
        print("Это не цифра и не буква!")
