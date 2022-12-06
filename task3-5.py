# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def fill_nega_fibo(negaqty):
    """Возвращает число Фибоначчи от отрицательного значения"""
    if negaqty == 0:
        return
    if negaqty == -1:
        return 1
    if negaqty == -2:
        return -1
    return fill_nega_fibo(negaqty+2)-fill_nega_fibo(negaqty+1)

def fill_posi_fibo(posiqty):
    """Возвращает число Фибоначчи от позитивного значения"""
    if posiqty == 0:
        return 0
    if posiqty == 1:
        return 1
    return fill_posi_fibo(posiqty-1)+fill_posi_fibo(posiqty-2)

def create_fibo(input_array, qty):
    """Возвращает массив значений чисел Фибоначчи от (-1*кол-во элементов) до (кол-во элементов) по возрастанию индексов"""
    nega_fibo = []
    posi_fibo = []
    i = qty
    while i > 0:
        nega_fibo.append(fill_nega_fibo(i*-1))
        i -= 1
    print(nega_fibo)
    i = 0
    while i < qty:
        posi_fibo.append(fill_posi_fibo(i))
        i += 1
    print(posi_fibo)
    return (nega_fibo+posi_fibo)

qty_elements = int(input("Введите количество элементов: "))
fibo_array = []
fibo_array = create_fibo(fibo_array, qty_elements)
print("Фибонначи с отрицательными элементами: ", fibo_array)
