# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
#  Выдать без повторений в порядке возрастания все те числа, которые встречаются в 
# обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами 
# элементы множеств.

import random

n = int(input("n - кол-во элементов первого множества: "))
m = int(input('m - кол-во элементов второго множества: '))

my_list_first = [random.randint(1, 10) for _ in range(n)]
print(my_list_first)
print(set(my_list_first))
my_list_second = {random.randint(1, 10) for _ in range(m)}
print(my_list_second)

result = my_list_first.intersection(my_list_second)
print(result)

sorted_result = list(result)
sorted_result.sort()
print(sorted_result)