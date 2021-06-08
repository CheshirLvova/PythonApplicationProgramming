##############################################################################
##Задача 1
print('Задача 1\n')
##На клавіатурі друкують по черзі в стовпчик цілі числа різних знаків. Послідовність
##чисел закінчується нулем, наприклад:3  28  -4  901  666  -25  -25  700  -1  0
##Обчислити:  1) кількість додатніх чисел; 2) кількість від’ємних чисел;
##3) середнє арифметичне від’ємних.

def checkCounts(list):
    positivecount = 0
    negativecount = 0
    negativesum = 0
    for i in list:
        if i > 0:
            positivecount +=1
        if i < 0:
            negativecount += 1
            negativesum += i
    print(list)
    print('кількість додатніх чисел =', positivecount,'кількість від’ємних чисел =', negativecount, 'середнє арифметичне від’ємних =', (negativesum/negativecount))
    pass

    #tests
##a = []
##number = 1
##while number != 0:
##    number = int(input())
##    a.append(number)
##checkCounts(a)        ##у випадку друку по черзі у стовпчик

testList = [3, 28, -4, 901, 666, -25, -25, 700, -1, 0]
checkCounts(testList)
    
##############################################################################
##Задача 2
print('\nЗадача 2\n')
##  Задано два цілі додатні числа a, b. Знайти їх найбільший
## спільний дільник, використовуючи алгоритм Евкліда неоптимізований.

def EuklidAlgo( a, b):
    print('Для заданих чисел', a, 'і', b)
    while a != b:
        if a > b: a = a - b
        else: b = b - a
    print('НСД = ', a)
    pass

##a = int(input('перше число = '))
##b = int(input('друге число = '))
##EuklidAlgo(a, b)

    #tests
EuklidAlgo(36, 8)
EuklidAlgo(22, 8)
EuklidAlgo(4, 2)

##############################################################################
##Задача 3
print('\nЗадача 3\n')
##  Скільки разів в заданому рядку зустрічається буква  ‘а’  українська.

def UkrACounter( text):
    count = 0
    count = int(count)
    message = text
    for character in message:
        if character == "а":
            count += 1
    print(message)
    print('Українська літера а зустрічається у заданому рядку', count, 'разів.')
    pass

    #tests
UkrACounter("Горіла сосна, палала")
UkrACounter("Horila sosna, palala")

##############################################################################
##Задача 4
print('\nЗадача 4\n')
## Задане речення поділити на слова і надрукувати їх в стовпчик.
def CutSentence(sentence):
    words = sentence.split(' ')
    for i in words:
        print(i)
    pass

    #tests
CutSentence('Ре́чення — граматична конструкція, побудована з одного чи кількох слів певної мови, що становить окрему, відносно незалежну думку.')
    
input()
