#підключення модулів
import urllib.request
# дані, отримані модулем urllib, завжди повертають як рядки байтів
import http.client, urllib.parse, sys, os, subprocess
import json # використаємо модуль json
from pprint import pprint # "гарний" друк


##Завдання 1. [ Оберіть для себе тематику, яка вас цікавить – не обов'язково лише в
##навчанні. Можливо, це вже трапилось на попередній темі  ].
##В інтернеті знайти за своєю  тематикою повну url-адресу сервера і файла формата
##JSON, розташованого на сервері. Використовуючи одну з схем доступу до файлів на вебсерверах (розглядали раніше), складіть сценарій, виконайте, отримайте json-файл і збережіть
##на своєму комп'ютері.

def task1():
    print("\nЗадача 1. Pозшукавши окремим незалежним способом адресу деякого json-файла (https://data.nasa.gov/api/views/yvxp-ccvk/rows.json), cкладаю сценарій веб-клієнта, щоб отримати на свій комп'ютер знайдений файл.\nПочаток виконання...")
    anyurl="https://data.nasa.gov/api/views/yvxp-ccvk/rows.json"
    servername = "data.nasa.gov"
    filename = "/api/views/yvxp-ccvk/rows.json"
    try:
     print("створюємо об'єкт сервера...")
     server = http.client.HTTPSConnection(servername) # створити об'єкт сервера
     print("відправляємо запит...")
     server.request('GET', filename) # відправити запит
     reply = server.getresponse() # отримати відповідь сервера
    except: # можуть бути помилки з'єднання
     info= sys.exc_info() #отримати інформацію про помилку (type,value,traceback)
     print("помилка HTTPSConnection:\n", info[0], info[1])
     sys.exit() # припинити виконання сценарію
    print("...отримано відповідь...") # відповідь отримана - продовжуємо
    if reply.status == 200:
        # код 200 означає успішне виконання
        with open("SxSW2016Leads.json","wb") as fsave: # зберегти у файл як потік байтів
            fsave.write(reply.read()) # для "wb"
            reply.close() # закрити з’єднання з сервером
        print('задача успішно виконана')
    else:
        print('помилка надсилання запиту: ', reply.status, " ", reply.reason)
        print("...не готово")
    pass

##Завдання 2. Запустіть отриманий json-файл на перегляд, щоб переконатись про зміст
##файла. Перегляд виконати з сценарію python способами, викладеними в "Формат даних
##JSON.pdf": 1) як звичайний текстовий файл; 2) як роздрук внутрішнього зображення python.
##Це завдання для самоконтролю.

def task2():
    print("\nЗадача 2. Запускаю отриманий json-файл на перегляд, щоб переконатись про зміст файла. Перегляд виконуватиму з сценарію python способами, викладеними в файл з довідковим матеріалом. \nПочаток виконання...")
    ##Щоб переглянути дані формату JSON з сценарію python, можна використати дві
    ##можливості.
    ##1) безпосередньо переглянути сам файл, запустивши на виконання дочірній процес:    
    destfile = "SxSW2016Leads.json"
    dirname = os.path.abspath('.') # шлях від кореня до поточної папки
    filename = os.path.join(dirname, destfile)
    print('Перегляд файлу за допомогою запуску дочірного процесу...\n')
    parprog = subprocess.Popen(["notepad.exe", filename])
    ##2) перетворити json-файл у внутрішнє зображення і надрукувати у вікні виконання:
    # module provides a capability to "pretty-print" arbitrary Python
    # data structures in a form which can be used
    # as input to the interpreter
    print('Друк у вікні виконання перетвореного json-файлу у внутрішнє зображення...\n')
    with open(destfile) as data_file:
     data = json.load(data_file)
    pprint(data)
    print('Задача успішно виконана\n')
    
    pass

##Завдання 3. Виконати програмне дослідження python-структури документа (тобто
##json-файла в зображенні об'єкта python – десеріалізованому). Приклад дослідження є в
##файлах матеріалів.
##Увага! Алгоритм програмного дослідження, вибір операторів python і функцій тощо,
##повністю залежать від будови файла формата json. Складати python-програму дослідження
##треба окремими кроками, співставлячи після кожного кроку надруковані результати і
##json-файл в форматі звичайного текста. Примітка від авторки коду: Оскільки файл,
##що був знайдений мною попередньо, мав велику кількість даних, для програмного
##дослідження я обрала менший, створений попередньо мною файл для ясності надрукованих
##команд.

def task3():
    print('\nЗадача 3. Виконую програмне дослідження python-структури документа...')
    destfile = "Presents.json"
    with open(destfile) as data_file:
     data = json.load(data_file)
    print("Тип цілого документа: ", type(data).__name__)
    print("Документ має ", len(data), "елементів")
    print("Тип кожного елемента як цілого:", *[type(ob).__name__ for ob in data])
    print("\nТипи значень окремих елементів документа за ключами:", *[type(data[ob]).__name__ for ob in data.keys()])
    print("\nТип елемента 't-shirt':", type(data["t-shirt"]).__name__)
    print("\nЗначення цілого елемента 'music-card':\n", data["music-card"])
    print("\nПоелементний перелік частин 'music-box':")
    print(*[ subvalue for subvalue in data["music-box"] ], sep="\n")
    print(*[ subvalue for subvalue in data["music-box"].items() ],sep="\n")
    print("\nСписок значень окремих елементів документа:", *[str(ob) + " : " + str(data[ob]) for ob in data.keys()],sep="\n\n")
    pass

##Завдання 4. Складіть власні умови двох різних задач аналізу отриманого json-файла.
##Можна скористатись зразками, які є в файлі "Формат даних JSON.pdf". Умови задач залежать
##від змісту отриманого json-файла, тому це є самостійною роботою.

def task4():
    print('\nЗадача 4. Виконую власні умови дo двох різних задач аналізу отриманого json-файла...')
    destfile = "Presents.json"
    with open(destfile) as data_file:
     data = json.load(data_file)
    ##Виконання задачі 1
    print('\n --- Задача 1. Друк списку назв товарів і цін ------')
    key1 = data.keys() # отримати всі ключі першого рангу
    #print(list(key1)) # контрошль списку ключів першого рангу
    for k in key1: # перевірка за кожним ключем
        if isinstance(data[k], dict): # чи значення є словником
            key2 = data[k].keys() # ключі внутрішнього словника
            #print(list(key2)) # контроль списків внутрішніх ключів
            if 'name' in key2 and 'price' in key2: # чи є потрібні дані
                print("{0:10}{1}".format(data[k]['name'], data[k]['price']))
    ##Виконання задачі 2
    print("\n --- Задача 2. Показати список постачальників продукції в магазин -----")
    key1 = data.keys() # ключі першого рангу
    for k in key1: # перевірка за кожним ключем
        if isinstance(data[k], dict): # чи значення є словником
            key2 = data[k].keys() # ключі внутрішнього словника
            if 'name' in key2 and 'production' in key2 :
                # якщо є дані про постачальника
                print("{0:10}, розроблена компанією/виробництвом: {1}".format(data[k]['name'], data[k]['production']))
    pass

def main():
    task1()
    task2()
    task3()
    task4()
    pass

main()

