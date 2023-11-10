# Дополнительные полезные функции и методы словарей
# Метод keys() - возвращает список ключей словаря
# Метод values() - возвращает список значений словаря
# Метод items() - возвращает список из пар (кортежи) ключ- значение
russian_dict=dict(
    кошка=['cat','pussycat'],
    красивый=['beautiful','nice','lovely']
)
print(russian_dict.keys())
print(russian_dict.values())
print(russian_dict.items())
#Вывод всех ключей словаря
#for key in название_словаря: print(key)
print("="*100)
for key in russian_dict:
    print(key)
#Вывод всех значений
#for value in название_словаря.values(): print(value)
print("="*100)
for value in russian_dict.values():
    print(value)

#Вывод всех пар «ключ / значение»
#for key,value in название_словаря.items(): print(key,value)
print("="*100)
for key, value in russian_dict.items():
    print(key,value)

# Метод clear() - полностью очищает словарь (удаляет все пары ключ-значение)
# Метод copy()  - возвращает копию указанного  словаря
print("="*100)
ru_dict = russian_dict.copy()
russian_dict.clear()
print(ru_dict["кошка"])
# создание нового словаря  из  последовательности key и значениями value. По умолчанию value присваивается значение None.
#название_словаря=dict.fromkeys(['ключ1', 'ключ2','ключ3'],value)
ru_dictionary=dict.fromkeys(['key1','key2','key3'],0)
ru_dictionary2=dict.fromkeys(['key1','key2','key3'])
print(ru_dictionary)
print(ru_dictionary2)

