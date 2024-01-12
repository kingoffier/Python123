try:
    first_num=int(input("Введите первое число:"))
    second_num=int(input("Введите второе число:"))
    result=first_num % second_num
    if(second_num==0):
        second_num=int(input("Введите второе число:"))
except ZeroDivisionError:
    second_num = int(input("Введите второе число:"))
except ValueError:
    print("Введено некорректное число")
    first_num = int(input("Введите первое число:"))
    second_num = int(input("Введите второе число:"))
else:
    print("Остаток от деления:",result)
finally:
    if second_num!=0:
        result=first_num%second_num
        print(result)
    else:
        print("Делить на 0 нельзя")