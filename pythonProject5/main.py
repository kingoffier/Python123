try:
    first_num=int(input())
    second_num=int(input())
    result=first_num/second_num
except ZeroDivisionError:
    print("Делить на 0 нельзя")
except ValueError:
    print("Введено некорректное число")
else:
    print("Частное от деления:",result)