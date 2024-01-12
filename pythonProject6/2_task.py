#  Задача
# Вывести на экран:
# - сумму всех элементов списка
# - среднее арифметическое всех элементов списка
# - максимальное значение списка
# - минимальное значение списка

def arr(arr):
    summ = sum(arr)
    avg = sum(arr) / len(arr)
    minn = min(arr)
    maxx = max(arr)
    print(f'Сумма: {summ}')
    print(f'Среднее арифметическое: {avg}')
    print(f'Минимальное значение: {minn}')
    print(f'Максимальное значение: {maxx}')
    print("--------------------")
    return summ,avg,minn,maxx
'''
first_arr=[]
for i in range(10):
    num=int(input(f"Введите {i+1} элемент:"))
    first_arr.append(num)
arr(first_arr)
'''
second_arr=[12,5,456,-15,64,54,-24]
arr1 = arr(second_arr)[1]
arr2 = arr(second_arr)[2]
arr3 = arr(second_arr)[3]
print(arr(second_arr)[0])
print(arr1)
print(arr2)
print(arr3)

