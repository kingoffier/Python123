name=input("Укажите свое имя:")
file=open('log_calc.txt','a',encoding='utf-8')
file.write(f'Пользователь: {name}\n')
while True:
    try:
        num_1=int(input("Введите первое число:"))
        oper=input("Введите операцию % + - * /  :")
        num_2=int(input("Введите второе число:"))
        result = eval(f"{num_1} {oper} {num_2}")
        file.write(f"Совершается операция {num_1} {oper} {num_2} = {result}")
    except ZeroDivisionError:
        num_2=int(input("Делить на 0 нельзя"))
        file.write(f"Ошибка деления на 0\n")
        file.write(f"Введено новое число: {num_2}")
    except SyntaxError:
        oper=input("Введите корректную операцию % + - * /")
        file.write(f"Ввод некорректной операций\n")
        file.write(f"Введена новая операция: {oper}")
    finally:
        result=eval(f"{num_1} {oper} {num_2}")
        print(f"Результат операции: {num_1} {oper} {num_2}")
        file.write(f"Результат: {num_1} {oper} {num_2}")
        is_continue=input("Продолжить работу? ")
        if is_continue== "Нет":
            print("Пока")
            file.close()
            break
