import my_package.int_module

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

print("Сумма: ", my_package.int_module.sum(num1, num2))
print("Разница ", my_package.int_module.sub(num1, num2))
print("Умножение ", my_package.int_module.mul(num1, num2))


import my_package.str_module

name = input("Как тебя зовут?\n")
word = input("Напишите любое слово: ")

print(my_package.str_module.greet(name))
print("Верхний регистр", my_package.str_module.big_str(word))


