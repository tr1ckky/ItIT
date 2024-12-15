print('Введите ваше имя и возраст:')
name, age = str(input()), str(input()) 
if age == '':
        age = 30
def describe_person(name, age=30):
        return 'Имя:' + name + '\nВозраст:' + str(age)
print(describe_person(name))