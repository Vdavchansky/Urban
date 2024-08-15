import random


def find_password(n):
    password = ""
    for i in range(1, n // 2 + 1):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                password += str(i) + str(j)
    return password


while True:
    n = random.randint(3, 20)
    print(f"Число в первой вставке: {n}")
    result = find_password(n)
    print(f"Пароль: {result}")

    input("Нажмите Enter, чтобы продолжить...")
