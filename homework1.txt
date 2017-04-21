x= int(input("Please input any number from 1 to 9\n"))
if 0<x<4:
    s = input(("Write a line\n"))
    n = int(input("Write a number of lines\n"))
    print (s*n)
elif 3<x<7:
    m = int(input("Please write the exponent\n"))
    print(x**m)
elif 6<x<10:
    i = 0
        for i in range (0,10):
        x=x+1
        print (x)
else:
        print("Error")