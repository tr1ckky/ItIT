mode = input("Выберите способ чтения файла:\n Введите '1' для чтения всего файла\n Введите '2' для построчного чтения\n")
def read_file(mode):
    if mode == '1':
        with open('example.txt', 'r') as file:
            content = file.read()
            print(content)
    elif mode == '2':
        with open('example.txt', 'r') as file:
            for line in file:
                print(line, end = '')
    else:
        print("Неккоректный режим чтения, используйте '1' или '2'.")
read_file(mode)