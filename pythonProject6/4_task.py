#  Задача
# Напишите функцию, которая:
# - принимает на вход строку
# - возвращает количество гласных букв в строке.
# В строке используются только латинские символы
# Регистр букв может быть любой.
def count_vowels(str):
    vowels=['e','o','a','u','i','y']
    count = 0
    for item in str:
        if item.lower() in vowels:
            count+=1
    return count
data=input("Введите строку: ")
print(count_vowels(data))