##До роботи додаю два файли, які отримала у результаті виконання
##задач 2 та 3

##імпорт необхідних модулів
import http.client, urllib.parse, sys, os
# опрацювання xml-файлів: використати модуль xml.etree.ElementTree
import xml.etree.ElementTree as ET # ET - скорочене позначення

##Задача 1. [ Оберіть для себе тематику, яка вас цікавить ]. В інтернеті знайти за своєю
##тематикою повну url-адресу сервера і веб-сторінки чи файла, розташованої на сервері. Для
##цього можна, наприклад, використати звичайний Internet Explorer, виконавши пошук в
##Internet до отримання кінцевої сторінки веб-сайту (ендпоінт). Internet Explorer показує повну
##url-адресу в рядку зверху вікна відображення сторінки. Цю адресу треба копіювати у свій
##сценарій (кириличні літери доведеться записати вручну). Для веб-серверів загального
##доступу такі адреси зазвичай є постійними.
def task1():
    print("\nЗадача 1. Тематика, яку я обрала - osu, опісля знайшла за цією тематикою  повну url-адресу сервера і веб-сторінки, розташованої на сервері, а саме:")
    anyurl="https://osu.ppy.sh/home/news/2020-10-09-beatmap-spotlights-season-2-autumn-2020"
    servername = "osu.ppy.sh"
    filename = "/home/news/2020-10-09-beatmap-spotlights-season-2-autumn-2020"
    print(anyurl)
    pass # кінець сценарію


##Задача 2. Складіть сценарій веб-клієнта, щоб отримати на свій комп'ютер знайдену вебсторінку
##чи файл. Сценарій веб-клієнта бажано програмувати в режимі try-except, щоб на
##випадок відмови сайту побачити інформацію про вірогідну причину.
##Увага! Не всі веб-сторінки дозволені для копіювання в обхід авторського сайту, спроба
##стороннього запиту на отримання веб-сторінки може бути заблокована. Такі речі треба
##перевіряти експериментально.
##а) може допомогти повторний запуск сценарію, але з паузою 10-15 секунд;
##б) якщо не вдається, знайдіть в інтернеті іншу веб-сторінку.
##Коли сторінка отримана, запустіть її на перегляд способами, розглянутими в темі
##"Деякі методи організації сценаріїїв". Не забувайте, що для запуску перегляду в загальному
##випадку потрібно зазначити повний шлях до файла.
##Текст сценарію (#...) і хід виконання (print()) обов'язково коментувати. Подібні сценарії
##часто дають збій у виконанні, тому треба хоча б побачити трасування виконаної частини
##сценарію.

def task2():
    print("\nЗадача 2. Використовуючи url-адресу із задачі 1, cкладаю сценарій веб-клієнта, щоб отримати на свій комп'ютер знайдену вебсторінку.\nПочаток виконання...")
    anyurl="https://osu.ppy.sh/home/news/2020-10-09-beatmap-spotlights-season-2-autumn-2020"
    servername = "osu.ppy.sh"
    filename = "/home/news/2020-10-09-beatmap-spotlights-season-2-autumn-2020"
    try:
     print("створюємо об'єкт сервера...")
     server = http.client.HTTPSConnection(servername) # створити об'єкт сервера
     print("відправляємо запит...")
     server.request('GET', filename) # відправити запит
     reply = server.getresponse() # отримати відповідь сервера
    except: # можуть бути помилки з'єднання
     info= sys.exc_info() #отримати інформацію про помилку (type,value,traceback)
     print("Помилка HTTPSConnection:\n", info[0], info[1])
     sys.exit() # припинити виконання сценарію
    print("...отримано відповідь...") # відповідь отримана - продовжуємо
    if reply.status == 200:
        # код 200 означає успішне виконання
        with open("osu-news.html","wb") as fsave: # зберегти у файл як потік байтів
            fsave.write(reply.read()) # для "wb"
            reply.close() # закрити з’єднання з сервером
    else:
        print('помилка надсилання запиту: ', reply.status, " ", reply.reason)
        print("...готово")
    # можна запустити файл на перегляд одним з способів, розглянутих раніше:
    print('запуск отриманого файла...')
    os.startfile("osu-news.html")
    print('задача виконана')
    pass

