mode = input("Выберите способ чтения файла:\n Введите '1' для чтения всего файла\n Введите '2' для построчного чтения\n")
def read_file(filename, mode):
    try:
        if mode == '1':
            with open(filename, 'r') as file:
                content = file.read()
                print(content)
        elif mode == '2':
            with open(filename, 'r') as file:
                for line in file:
                    print(line, end = '')
        else:
            print("Неккоректный режим чтения, используйте '1' или '2'.")
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден. Пожалуйста, проверьте корректность имени файла и попробуйте ещё раз.")
read_file("example.txt", mode)