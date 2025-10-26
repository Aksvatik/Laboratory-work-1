def validate_user_num(num):
    if num.isnumeric() and int(num) > 0:
        return int(num)
    else:
        return None


while True:
    user_num = input("Введите число: ")
    checked_num = validate_user_num(user_num)
    if checked_num is not None:
        for i in range(1, checked_num + 1):
            print(i)
        break
    else:
        print("Вводите только положительные числа больше 0.")