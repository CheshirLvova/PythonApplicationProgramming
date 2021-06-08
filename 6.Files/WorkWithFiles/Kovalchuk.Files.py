# модулі для роботи з файлами та ресурсами операційної системи
import os
from os import path
import glob
import time

def pretty_print(a_dict): #друк елементів словника
    for key in a_dict:
        print(key, ':', a_dict[key])
    pass
##Задача 1. В папці є 10-12 файлів різного типу. Знайти і показати два файли найдавнішої
##дати створення і два файли найновішої дати незалежно від типу (надрукувати імена і дати).
##Для цього треба спочатку підготувати саму папку і записати туди довільні файли.
##Надрукувати знайдені файли і цілий список файлів для порівняння.
def task1():
    files = {}
    dirname = os.path.abspath('.')
    ls = os.listdir('Test1') # список всіх файлів і папок, які є в поточній папці
    print("\nфайли, що містяться у папці Test1:")
    for filename in range(len(ls)):
        ls[filename] = os.path.join(dirname, 'Test1', ls[filename])
    for filename in range(len(ls)):
        gt = os.path.getmtime(ls[filename])
        sttm = time.localtime(gt)
        tm = "Дата змінення: {0},{1},{2}, {3}:{4}:{5}".format(sttm.tm_mday, sttm.tm_mon, sttm.tm_year, sttm.tm_hour, sttm.tm_min, sttm.tm_sec )
        files.update([(ls[filename], tm)])
    pretty_print(files)
    oldvalues = list(files.values())
    keys = list(files.keys())
    val = list(files.values())
    val.sort()
    need = {}
    n = []
    for i in range(len(val)):
        if i == 0 or i == 1 or i == len(val)-1 or i == len(val)-2:
            n.append(oldvalues.index(val[i]))
    for i in range(len(n)):
            need.update([(keys[n[i]], files[keys[n[i]]])])
    print("\nфайли, що були зміненими останніми та першими у папці (по 2 відповідно):")
    pretty_print(need)
    pass
##Задача 2. В двох різних папках записано по 8-10 файлів. Деякі файли можуть бути
##дубльовані за ознакою однакового імені і розміру. Підготувати для тестування такі папки і
##файли. Знайти дубльовані файли – показати їх імена і папки, в яких вони є.
def task2():
    files = {}
    dir1 = {}
    dir2 = {}
    dirname = os.path.abspath('.')
    ls1 = os.listdir('Test1') # список всіх файлів і папок, які є в поточній папці
    for filename in range(len(ls1)):
        ls1[filename] = os.path.join(dirname, 'Test1', ls1[filename])
    ls2 = os.listdir('Test2') # список всіх файлів і папок, які є в поточній папці
    for filename in range(len(ls2)):
        ls2[filename] = os.path.join(dirname, 'Test2', ls2[filename])
    for filename in range(len(ls1)):
        sz = os.path.getsize(ls1[filename])
        dir1.update([(ls1[filename], sz)])
    for filename in range(len(ls2)):
        sz = os.path.getsize(ls2[filename])
        dir2.update([(ls2[filename], sz)])

    print("\nфайли з першої папки:")
    pretty_print(dir1)
    print("\nфайли з другої папки:")
    pretty_print(dir2)
    for i in range(len(dir1)):
        for j in range(len(dir2)):
            if dir1[ls1[i]] == dir2[ls2[j]]:#перевірка реалізована таким чином,бо в другій папці є менше файлів, аніж у першій
                files.update([(ls2[j], dir2[ls2[j]])])
    print("\nфайли, які є однаковими:")
    pretty_print(files)
    pass



##Задача 3. В поточній папці є 4 вкладені папки, в кожній з яких є по 6-7 файлів різних
##типів. Підготувати такі папки і файли для тестування. Зробити запит на консоль про тип
##файлів, які нас цікавлять: doc, py, txt, dll, exe, json, pdf, jpg, xml, чи інші. Надрукувати
##загальний список файлів визначеного типу, які є у всіх вкладених папках разом.
def task3():
    print('Файли з розширенням ".txt":')
    part = glob.glob('Test3\*.txt') # список файлів, які відповідають заданому шаблону
    
    for i in range(len(part)):
        print(part[i])
    part = glob.glob('Test3\A\*.txt') # список файлів, які відповідають заданому шаблону
    for i in range(len(part)):
        print(part[i])
    part = glob.glob('Test3\A\B\*.txt') # список файлів, які відповідають заданому шаблону
    for i in range(len(part)):
        print(part[i])
    part = glob.glob('Test3\A\B\C\*.txt') # список файлів, які відповідають заданому шаблону
    for i in range(len(part)):
        print(part[i])
    pass

#Виконання завдань
print("Завдання 1")
task1()
print('\n')
print("Завдання 2")
task2()
print('\n')
print("Завдання 3")
task3()
