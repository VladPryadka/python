import random
secret_number = random.randint(1, 10)

guess = int(input("�������� ����� �� 1 �� 10: "))

if guess == secret_number:
    print("����������! �� ������� �����!")
else:
    difference = abs(secret_number - guess)
    if difference <= 2:
        print("������")
    elif difference <= 4:
        print("�����")
    else:
        print("�������")
    print(f"���������� ����� ����: {secret_number}")
