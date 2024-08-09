x = int(input("Введите первое число: "))
y = int(input("Введите второе число: "))
z = int(input("Введите третье число: "))
if x == y == z:
    print(3)
elif x == y or x == z or y == z:
    print(2)
elif x != y != z:
    print(0)
