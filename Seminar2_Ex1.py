'''
На колесе рулетки карманы пронумерованы от 0 до 36. Ниже приведены цвета карманов: 
карман 0 зеленый;
для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, 
карманы с четным номером – черный;
для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, 
карманы с четным номером – красный;
для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, 
карманы с четным номером – черный;
для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, 
карманы с четным номером – красный.
Напишите программу, которая считывает номер кармана и показывает, 
является ли этот карман зеленым, красным или черным. Программа должна вывести сообщение об ошибке, 
если пользователь вводит число, которое лежит вне диапазона от 0 до 36.

Формат входных данных
На вход программе подаётся одно целое число.
Формат выходных данных
Программа должна вывести цвет кармана либо сообщение «ошибка ввода», 
если введённое число лежит вне диапазона от 0 до 36
'''
n = int(input('Enter the count of Ruletka: n= '))

if n<0 or n>36:
    print('Error')
elif n==0:
    print(f'Color {n} -> Green ')
elif 0<n<11 and n%2!=0:
    print(f'Color {n} -> Red ')
elif 0<n<11 and n%2==0:
    print(f'Color {n} -> Black ')
elif 10<n<19 and n%2!=0:
    print(f'Color {n} -> Black ')
elif 10<n<19 and n%2==0:
    print(f'Color {n} -> Red ')
elif 18<n<29 and n%2!=0:
    print(f'Color {n} -> Red ')
elif 18<n<29 and n%2==0:
    print(f'Color {n} -> Black ')
elif 28<n<37 and n%2!=0:
    print(f'Color {n} -> Black ')
else:
    print(f'Color {n} -> Red ')
