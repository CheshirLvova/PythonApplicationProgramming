## Це завдання є підсумковим на основі декількох останніх вивчених тем. Метою завдання
## є напрацювання навиків комплексної розробки окремих складових частин програмних
## проєктів певного цільового призначення.
## За основу свого проєкта можна початково прийняти архітектуру, описану в файлі
## матеріалів "Модель проєкта за даними JSON.pdf" в розділі "Постановка задачі". Зразу
## підкреслимо, що можна будувати проєкт на основі файлів й інших типів, наприклад, xml.
## Приклад архітектури проєкта в графічному зображенні показано на малюнку.

## підключення необхідних для роботи бібліотек
import os
import glob
import json
import subprocess
from functools import reduce
import urllib.request
from datetime import date
from pprint import pprint

## підключення бібліотек для створення віконної програми :3
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter.ttk import Checkbutton
from tkinter.ttk import Radiobutton
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import ttk
from tkinter import filedialog
from tkinter import Menu

## - обрати тему, визначити загальний зміст і перелік задач, зафіксувати умови застосування
## Тема моєї роботи: створення програми для перевірки погоди у Львові, перелік задач вказаний
## відповідно з кожною задачею, як коментар, а також у інструкції для користувача


## - визначити джерела постачання даних для виконання задач проєкта; зафіксувати адреси
## серверів чи інші, звідки отримувати дані;
def GetServerAddress(apiKey):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Lviv&appid=$$apiKey$$'
    return url.replace('$$apiKey$$', apiKey)

def GetDataFromServer():
    ##  1) перевірити, чи є дані за сьогоднішній день  
    print('Checking if file with data for this day already exist')

    dirPath = '.\\'
    files = glob.glob(os.path.join(dirPath, '*.json'))

    today = date.today().strftime('%d-%m-%Y')
    filename = dirPath + f'{today}.json'
    ## 2) якщо даних немає – отримати від сервера   
    if filename in files:
        print('File with data for this day already exist')
        return

    print('Connecting to server...')

    remoteaddr = GetServerAddress('1952efb4a7da640d955fd67682858a7f')
    remotefile = urllib.request.urlopen(remoteaddr)  
    ## 3) прийняти рішення на випадок відсутності даних
    print('Get file')

    with open(filename, 'wb') as fsave:     
        fsave.write(remotefile.read())  
        print('File was saved')

    remotefile.close()
    print('Remote file closed')

    print('\nPrint file to python window: ')
    with open(filename) as data_file:
        data = json.load(data_file)
    pprint(data)

    print('\nPrinting finished')

## Завдання 1. Аналіз структури файлу json і показ прикладу даних
def GatherAllData(result_file):
    """ Read all data from result_file and analyze json structure """
    result_file.write('Function to gather data from all .json files started')

    dirPath = '.\\'
    files = glob.glob(os.path.join(dirPath, '*.json'))

    result_file.write('\nAll data files have same structure:')
    with open(files[0]) as data_file:
        one_file_data = json.load(data_file)
        result_file.write('\nMain info:')
        result_file.write(f'\nType of entire document: {type(one_file_data).__name__}')
        result_file.write(f'\nDocument has: {len(one_file_data)} elements')
        result_file.write(f'\nType of every element: {[type(one_file_data[elem]).__name__ for elem in one_file_data.keys()]}:')
        result_file.write(f"\nType of 'main' element: {type(one_file_data['main']).__name__}")
        result_file.write(f"\nValue of 'main':\n{one_file_data['main']}")
        result_file.write("\nSubelements of 'main':\n")
        result_file.write('\n'.join([ str(subvalue) for subvalue in one_file_data['main'].items() ]))
        
    data = []

    for file in files:
        with open(file) as data_file:
            filename = os.path.split(file)[1]
            temp = json.load(data_file)
            data.append({os.path.splitext(filename)[0] : temp})     

    result_file.write('\n\nAll data gathered')
    result_file.write('\nFirst data entry printed for example:\n')   
    json.dump(data[0], result_file, indent=4)
    
    return data
