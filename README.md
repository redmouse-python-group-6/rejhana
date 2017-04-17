# -*- coding: utf-8 -*-
print("Общество в начале XXI века")
x = int(input("Please indicate your age\n"))
if -1<x<7:
    print("Вам в детский сад")
elif 6<x<18:
            print("Вам в школу")
elif 17<x<25:
    print("Вам в профессиональное учебное заведение")
elif 24<x<60:
    print("Вам на работу")
elif 59<x<121:
    print("Вам предоставляется выбор")
else:
    str="Ошибка! Это программа для людей!\n"
    print(str*5)