def comparison_num(a, b):
    if a > b:
        return f"\nБольшее число: {a}"
    if a < b:
        return f"\nБольшее число: {b}"
    return "\nЧисла равны."


def error_checking(text):
    while True:
        variable = input(text)
        try:
            return float(variable)
        except ValueError:
            print("Вводите только числа.")


user_num1 = error_checking("Введите первое число: ")
print("")
user_num2 = error_checking("Введите второе число: ")

print(comparison_num(user_num1, user_num2))