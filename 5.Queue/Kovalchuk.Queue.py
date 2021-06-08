#РЕАЛІЗАЦІЯ ЧЕРГИ НА ОСНОВІ СПИСКУ LIST
class Queue:
    # початок черги - в кінці ist праворуч, кінець - на початку list
    # ----------- "стандартні" функції черги -------------------
    def __init__(self):     # спочатку черга завжди порожня
        self.queue = []

    def __str__(self):      # список елементів черги - для контролю
        return "<back> [" + ",\n".join(map(str, self.queue)) + "] <front>"

    def push(self, obj):    # записати в чергу в кінець
        self.queue.insert(0, obj)
        return self         # для кратних записів

    def pop(self):         # прочитати елемент з черги
        if self.queue : return self.queue.pop()
        else : return None  # якщо черга порожня

    def len(self):          #кількість елементів у черзі
        return len(self.queue)

    def front(self):        # перший елемент черги
        if self.queue : return self.queue[len(self.queue) - 1]
        else : return None

    def back(self):         # останній елемент черги
        if self.queue : return self.queue[0]
        else : return None

    def empty(self):        # перевірити, чи черга порожня
        return not self.queue

    def clear(self):        # очистити чергу (якщо порібна та сама ще один раз)
        self.queue = []

    # -------------- додаткові функції черги ------------------
    def find(self, key, value):
        index_list = [self.queue[i] for i in range(len(self.queue))
                     if (self.queue[i][key]==value)]
        return index_list
        

    def remove(self, k):    #викреслити і повернути елемент в позиції k
        if 0 <= k <len(self.queue):
            y = self.queue[k]; del self.queue[k : k+1]; return y
        else: return None   # елемента за таким номером немає

    def all(self):          # повернути список цілої черги
        return self.queue

#клас машин-перевізників для визначення основних функцій
class cars:
    def __init__(self):
        self.green_сoridor = Queue()
        self.general_сoridor = Queue()
        self.goods = list()

    #Функції для різних переміщень машин у чергах.
    def put_avto_in_general(self,avto): #додаємо машину в загальну чергу
        self.general_сoridor.push(avto)
        print("Авто {} було додано в загальний коридор".format(avto))
        
    def put_avto_in_green(self): #переміщаємо машину до зеленого коридору
        avto = self.general_сoridor.pop()
        self.green_сoridor.push(avto)
        print("Авто {} було додано в зелений коридор".format(avto))
        
    def move_from_green_to_general(self):
        avto = self.green_сoridor.pop()
        self.general_сoridor.push(avto)
        print("Авто {} було переміщено в загальний коридор".format(avto))
        
    def move_from_general_to_green(self):
        avto = self.general_сoridor.pop()
        self.green_сoridor.push(avto)
        print("Авто {} було переміщено в зелений коридор".format(avto))
        
    #Функції для заборони в'їзду машині.
    def denied_on_general(self): #забороняємо в'їзд машині на загальному коридорі
        avto = self.general_сoridor.pop()
        print("Для авто {} було заборонено в'їзд на загальному коридорі".format(avto))
    def denied_on_green(self): #забороняємо в'їзд машині на зеленому коридорі
        avto = self.green_сoridor.pop()
        print("Для авто {} було заборонено в'їзд на зеленому коридорі".format(avto))
        
    #Функції для дозволу в'їзду машині.
    def allow_on_green(self): #дозволяємо в'їзд машині на зеленому коридорі
        car = self.green_сoridor.pop()
        good = {}; good['товар'] = car['товар']; good['ціна'] = car['ціна']; self.goods.append(good)
        print("Для авто {} було дозволено в'їзд на зеленому коридорі".format(car))
    def allow_on_general(self): #дозволяємо в'їзд машині на червоному коридорі
        car = self.general_сoridor.pop()
        good = {}; good['товар'] = car['товар']; good['ціна'] = car['ціна']; self.goods.append(good)
        print("Для авто {} було дозволено в'їзд на загальному коридорі".format(car))

    #Функція для отрмання декларацій з машинами, що везуть певний товар
    def get_avto_by_goods(self, item):
        position = self.general_сoridor.find('товар', item)
        for declaration in position:
            print("Mашини, що везуть товар'{}':\n {}.".format(item, declaration))
    
    #Функція для отримання декларацій з машинами, що прямують до конкретного міста
    def avtos_to_city(self, city):
        position = self.general_сoridor.find('куди', city)
        for avtos in position:
            print("Машини, що прямують до '{}': \n {}.".format(city, avtos))
        
    #Функція для отримання усіх товарів, що перетнули митницю
    def get_goods_which_was_passed(self):
        print("Товари, які пройшли перевірку:")
        for x in self.goods:
            print("Найменування товару:{}, ціна товару: {}.".format(x['товар'],
                    x['ціна'] ))
    #Функція для отримання сумарної вартості товарів, що перетнули митницю
    def maximum_price_of_goods(self):
        sum_of_goods = 0
        for x in self.goods:
            sum_of_goods += x["ціна"]
        print("Загальна вартість товарів, які пройшли перевірку: {}.".format(sum_of_goods))
        
    
    # ------------------------------------------------------

    
