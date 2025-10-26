def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def checking_num(text):
    while True:
        number = input(text).strip()
        if number.isdigit():
            return int(number)
        print("Вводите только положительные числа.")


user_num = checking_num("Введите число: ")

print(is_prime(user_num))