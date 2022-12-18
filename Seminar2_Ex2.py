'''
Стоимость строки:
Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, 
что один любой символ (в том числе пробел) стоит 60 копеек. 
Ответ дайте в рублях и копейках в соответствии с примерами.

Формат входных данных:
На вход программе подается строка текста.

Формат выходных данных:
Программа должна вывести стоимость строки.

Тестовые данные:
Sample Input 1:
Привет, как дела?!
Sample Output 1:
10 р. 80 коп.
Sample Input 2:
Тимур - лучший математик на свете!!
Sample Output 2:
21 р. 0 коп.
'''
text = input("Enter the text: ")
print(f"Sample Input:\n {text}")
CostText=len(text)*60

'''
CostText=0
i=0
while i<len(text):
    CostText=CostText+60
    i+=1
    '''
# CostText=0
#for i in text:
#   CostText=CostText+60
print(f"Sample Output:\n{CostText//100} р. {CostText%100} коп.")