##Задача 3. [ Розшукайте окремим незалежним способом адресу деякого xml-файла ].
##Використовуючи одну з схем доступу до файлів на веб-серверах, складіть сценарій,
##виконайте, отримайте і збережіть на своєму комп'ютері такий xml-файл (файл даних).
##Запустіть його на перегляд, щоб переконатись про отримання і про зміст файла.
def task3():
    print("\nЗадача 3. Pозшукавши окремим незалежним способом адресу деякого xml-файла (https://zaxid.net/resources/xml/iUaRu.xml), cкладаю сценарій веб-клієнта, щоб отримати на свій комп'ютер знайдений файл.\nПочаток виконання...")
    anyurl="https://zaxid.net/resources/xml/iUaRu.xml"
    servername = "zaxid.net"
    filename = "/resources/xml/iUaRu.xml"
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
        with open("zaxid.xml","wb") as fsave: # зберегти у файл як потік байтів
            fsave.write(reply.read()) # для "wb"
            reply.close() # закрити з’єднання з сервером
    else:
        print('помилка надсилання запиту: ', reply.status, " ", reply.reason)
        print("...готово")
    # можна запустити файл на перегляд одним з способів, розглянутих раніше:
    print('запуск отриманого файла...')
    os.startfile("zaxid.xml")
    print('задача виконана')
    pass

##Задача 4. [ Виконайте попередньо вправи на опрацювання xml-файлів, використавши
##наданий файл data.xml і приклад опрацювання цього xml-файла. Доведеться самостійно
##вивчити модуль xml.etree.ElementTree  ].
##Складіть самостійно деяку програму опрацювання свого xml-файла, отриманого в
##задачі 3. Продемонструйте в своїй програмі різні функції і способи опрацювання файла.
##Конкретний обсяг програми для цієї задачі не регламентуємо, це творча робота.

def task4():
    print('\nЗадача 4. Складаю деяку програму опрацювання свого xml-файла, отриманого в задачі 3')
    print('читання даних з xml-файла...')
    # читати дані з xml-файла: текст файла має бути в коді UTF-8
    tree = ET.parse('zaxid.xml') # читати і розділити на окремі елементи
    # кожний елемент дерева має tag і словник атрибутів attrib
    root = tree.getroot() # кореневий елемент (вузол, атрибут)
    #print(root.tag, root.attrib)
    print()
    # дочірні вузли кожного атрибута є ітерованим об'єктом і мають свої атрибути:
    for item in root.iterfind('.'):
        print( 'Вивід кореневого елемента: %s' % item.tag)
    print('')
    # доступ до дочірніх вузлів виконують додатковими індексами,
    # а доступ до словника атрибутів - як у звичайного словника - через ключі
    # пошук потрібних елементів:
    # кожний вузол має метод iter(), який будує ітератор для обходу
    # всіх вузлів заданого імені цілого піддерева даного вузла
    count = 0
    titles = []
    for child_of_root in root.iter('{http://backend.userland.com/rss2}item'):
        for serv in child_of_root.findall('{http://backend.userland.com/rss2}title'):
            titles.append(serv.text)
            #print(serv.text, ":")
    print('Вивід списку останніх новин:')    
    for child_of_root in root.iter('{http://backend.userland.com/rss2}item'):
        count = int(count)
        print(count, '.', end=' ')
        #print(child_of_root.attrib)
        print('Назва новини:', titles[count], ';')
        for serv in child_of_root.findall('{http://backend.userland.com/rss2}enclosure'): # для furn знайти підвузли service
            # для кожного підвузла отримати доступ до його атрибутів
            sa = serv.get("url")
            mn = serv.get("type")
            if sa : print('''       Джерело:''', sa, " ")
            if mn : print('''       Тип файлу джерела:''', mn, " ")
        #print( 'Тег: %sKлючів: %sЕлементів: %sTекст: %sn'%(child_of_root.tag, child_of_root.keys(), child_of_root.items(), child_of_root.text))
        count += 1
    pass

def main():
    task1()
    task2()
    task3()
    task4()
    pass

main()
