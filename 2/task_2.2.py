#Функция вывода приветствия с пользователем
def describe_person(name, age=30):
    print(f"Привет, {name.title()}. Вам {age}!")


def user_agreement():
    while True:
        agreement = input("Согласны ли Вы указать возраст? Y/N\n").upper().strip()
        if agreement == "Y":
            return True
        if agreement == "N":
            return False
        else:
            print("Вводите только Y - согласен(а) или N - не согласен(а)")


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


def checking_age(text):
    while True:
        number = input(text)
        if number.isdigit():
            num = int(number)
            if num > 0:
                return num
            print("Возраст должен быть положительным.")
        else:
            print("Вводите только цифры.")


user_name = checking_name("Введите свое имя: ")
if user_agreement():
    user_age = checking_age("Введите свой возраст: ")
    describe_person(user_name, user_age)
else:
    describe_person(user_name)