## Завдання 2. Виведення значень за певним ключем
def GetValuesByKey(data, key):
    """ Get values from data by specific key """
    values = []
    
    for record in data: 
        key1 = list(record.keys())[0]
        key2 = record[key1].keys()
        for k in key2:  
            if k == key:
                values.append({"value":record[key1][k], "date":key1})

            elif isinstance(record[key1][k], list):
                for elem in record[key1][k]: 
                    key3 = elem.keys()
                    if key in key3:
                        values.append({"value": elem[key], "date":key1})

            elif isinstance(record[key1][k], dict):  
                key4 = record[key1][k].keys()
                if key in key4:
                    values.append({"value":record[key1][k][key], "date":key1})

    return values
## Завдання 2.  Виведення значення за певним ключем             
def GetValueByKey(result_file, data, key):
    """ Write to result_file values from data by specific key """
    result_file.write(f'\n\nPrint value by key: {key}:')
    a = 'Print value by key:'
    a += key
    values = GetValuesByKey(data, key)
    for value in values:
        if('value'== 'temp' or 'value'=='feels_like' or 'value'== 'temp_min' or 'value'== 'temp_max'):
            value['value'] += - 273.15
        result_file.write(f'\nValue of key: {key} is {value["value"]} on {value["date"]}')
        a += '\nValue of key: '
        a += key
        a += ' is '
        a += str(value["value"])
        a += ' on '
        a += str(value["date"])
    return a
## Завдання 3. Друк максимального значення за допомогою ключа              
def GetMaxValueByKey(result_file, data, key):
    """ Write to result_file max value from data by specific key """
    result_file.write(f'\n\nPrint max value by key: {key}:')
    values = GetValuesByKey(data, key)
    maxPair = max(values, key=lambda value: value["value"])
    if('value'== 'temp' or 'value'=='feels_like' or 'value'== 'temp_min' or 'value'== 'temp_max'):
        maxPair["value"] += - 273.15
    result_file.write(f'\nMax value of key: {key} is {maxPair["value"]} on {maxPair["date"]}')
    
    m = '\nMax value of key: '
    m += key
    m += ' is '
    m += str(maxPair["value"])
    m += ' on '
    m += str(maxPair["date"])
    return m

## Завдання 4. Друк середнього значення по ключу              
def GetAvgValueByKey(result_file, data, key):
    """ Write to result_file average value from data by specific key """
    result_file.write(f'\n\nPrint average value by key: {key}:')

    values = GetValuesByKey(data, key)
    avg = reduce(lambda prev,current: prev + current["value"], values, 0)

    result_file.write(f'\nAvg value of key: {key} is {avg/len(values)}')
    av = '\nAvg value of key: '
    av += key
    av += 'is '
    av += str(avg/len(values))
    return av
## Завдання 5. Друк дат із заданим значенням за ключем                
def GetDaysWithParticulatWeatherCondition(result_file, data, key, value):
    """ Write to result_file days with particulat weather condition """
    result_file.write(f'\n\nPrint dates with given value by key: {key}:')
    d = 'Print dates with given value by key: '
    d += key
    values = GetValuesByKey(data, key)
    vals = filter(lambda x: x["value"] == value, values)
    for val in vals:
        result_file.write(f'\nValue of key: {key} is {val["value"]} on {val["date"]}')
        d += '\nValue of key: '
        d += key
        d += ' is '
        d += val["value"]
        d += ' on '
        d += val["date"]
    return d
## Завдання 6. Друк дат із значенням, більшим, ніж вказане ключем              
def GetDaysWithValueMoreThan(result_file, data, key, diff):
    diff = float(diff)
    """ Write to result_file days with value more than """
    result_file.write(f'\n\nPrint dates with value bigger then given by key: {key}:')
    t = 'Print dates with value bigger then given by key: '
    t += key
    values = GetValuesByKey(data, key)
    vals = filter(lambda x: x["value"] > diff, values)
    for val in vals:
        result_file.write(f'\nValue of key: {key} is {val["value"]} and is more than {diff} on {val["date"]}')
        t += '\nValue of key: '
        t += key
        t += ' is '
        t += str(val["value"])
        t += ' and is more than '
        t += str(diff)
        t += ' on '
        t += val["date"]
    return t


