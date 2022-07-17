import math
# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input('Введите номер дня недели: '))
if day<=5:
    print("Нет, рабочий день")
elif day>5 and day<=7:
    print('Ура, входной')
else:
    print('Нет такого дня')

# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


x = int(input("Введите Х "))
y = int(input('Введите Y '))
z = int(input('Введите Z '))
if (not (x or y or z)) == (not x and not y and not z):
    print('True')
else:
    print('False')

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).


x = int(input('Введите координату Х: '))
y = int(input('Введите координату Y '))

if x > 0 and y > 0:
    print('--> 1')
elif x < 0 and y > 0:
    print('--> 2')
elif x < 0 and y < 0:
    print('--> 3')
elif x > 0 and y < 0:
    print('--> 4')
else:
    print('Координаты не правильные')


#  4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

f = int(input('Введите номер четверти: '))
if f == 1:
    print("Координаты: X от 0 до плюс бесконечности; Y от 0 до плюс бесконечности")
elif f == 2:
    print("Координаты: X от 0 до минус бесконечности; Y от 0 до плюс бесконечности")
elif f == 3:
    print("Координаты: X от 0 до минус бесконечности; Y от 0 до минус бесконечности") 
elif f == 4:
    print("Координаты: X от 0 до плюс бесконечности; Y от 0 до минус бесконечности")
else:
    print('Такой четверти нет')


#  5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

#  Пример:

#  - A (3,6); B (2,1) -> 5,09
#  - A (7,-5); B (1,-1) -> 7,21


a1 = int(input('Первое значение А '))
a2 = int(input('Второе значение А '))
b1 = int(input('Первое значение В '))
b2 = int(input('Второе значение В '))
distance = math.sqrt(((a1-b1)**2)+((a2-b2)**2))
print(round(distance, 2))

