# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as rnd
def randomize(input_list, qtys):
    """Функция для создания массива со случайными целыми числами из пустого входящего массива.
    На входе ожидается пустой массив и количество элементов, которое должно быть сгенерировано
    """
    i = 0
    qtys = int(qtys)
    input_list = []
    while i < qtys:
        input_list.append(rnd(0, 10))
        i += 1
    return input_list
    
def sum_elem (input_list):
    """ Находит сумму нечётных элементов массива"""
    i=1
    sum=0
    while i<len(input_list):
        sum+=input_list[i]
        i+=2
    return sum

qty = input('Введите количество элементов массива: ')
pure_list = []
pure_list = randomize(pure_list,qty)
print(pure_list)
print("Сумма элементов под нечётными индексами: ",int(sum_elem(pure_list)))