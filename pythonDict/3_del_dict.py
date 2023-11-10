# Удаление из словаря
# 1)Оператор del - удаляет элемент по указанному ключу
#       del название_словаря[ключ]
# 2)Метод pop - удаляет и возвращает элемент по указанному ключу
#       название_словаря.pop(ключ)
# 3)Метод popitem() - удаляет и возвращает последний по порядку элемент
#       название_словаря.popitem()
russian_dict=dict(
    кошка=['cat','pussycat'],
    красивый=['beautiful','nice','lovely']
)
item = input("Введите элемент:")
russian_dict['собака']=['dog', 'pussydog']
russian_dict.pop("кошка")
del russian_dict["красивый"]
if item in russian_dict:
    result = russian_dict.popitem()
    print(result)
else:
    print("dinahy aha maha")
print(russian_dict)
