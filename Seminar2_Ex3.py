'''Количество слов:
Дана строка, состоящая из слов, разделенных пробелами. Напишите программу, 
которая подсчитывает количество слов в этой строке.
Формат входных данных:
На вход программе подается строка.
Формат выходных данных:
Программа должна вывести количество слов в строке.

Примечание 1. Кроме слов в тексте могут присутствовать только пробелы (один или несколько).
Примечание 2. Решите задачу в одну строчку кода.
Тестовые данные:
Sample Input 1:
Hello world
Sample Output 1:
2
Sample Input 2:
Timur forever young
Sample Output 2:
3
'''
print("Sample Input:")
text = input("Enter the text: ")
'''#variant1:
count=0
i=0
while i<len(text):
      if text[i] == " ":
        count = count+1
      i=i+1
countWord = count+1
print(f"Sample Output:\n{countWord}")
'''
'''
#variant2:
count=0
for i in text:
    if i == " ":
        count+=1
countWord = count+1
print(f"Sample Output:\n{countWord}")
'''
#variant3:
print(text.count(' ')+1)

