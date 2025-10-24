def max_of_two(x, y):
    if x != y:
        return f"Большее число: {max(x, y)}"
    else:
        return f"Числа равны."


user_num1 = int(input("Введите первое число: "))
user_num2 = int(input("Введите второе число: "))

print(max_of_two(user_num1, user_num2))