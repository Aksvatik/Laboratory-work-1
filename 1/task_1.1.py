def validate_user_num(num):                   #Функция проверки
    if num.isnumeric() and int(num) > 0:      #Метод .isnumeric проверяет есть ли числа в строке
        return int(num)                       #Если в строке есть число, аргумент num становится целочисленным
    else:
        return None                           #Если в строке нет чисел


while True:
    user_num = input("Введите число: ")                        #Запрос числа
    checked_num = validate_user_num(user_num)                  #Присваивание переменной значения validate_user_num(user_num)
    if checked_num is not None:                                #Проверка на значение функции
        for i in range(1, checked_num + 1):                    #Перебор всех i от 1 до числа пользователя включительно
            print(i)                                           #Вывод чисел
        break
    else:                                                      #В противном случае
        print("Вводите только положительные числа больше 0.")