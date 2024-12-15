print('Введите число для проверки:') 
number = int(input()) 
def is_prime(number):
    for i in range(2, (number//2) +1):
        if number % i == 0:
            return False
    return True
print(is_prime(number))      