# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91

from random import randint as rnd

def real_fill(input_array, qty):
    """Заполняет массив случайными вещественными числами с 5 значящими символами
    На входе ожидает пустой массив, который нужно заполнить и количество элементов, которое нужно сгенерировать"""
    i = 0
    while i < qty:
        input_array.append(round(rnd(1, 10)+float(2*1/rnd(1, 10)) +
                           float(1/rnd(1, 100))+float(1/rnd(1, 1000)), 5))
        i += 1
    return input_array

def dif_float(input_array):
    """Находит разницу между максимальным и минимальным значением дробной части элементов входного массива
    На входе ожидает массив из вещественных чисел"""
    max = input_array[0]-int(input_array[0])
    min = max
    i = 0
    for i in input_array:
        float_digit = i-int(i)
        if float_digit > max:
            max = float_digit
        if float_digit < min:
            min = float_digit
    return round(max-min,5)

qty_elem = int(input("Введите количество элементов массива: "))
real_array = []
real_array = real_fill(real_array, qty_elem)
print(real_array)
print("Разница между максимальным и минимальным значением дробной части элементов = ",
      dif_float(real_array))
