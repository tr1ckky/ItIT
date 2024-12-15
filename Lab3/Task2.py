def add():
    user_text = input('Введите текст для записи в файл:\n')
    with open("user_input.txt", 'a') as file:
        file.write(user_text)
        print("Текст записан")
add()