def runSubprocess():
    """ Run Python subprocess """
    print('Run subprocess')
    window = Tk()
    window.title("Lviv Weather Checker by Sofiia Kovalchuk, PMI-44")
    window.geometry('820x450')
    
    lbl = Label(window, text="Get value from data by specific key:")  
    lbl.grid(column=0, row=0)  
    combo = Combobox(window)  
    combo['values'] = ('temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity')  
    combo.grid(column=1, row=0)
    def clicked():
        txt = scrolledtext.ScrolledText(window, width=70, height=4)  
        txt.grid(column=0, row=1)
        with open('.\\result.txt', 'a') as result_file:
            data = GatherAllData(result_file)
            res = GetValueByKey(result_file, data, combo.get())
        txt.insert(INSERT, res)
        
    btn = Button(window, text="Get", command=clicked)  
    btn.grid(column=3, row=0)

    lbl1 = Label(window, text="Get max value from data by specific key:")  
    lbl1.grid(column=0, row=2)  
    combo1 = Combobox(window)  
    combo1['values'] = ('temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity')  
    combo1.grid(column=1, row=2)
    def clicked():
        txt1 = scrolledtext.ScrolledText(window, width=70, height=1)  
        txt1.grid(column=0, row=3)
        with open('.\\result.txt', 'a') as result_file:
            data = GatherAllData(result_file)
            res1 = GetMaxValueByKey(result_file, data, combo1.get())
        txt1.insert(INSERT, res1)
        
    btn1 = Button(window, text="Get", command=clicked)  
    btn1.grid(column=3, row=2)

    lbl2 = Label(window, text="Get average value from data by specific key:")  
    lbl2.grid(column=0, row=4)  
    combo2 = Combobox(window)  
    combo2['values'] = ('temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity')  
    combo2.grid(column=1, row=4)
    def clicked():
        txt2 = scrolledtext.ScrolledText(window, width=70, height=1)  
        txt2.grid(column=0, row=5)
        with open('.\\result.txt', 'a') as result_file:
            data = GatherAllData(result_file)
            res2 = GetValueByKey(result_file, data, combo2.get())
        txt2.insert(INSERT, res2)
        
    btn2 = Button(window, text="Get", command=clicked)  
    btn2.grid(column=3, row=4)

    lbl3 = Label(window, text="Get days with particulat weather condition:")  
    lbl3.grid(column=0, row=6)  
    combo3 = Combobox(window)  
    combo3['values'] = ('Clouds', 'Mist', 'Clear', 'Fog', 'Rainy', 'Snow')  
    combo3.grid(column=1, row=6)
    def clicked():
        txt3 = scrolledtext.ScrolledText(window, width=70, height=1)  
        txt3.grid(column=0, row=7)
        with open('.\\result.txt', 'a') as result_file:
            data = GatherAllData(result_file)
            res3 = GetDaysWithParticulatWeatherCondition(result_file, data, 'main', combo3.get())
        txt3.insert(INSERT, res3)
        
    btn3 = Button(window, text="Get", command=clicked)  
    btn3.grid(column=3, row=6)

    lbl4 = Label(window, text="Get days with value more than: (temperature is in K (C = K - 273.15)")  
    lbl4.grid(column=0, row=8)  
    combo4 = Combobox(window)  
    combo4['values'] = ('temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity')  
    combo4.grid(column=1, row=8)
    spin = Spinbox(window, from_=-350, to=350, width=5)  
    spin.grid(column=2, row=8) 
    def clicked():
        txt4 = scrolledtext.ScrolledText(window, width=70, height=4)  
        txt4.grid(column=0, row=9)
        with open('.\\result.txt', 'a') as result_file:
            data = GatherAllData(result_file)
            res4 = GetDaysWithValueMoreThan(result_file, data, combo4.get(), spin.get())
        txt4.insert(INSERT, res4)
        
    btn4 = Button(window, text="Get", command=clicked)  
    btn4.grid(column=3, row=8)
    
    window.mainloop()
    print('Subprocess ended')
              
def main():
    GetDataFromServer()
    runSubprocess()
    
main()
