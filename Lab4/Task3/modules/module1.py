def pif ():
    print("Для вычисления гипотенузы введите:")
    a, b = int(input("Катет a: ")), int(input("Катет b: "))
    c2 = a**2 + b**2
    c = c2**0.5
    return print(f"Гипотенуза равна: {c}")