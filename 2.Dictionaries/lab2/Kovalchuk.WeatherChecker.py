##функція, що здійснює читання файлу по рядках
def read_file():
    with open('weather.txt', 'r') as file:
        lines = file.readlines()
        return lines
        #print(lines)

##функція, що створює список словників з усіма вхідними даними програми 
def file_to_list(lines):
    list_of_dicts = []
    for l in lines:
        data = l.split('|')
        all_weather = dict(zip(['city', 'date', 'time', 'weather_condition', 'temperature', 'pressure', 'wind'], data))
        list_of_dicts.append(all_weather)
    return list_of_dicts

##функція, що здійснює запис до файлу
def to_file(data):
    with open('results.txt', 'a') as file:
        file.writelines(str(data))
        
##1. Прогноз погоди у вашому місті (до 7 днів через малу кількість вхідних даних);
def show_weather_for_date(all_weather, city, date):
    city_data_for_date = []
    for i in all_weather:
        if i['city'] == city and i['date'] == date:
            city_data_for_date.append(i)
    print('1. Погода у місті ', city, ' на ', date, ':\n')
    to_file('1. Погода у місті ' + city + ' на ' + date + ':\n\n')
    if(len(city_data_for_date) == 0):
        print('От, халепа! Немає даних для відображення! База даних поступово зростатиме. Спробуйте ввести іншу дату')
        to_file('От, халепа! Немає даних для відображення! База даних поступово зростатиме. Спробуйте ввести іншу дату')
    for i in city_data_for_date:
        print(' Час: ' + i['time'] + ', погодні умови: ' + i['weather_condition'] + ', температура: ' + i['temperature'] + ', атмосферний тиск: ' + i['pressure'] + ', вітер: ' + i['wind'] + '\n')
        to_file('   Час: ' + i['time'] + ', погодні умови: ' + i['weather_condition'] + ', температура: ' + i['temperature'] + ', атмосферний тиск: ' + i['pressure'] + ', вітер: ' + i['wind'] + '\n')
    return city_data_for_date

##  2. Відображення метеоданих вашого міста;
def weather_of_the_city(all_weather, city):
    city_data = []
    for i in all_weather:
        if i['city'] == city:
            city_data.append(i)

    print('2. Відображення метеоданих міста ', city, ':\n')
    to_file('2. Відображення метеоданих міста ' + city + ':\n\n')
    if(len(city_data) == 0):
        print('От, халепа! Немає даних для відображення! База даних поступово зростатиме. Спробуйте ввести іншу дату')
        to_file('От, халепа! Немає даних для відображення! База даних поступово зростатиме. Спробуйте ввести іншу дату')
    for i in city_data:
        print(' Дата: ' + i['date'] + ', час: ' + i['time'] + ', погодні умови: ' + i['weather_condition'] + ', температура: ' + i['temperature'] + ', атмосферний тиск: ' + i['pressure'] + ', вітер: ' + i['wind'] + '\n')
        to_file('   Дата: ' + i['date'] + ', час: ' + i['time'] + ', погодні умови: ' + i['weather_condition'] + ', температура: ' + i['temperature'] + ', атмосферний тиск: ' + i['pressure'] + ', вітер: ' + i['wind'] + '\n')
    return city_data

##  3. Пошук максимальної температури у заданому місті;
def max_temperature_of_day(all_weather, date):
    list_of_temperature = []
    for i in all_weather:
        if i['date'] == date:
            list_of_temperature.append(int(i['temperature']))

    res = max(list_of_temperature)
    ct = ''
    for i in all_weather:
        if int(i['temperature']) == int(res):
            ct =str(i['city'] + ' ')
    print('3. Максимальна температура ' + date + ' становить ' + str(res) + '°C у місті ' + ct + '.\n')
    to_file('3. Максимальна температура ' + date + ' становить ' + str(res) + '°C у місті ' + ct + '.\n')
    if(len(list_of_temperature) == 0):
        print('От, халепа! Немає даних для відображення! База даних поступово зростатиме. Спробуйте ввести іншу дату')
        to_file('От, халепа! Немає даних для відображення! База даних поступово зростатиме. Спробуйте ввести іншу дату')
    return res

##  4. Пошук мінімальної температури у заданому місті;
def min_temperature_of_day(all_weather, date):
    list_of_temperature = []
    for i in all_weather:
        if i['date'] == date:
            list_of_temperature.append(int(i['temperature']))

    res = min(list_of_temperature)
    ct = ''
    for i in all_weather:
        if int(i['temperature']) == int(res):
            ct =str(i['city'] + ' ')
    print('4. Мінімальна температура ' + date + ' становить ' + str(res) + '°C у місті ' + ct + '.\n')
    to_file('4. Мінімальна температура ' + date + ' становить ' + str(res) + '°C у місті ' + ct + '.\n')
    if(len(list_of_temperature) == 0):
        print('От, халепа! Немає даних для відображення! База даних поступово зростатиме. Спробуйте ввести іншу дату')
    return res

