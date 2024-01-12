#  Задача
# Вывести на экран сумму всех цифр заданного числа
# дано: 123 -> вывод: 6
# дано: 337 -> вывод: 13
def sum_digits(num):
    summ=0
    while num>0:
        summ+=num%10
        num=num//10
    return summ
a=int(input("Введите число: "))

print(sum_digits(a))

