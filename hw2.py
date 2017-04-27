#Написать программу поиска самого длинного слова в строке, разделенной пробелами.
a = (input("please, write a line\n")).split()
longestLength = 0
longestWord = ""
for word in a:
    if len(word) > longestLength:
        longestWord=word
        longestLength = len(word)
print("Longest word:", longestWord)

#Написать программу поиска самого длинного слова в строке, разделенной точкой запятой.
a = (input("please, write a line,separating words with (;) \n")).split(";")
longestLength = 0
longestWord = ""
for word in a:
    if len(word) > longestLength:
        longestWord=word
        longestLength = len(word)
print("Longest word:", longestWord)

#Написать программу самого короткого слова который выделяется знаком который пользователь вводит в интерактивном режиме
b = input("choose a splitting sign\n")
a = input('write a line\n')
longest = len(a)
a=a.split(b)
shortest = ""
for element in a:
    if len(element)<longest:
        shortest = element
        longest = len(element)
print("Shortest word:", shortest)

#Написать программу которое находит введенное слово в строке которое также вводится пользователем в интерактивном режиме
a=input("Please,choose a word to find\n")
b=input("Please write a line\n").split()
for word in b:
        if word ==a:
            print(b.index(a))

#Посчитать количество слов в предложении которое вводит пользователь
a=input("Please write a line\n").split()
print(len(a))