##5. Визначити динаміку зміни температури в зазначеному місті протягом дня;
def temperature_amplitude_for_date(all_weather, city, date):
    city_data_for_date = []
    for i in all_weather:
        if i['city'] == city and i['date'] == date:
            city_data_for_date.append(int(i['temperature']))
            
    res = max(city_data_for_date) - min(city_data_for_date)
    ct = ''
    for i in all_weather:
        if int(i['temperature']) == int(res):
            ct +=str(i['city'] + ' ')
    print('5. Амплітуда коливань температури ' + date + ' становить ' + str(res) + '°C у місті ' + city + '.\n')
    to_file('5. Амплітуда коливань температури ' + date + ' становить ' + str(res) + '°C у місті ' + city + '.\n')
    if(len(city_data_for_date) == 0):
        print('От, халепа! Немає даних для відображення! База даних поступово зростатиме. Спробуйте ввести іншу дату')
        to_file('От, халепа! Немає даних для відображення! База даних поступово зростатиме. Спробуйте ввести іншу дату')
    return res

##  6. Відобразити метеорологічні дані в містах, де температура менша від t°C – тобто, де настало похолодання;
def lower_temperature_than_t(all_weather, temperature):
    list_of_temperatures = []
    for i in all_weather:
        if int(temperature) > int(i['temperature']):
            list_of_temperatures.append(int(i['temperature']))
    if(len(list_of_temperatures) == 0):
        print('От, халепа! Немає даних для відображення! База даних поступово зростатиме. Спробуйте ввести іншу температуру')
        to_file('От, халепа! Немає даних для відображення! База даних поступово зростатиме. Спробуйте ввести іншу температуру')
    else: 
        print('6. Відображення метеоданих в містах, де температура менша від ', temperature, '°C:\n')
        to_file('6. Відображення метеоданих в містах, де температура менша від ', temperature, '°C:\n\n')
    
        for i in list_of_temperatures:
            print(' Місто: ' + i['city'] + ', дата: ' + i['date'] + ', час: ' + i['time'] + ', погодні умови: ' + i['weather_condition'] + ', температура: ' + i['temperature'] + ', атмосферний тиск: ' + i['pressure'] + ', вітер: ' + i['wind'] + '\n')
            to_file('   Місто: ' + i['city'] + ', дата: ' + i['date'] + ', час: ' + i['time'] + ', погодні умови: ' + i['weather_condition'] + ', температура: ' + i['temperature'] + ', атмосферний тиск: ' + i['pressure'] + ', вітер: ' + i['wind'] + '\n')
    return list_of_temperatures

def main():
    lines = read_file()
    all_weather = file_to_list(lines)
    print('''
Вас вітає програма з прогнозом погоди по всіх куточках України,
а також погодним архівом для відображення статистики даних по певним критеріям.

Слід зазначити, що всі результати, які ви бачитимете на екрані, записуватимуться до файлу з результатами для запобіганню втрати даних.

Надалі ви можете користуватися пунктами меню для знаходження необхідної інформації
''')
    
    while(True):
        task = int(input('''(для взаємодії з програмою достатньо натиснути відповідну цифру пункту меню та виконати подальші інструкції):

1. Прогноз погоди у вашому місті (до 7 днів);
2. Відображення метеоданих вашого міста;
3. Пошук максимальної температури у заданому місті;
4. Пошук мінімальної температури у заданому місті;
5. Визначити динаміку зміни температури в зазначеному місті протягом дня;
6. Відобразити метеорологічні дані в містах, де температура менша від t°C – тобто, де настало похолодання;
7. Завершити роботу;
        '''))
        if(task == 1):
            city = input('Введіть місто з вказаного переліку у заданому форматі (З великої літери, без пропусків): Львів, Київ, Тернопіль: ')
            date = input('Введіть дату у форматі дд.мм.рік (наприклад, 01.10.2020): ')
            show_weather_for_date(all_weather, city, date)
        elif(task == 2):
            city = input('Введіть місто з вказаного переліку у заданому форматі (З великої літери, без пропусків): Львів, Київ, Тернопіль: ')
            weather_of_the_city(all_weather, city)
        elif(task == 3):
            date = input('Введіть дату у форматі дд.мм.рік (наприклад, 01.10.2020): ')
            max_temperature_of_day(all_weather, date)
        elif(task == 4):
            date = input('Введіть дату у форматі дд.мм.рік (наприклад, 01.10.2020): ')
            min_temperature_of_day(all_weather, date)
        if(task == 5):
            city = input('Введіть місто з вказаного переліку у заданому форматі (З великої літери, без пропусків): Львів, Київ, Тернопіль: ')
            date = input('Введіть дату у форматі дд.мм.рік (наприклад, 01.10.2020): ')
            temperature_amplitude_for_date(all_weather, city, date)
        elif(task == 6):
            temperature = input('Введіть температуру (цілочисловим значенням)): ')
            lower_temperature_than_t(all_weather, temperature)
        elif(task == 7):
            print('Гарного дня!')
            break
main()
    
