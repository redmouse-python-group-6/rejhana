#3.	Напишите функцию, которая разбивает введённую строку на слова и выводит по очереди само слова тире ее длина.
x=input("Please, write a line\n").split()
def spl():
   for element in x:print(element,"-",len(element))
spl()

#4.	Написать функцию в которую можно передать сколько угодно значений и оно возводит каждое последующее число в степень предыдущего (первое значение возводим в степень один)
def power():
    i = 0
    a = 1
    for i in range(0, 100):
        x = int(input('Please, input a number\n'))
        print(x ** a)
        a = x
power()