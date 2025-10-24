def greet(name):
    return f"Привет, {name.title()}!"


def checking_name(text):
    while True:
        variable = input(text).strip()
        if all(part.isalpha() for part in variable.split()):
            return variable
        print("Имя не должно содержать цифры или символы.\n")


user_name = checking_name("Как тебя зовут?\n")

print(greet(user_name))