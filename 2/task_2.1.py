def greet(name):
    return f"Привет, {name.title()}!"


def square(number):
    return format(number**2, ".2f")


def max_of_two(x, y):
    if x != y:
        return f"\nБольшее число: {max(x, y)}"
    return "\nЧисла равны."


def checking_name(text):
    while True:
        name = input(text).strip()
        if not name:
            print("Имя не может быть пустым.\n")
            continue
        if all(part.isalpha() for part in name.split()):
            name = " ".join(name.split())
            return name
        print("Имя не должно содержать цифры или символы.\n")


def error_checking(text):
    while True:
        number = input(text)
        try:
            return float(number)
        except ValueError:
            print("Вводите только числа.\n")


user_name = checking_name("Как тебя зовут?\n")
print(greet(user_name))

user_num = error_checking("Введите число: ")
print(square(user_num))


user_num1 = error_checking("Введите первое число: ")
print("")
user_num2 = error_checking("Введите второе число: ")
print(max_of_two(user_num1, user_num2))