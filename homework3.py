#5.	Переписать первое задание разбив его на модули
#6.	Собрать все модули в пакет
import mult
import lst
import exp
x= int(input("Please input any number from 1 to 9\n"))
if 0 < x < 4: mult.mult()
elif 3 < x < 7: exp.exp(x)
elif 6 < x < 10: lst.lst(x)
else: print("Error!!!")