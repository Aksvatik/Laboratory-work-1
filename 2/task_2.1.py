def great(name):
    print(f"Привет, {name.capitalize()}!")


user_name = input("Как тебя зовут?\n").strip()

great(user_name)

#--------------------------------------

def square(number):
    return number**2


#user_num = int(input("Введите число: "))

#print(square(user_num))

#-------------------------------------

def max_of_two(x, y):
    if x != y:
        return f"Большее число: {max(x, y)}"
    else:
        return f"Числа равны."


#user_num1 = int(input("Введите первое число: "))
#user_num2 = int(input("Введите второе число: "))

#print(max_of_two(user_num1, user_num2))