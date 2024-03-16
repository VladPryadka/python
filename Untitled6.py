import random
secret_number = random.randint(1, 10)

guess = int(input("Угадайте число от 1 до 10: "))

if guess == secret_number:
    print("Поздравляю! Вы угадали число!")
else:
    difference = abs(secret_number - guess)
    if difference <= 2:
        print("Горячо")
    elif difference <= 4:
        print("Тепло")
    else:
        print("Холодно")
    print(f"Загаданное число было: {secret_number}")
