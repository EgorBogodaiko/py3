# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
import math
def to_bin(input_decimal,i):
    """Переводит десятичное число в двоичную систему счисления
    На входе ожидает положительное целое число"""
    
    if (input_decimal< 0):
            return "Не переводится"
    elif (input_decimal> 0):
        temp = input_decimal%2
        return to_bin(input_decimal//2,i+1)+int(temp*math.pow(10,i))
    else:
        return 0
   
decimal_number = int(input("Введите десятичное число: "))
print("Перевод в двоичную систему счисления: ", to_bin(decimal_number,0))

   