def main():
    ## Частина 1. Побудувати шаблон митної декларації:
    ## avtonn = { авто : марка, номер_авто : номер, власник_авто : компанія,
    ## дата : рік-місяць-день,
    ## звідки : (країна,місто), куди : (країна,місто),
    ## товари : [ перелік_товарів – (назва,вартість) ],
    ## договір_перевезення : є / нема
    ## }


    ## Частина 2. Побудувати окремо список митних декларацій авто, які мають прибути до
    ## кордону (є в дорозі) і пройти митний контороль.

    # список містить перелік ключів шаблона
    listkey = ['авто', 'номер_авто', 'власник_авто', 'дата', 'звідки', 'куди', 'товар', 'ціна', 'договір_перевезення']
    # списки зі значеннями для авто
    data1 = ['Volvo',  'D1456AH', 'Green day company', '2020.10.12', 'Wroclaw', 'Вінниця', 'горіхи', 3000, 'нема']
    data2 = ['BMW',  'D1093AH', 'Green day company', '2020.10.12', 'Warszawa', 'Одеса', 'курага', 1000, 'є']
    data3 = ['Audi',  'ЛВ2536ЛК', 'Nestle-Україна', '2020.09.12', 'Львів', 'Gdańsk', 'батончики "Fitness"', 15000, 'є']
    data4 = ['Mercedes-Benz',  'ЖІ5889ЖТ', 'Green day company', '2020.10.12', 'Львів', 'Rzeszów', 'батончики "Nesquik"', 10000, 'є']
    data5 = ['Lada',  'DH1257AH', 'Green day company', '2020.10.12', 'Wroclaw', 'Одеса', 'какао "Nesquik"', 5000, 'нема']
    
    # декларації для авто
    avto1 = dict(zip(listkey, data1))
    avto2 = dict(zip(listkey, data2))
    avto3 = dict(zip(listkey, data3))
    avto4 = dict(zip(listkey, data4))
    avto5 = dict(zip(listkey, data5))
    
    ## Частина 3. Будемо використовувати дві черги: загальна, зелений коридор. З кожною
    ## чергою можна виконати операції відповідно до функцій програмного класу черги.
    avtos = cars()
    
    ## Частина 4. Операції митного контролю. [ Програмні операції з чергою ]
    ##  поставити авто в чергу для огляду; (одну або другу)
    avtos.put_avto_in_general(avto1)
    avtos.put_avto_in_general(avto2)
    avtos.put_avto_in_general(avto3)
    avtos.put_avto_in_general(avto4)
    avtos.put_avto_in_general(avto5)

    ##  скласти перелік авто (місце в черзі), які везуть вказаний товар;
    avtos.get_avto_by_goods('какао "Nesquik"')
    
    ##  які авто прямують до Одеси?
    avtos.avtos_to_city('Одеса')
    
    ##  перевести авто з однієї черги в кінець другої; (якщо немає потреби в детальному огляді, або навпаки);
    avtos.put_avto_in_green()
    avtos.put_avto_in_green()
    
    ##  закінчити огляд і дозволити перетин кордону – читати з черги;
    avtos.allow_on_general()
    avtos.allow_on_general()
    avtos.allow_on_green()

    ##  викреслити авто з черги (немає дозволу на перетин кордону);
    avtos.denied_on_green()
    avtos.denied_on_general()
    
    ##  таблиця товарів і цін, перевезених через кордон (підсумок);
    avtos.get_goods_which_was_passed()
    avtos.maximum_price_of_goods()
    

main()
