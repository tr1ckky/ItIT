print('Введите первое число, затем второе:')
x, y = int(input()), int(input())
def max_of_two(x, y):
    return 'Наибольшее число: ' + str(max(x, y)) 
print(max_of_two(x, y))