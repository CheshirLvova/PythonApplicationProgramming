stations = list()
routes = dict()
variables = list()
constants = dict()
questions = dict()


def is_sublist(ls1, ls2):
    l1 = "".join(ls1)
    l2 = "".join(ls2)
    return l1 in l2


#функція визначення кількості станцій для заданого трамвая
def count_of_stations_for_tram(tram_id):
    answer_is = True
    try:
        stations = list(set([i.strip() for i in routes[tram_id][0] + routes[tram_id][1]]))
    except:
        answer_is = False
    res = list()
    if answer_is:
        res.append(len(stations))
    return (answer_is, res)

#підрахунок маршрутів
def count_of_all_routes():
    res = len(routes)
    return res

#підрахунок різниці у зупинках між заданими станціями
def get_diff_in_stations(start_station, end_station):
    route = howto_get_to_n(start_station, end_station)
    count = 0
    res = list()
    answer_is = len(route) <= 1
    for i in route:
        count += len(i[1])
    if answer_is == False:
        res.append(count - 3)
        res.append(route[1][0])
        res.append(route[0][1][len(route[0][1])-1])
        if is_sublist(route[1][1],routes[route[1][0]][0]):
            res.append(routes[route[1][0]][0][len(routes[route[1][0]][0])-1])
        else:
            res.append(routes[route[1][0]][1][len(routes[route[1][0]][1])-1])
    else:
        res.append(count - 2)
    return (res)


def is_possible_to_get(station_id, tram_id):
    answer_is = station_id in set(routes[tram_id][0] + routes[tram_id][1])
    res = list()
    if answer_is == False:
        for i in routes:
            if station_id in set(routes[i][0] + routes[i][1]):
                res.append(i)
                break
    return (answer_is, res)

def is_possible_to_get_station(start_station, end_station):
    route = howto_get_to_n(start_station, end_station)
    answer_is = len(route) == 1
    res = list()
    if answer_is == False:
        res.append(route[1][0])
        res.append(route[0][1][len(route[0][1])-1])
        if is_sublist(route[1][1], routes[route[1][0]][0]):
            res.append(routes[route[1][0]][0][len(routes[route[1][0]][0])-1])
        else:
            res.append(routes[route[1][0]][1][len(routes[route[1][0]][1])-1])
    return (answer_is, res)

def get_stations_for_tram(tram_id):
    answer_is = True
    res = list()
    tram_id = tram_id.strip()
    try:
        st = list(set(routes[tram_id][0] + routes[tram_id][1]))
    except:
        answer_is = False
    if answer_is:
        res.append(tram_id)
        res.append(st[0] + " <---> " + st[len(st)-1])
        res.append(st)
    return (answer_is, res)


def get_trams_for_station(station):
    res = list()
    answer_is = True
    for i in routes:
        if station in routes[i][0] + routes[i][1]:
            res.append(i)
    if len(res) == 0:
        answer_is = False
    return (answer_is, res)


def get_to_university(start_station):
    end_station = "Головна Пошта"
    (answer_is,lst) = route_btw_stations(start_station, end_station)
    if answer_is:
        lst.append(end_station)
    return (answer_is,lst)


def route_btw_stations(start_station, end_station):
    route = howto_get_to_n(start_station, end_station)
    res = list()
    answer_is = len(route) == 1
    res.append(route[0][0])
    if answer_is:
        if is_sublist(route[0][1], routes[route[0][0]][0]):
            res.append(routes[route[0][0]][0][-1])
        else:
            res.append(routes[route[0][0]][1][-1])
    else:
        res.append(route[1][1][0])
        res.append(route[1][0])
        if is_sublist(route[1][1], routes[route[1][0]][0]):
            res.append(routes[route[1][0]][0][-1])
        else:
            res.append(routes[route[0][0]][1][-1])
        res.append(end_station)
    return (answer_is, res)

def get_route_from_list(direction,start_station,end_station):
    start = listLower(direction).index(start_station.lower())
    end = listLower(direction).index(end_station.lower())
    reverse = False
    if start > end:
        temp = start
        start = end
        end = temp
        reverse = True
    res = direction[start:end+1]
    if reverse:
        res.reverse()
    return res


def howto_get_to_n(start_station,end_station):
    #без жодних пересадок
    for k in routes:
        for direction in routes[k]:
            if start_station.lower() in listLower(direction) and end_station.lower() in listLower(direction):
                return [(k,get_route_from_list(direction, start_station, end_station))]
    #з однією пересадкою
    for t1 in routes:
        direction1 = list()
        known_station = object()
        unknown_station = object()

        for direction in routes[t1]:
            if start_station.lower() in listLower(direction):
                known_station = start_station.lower()
                unknown_station = end_station.lower()
                direction1 = direction
                break
            elif end_station.lower() in listLower(direction):
                known_station = end_station.lower()
                unknown_station = start_station.lower()
                direction1 = direction
                break

        if len(direction1) == 0:
            continue

        for t2 in routes:
            if t1 == t2:
                continue
            for direction2 in routes[t2]:
                if unknown_station in listLower(direction2):
                    common_stations = list(set(direction1) & set(direction2))
                    if len(common_stations) != 0:
                        common_station = common_stations[0]
                        if known_station == start_station:
                            return [(t1,get_route_from_list(direction1, known_station, common_station)), (t2,get_route_from_list(direction2, common_station, unknown_station))]
                        else:
                            return [(t2,get_route_from_list(direction2, unknown_station, common_station)), (t1,get_route_from_list(direction1, common_station, known_station))]
    return list()


