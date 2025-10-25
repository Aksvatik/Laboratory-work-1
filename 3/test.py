from tokenize import endpats


def read_file(mode):
    mode = input("Выберите метод: all - чтение целиком"
                 "line - ..."
                 "lines - ...")
    with open("test.txt", "r") as file:
        if mode == "all":
            content = file.read()
            print(content)
        elif mode == "line":
            line = file.readline()
            print(line)
        elif mode == "lines":
            lines = file.readlines()
            for line in lines:
                print(line)

read_file("all")
read_file("line")
read_file("lines")