actions = [count_of_stations_for_tram, count_of_all_routes, get_diff_in_stations, is_possible_to_get, is_possible_to_get_station, get_stations_for_tram, get_trams_for_station,get_to_university, route_btw_stations]
actions.reverse()

def read_routes(filename):
    ''' key : tram_id
        Value : [forth_direction list, back direction list] '''
    with open(filename, encoding='utf-8', mode='r') as f:
        content = [i.split("#") for i in f.read().split("$")]
        for i in content:
            global routes
            routes[i[0].strip()] = [i[1].strip().splitlines(), i[2].strip().splitlines()]

def read_all_stations(filename):
    with open(filename, encoding='utf-8', mode='r') as f:
        global stations
        stations = f.read().splitlines()
        stations.sort()
        
def read_questions(filename):
    def add_to_dict(dictionary,value,key):
        space = value.find(' ')
        firstWord = value[:space+1]
        if space == -1:
            dictionary[value] = key
        elif firstWord in dictionary.keys():
            add_to_dict(dictionary[firstWord],value[space+1:],key)
        else:
            dictionary[firstWord] = dict()
            add_to_dict(dictionary[firstWord],value[space+1:],key)

    def remove_solo(key,dictionary):
        if '+' in dictionary.keys() and '-' in dictionary.keys():
            return (key,dictionary)
        res = dict()
        if len(dictionary.keys()) == 1:
            if list(dictionary.keys())[0].startswith('$'):
                (tk,dc) = remove_solo('',list(dictionary.values())[0])
                return  (key,{list(dictionary.keys())[0]:{tk:dc}})
            return remove_solo(key.strip() + " " + list(dictionary.keys())[0],list(dictionary.values())[0])
        else:
            for k in dictionary.keys():
                (tk,dc) = remove_solo(k,dictionary[k])
                res[tk] = dc
            return (key,res)

    temp = dict()
    with open(filename,'r',encoding = 'UTF-8') as questionsFile:
        for line in questionsFile.readlines():
            qa = line.split('->')
            question = qa[0].strip()
            answers = qa[1].split('&')
            answers = {"+" : answers[0],"-" : answers[1], 'func' : actions.pop()}
            add_to_dict(temp,question,answers)
    global questions
    questions = remove_solo('',temp)[1]

def do_all_preparations():
    read_routes("all_trams_way.txt")
    read_all_stations("all_stops.txt")
    read_questions("QandA.txt")
    constants['$tram_id'] = routes.keys()
    constants['$station_id'] = stations


def listLower(lst):
    return [x.lower() for x in lst]

def navigate_user(dictionary,string,prev):
    found = False
    if list(dictionary.keys())[0].startswith('$'):
        key = list(dictionary.keys())[0].strip()
        if string.strip() == '':
            if '?' in key:
                print(prev + key.replace('$',''))
            else:
                print(prev + key.replace('$','') + ' ...')
            print('Можливі значення '+key.replace('$','').replace('?','') + ':')
            print('\t'.join(constants[key.replace('?','')]))
            return (False,{})
        global variables
        toFind = string.replace('?','').strip()
        if toFind.startswith('"'):
            toFind = toFind[toFind.find('"'):]
            toFind = toFind[:toFind[1:].find('"')+2]
        else:
            toFind = toFind.split(' ')[0]
        if toFind.lower().strip().replace('"','') in [x.lower().strip() for x in constants[key.replace('?','')]]:
            variables.append(toFind.replace('"',''))
            if '?' in key:
                return (True,list(dictionary.values())[0])
            return navigate_user(list(dictionary.values())[0],string[string.find(toFind)+len(toFind):],prev + toFind.strip()+' ')
        else:
            print('Не вдалося знайти {} {}'.format(key.replace('$','').replace('?',''),toFind))
            print('Можливі значення '+key.replace('$','').replace('?','') + ':')
            print('\t'.join(constants[key.replace('?','')]))
            return (False,{})

    if string.strip() != '':
        for k in dictionary.keys():
            if k.lower().strip().startswith(string.lower().strip()) or string.lower().strip().startswith(k.lower().strip()):
                found = True
                if k.endswith('?'):
                    return (True,dictionary[k])
                else:
                    return navigate_user(dictionary[k],string[len(k):],prev + k)

    if not found:
        for word in string.split(' '):
            found_two = False
            for k in dictionary.keys():
                if word.lower() in k.lower():
                    found_two = True
            if not found_two:
                print("Незрозуміле застосунку/неправильно записане слово: " + word)
        for k in dictionary.keys():
            if k.endswith('?'):
                print(prev + k)
            else:
                print(prev + k + '...')
    return (False,{})

def give_result(answer,dictionary):
    if answer[0]:
        print(dictionary['+'].format(*answer[1]))
    else:
        print(dictionary['-'].format(*answer[1]))

do_all_preparations()

print('''Вас вітає інформаційно-довідкова система про пересування містом трамваями у Львові!
Для початку роботи у системі ви можете натиснути клавішу Enter та побачите перелік
можливих початків постановки ваших запитань. Або ж ви можете ввести своє запитання
/ просто його початок (система вважає питання сформульованим остаточно,
якщо наприкінці речення ви поставили знак питання, якщо ви введете речення не повністю, програма
автоматично запропонує варіанти продовження). Також слід зауважити, що назви зупинок, які ви вводитимете,
потрібно записувати у подвійних лапках (наприклад, "вул. Русових"): ''')
while(True):
    variables = list()
    print()
    (questionFull,handler) = navigate_user(questions,input(),'')
    if questionFull:
        if '' in handler.keys():
            handler = handler['']
        give_result(handler['func'](*variables),handler)
