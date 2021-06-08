class Stack:
    def __init__ (self):            #спочатку стек завжди порожній
        self.stack = []

    def __str__ (self):             #список елементів стеку для контролю
        return "<bottom> [" + ",".join(map(str, self.stack)) + "] <top>"

    def push(self, obj):            #запис у стек
        self.stack.append(obj)
        return self                 #для коротких записів

    def pop(self):                  #читати з вершини
        if self.stack : return self.stack.pop()
        else: return None           #якщо стек порожній
        
    def empty(self):                #перевірка, чи стек порожній
        return not self.stack

    def len(self):                  #кількість елементів у стеку
        return len(self.stack)

    def peek(self):
         return self.stack[len(self.stack)-1]

    def clear(self):                #очистити стек (якщо потрібно, той самий)
        self.stack = []

##-------------Задача 2 (Для програмістів-математиків)--------------------------
##В текстовому файлі чи в текстовому рядку записана формула, яка б мала відповідати таким правилам:
##формула ::= терм ( ( + | - ) терм )*
##терм ::= ( x | y | z ) | "(" формула ")" | "[" формула "]" | "{" формула "}"
##Наприклад: (правильно)
##x + ( y – z – [ x + x ] + { [ z – z – y ] + ( y ) } ) - z
##Перевірити, чи відповідає правилам запис формули.
##Підказка (варіант). Це є ідея обчислення виразів за допомогою стека. Перший
##операнд записуємо в стек. Знак операції запам'ятовуємо – якщо є. Обчисливши другий
##операнд (або без обчислення, якщо другого немає), вибираємо з стека останній
##обчислений. Операндами можуть бути як величини x,y,z, так і дужки. Всі операнди x,y,z
##в процесі перевірки можна позначати однаково, наприклад, F. Результатом кожного
##кроку перевірки має бути відповідність: F↔F, F, (↔), [↔], {↔}.



def check_for_brackets(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString)-1 and balanced:
        symbol = symbolString[index]
        nextsymbol = symbolString[index+1]
        if symbol == "(":
            s.push(symbol)
        elif symbol == "(" and nextsymbol == ")":
            return False
        else:
            if symbol == ")":
                s.pop()

        index = index + 1

    if balanced and s.empty():
        return True
    else:
        return False

def check_for_sq_brackets(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString)-1 and balanced:
        symbol = symbolString[index]
        nextsymbol = symbolString[index+1]
        if symbol == "[":
            s.push(symbol)
        elif symbol == "[" and nextsymbol == "]":
            return False
        else:
            if symbol == "]":
                s.pop()

        index = index + 1

    if balanced and s.empty():
        return True
    else:
        return False

def check_for_curly_brackets(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString)-1 and balanced:
        symbol = symbolString[index]
        nextsymbol = symbolString[index+1]
        if symbol == "{":
            s.push(symbol)
        elif symbol == "{" and nextsymbol == "}":
            return False
        else:
            if symbol == "}":
                s.pop()

        index = index + 1
    if balanced and s.empty():
        return True
    else:
        return False

def check_for_operator(symbolString):
    s = Stack()
    balanced = True
    index = 0
    if symbolString[len(symbolString)-1] == "+" or symbolString[len(symbolString)-1] == "-":
        return False
    else:
        while index < len(symbolString)-2 and balanced:
            symbol = symbolString[index]
            next_symbol = symbolString[index+2]
            if (symbol == "+" or symbol == "-") and (next_symbol == "+" or next_symbol == "-" or next_symbol == ")" or next_symbol == "]" or next_symbol == "}"):
                balanced = False
            index = index + 1
        if balanced:
            return True
        else:
            return False
def check_for_symbols(symbolString):
    s = Stack()
    index = 0
    while index < len(symbolString):
        symbol = symbolString[index]
        if symbol in "xyz+-()[]{} ":
            s.push(symbol)
            s.pop()
        else:
            s.push(symbol) 
        index = index + 1
    if s.empty():
        return True
    else:
        return False
    
def formula_checker(symbolString):
    check = check_for_brackets(symbolString) and check_for_sq_brackets(symbolString) and check_for_curly_brackets(symbolString) and check_for_operator(symbolString) and check_for_symbols(symbolString)
    if check:
        return "Запис формули відповідає правилам"
    else:
        return "Запис формули не відповідає правилам"
     
def main():
    #тестування 2 завдання
    #Запис формули відповідає правилам
    print("Тест 1\nВхідні дані: x\nРезультат: ", formula_checker('x'))
    #Запис формули не відповідає правилам: додавання порожніх дужок
    print("\nТест 2\nВхідні дані: x + ()\nРезультат: ", formula_checker('x + ()'))
    #Запис формули відповідає правилам
    print("\nТест 3\nВхідні дані: x + z\nРезультат: ", formula_checker('x + z'))
    #Запис формули не відповідає правилам: пропущена ] після підформули z – z – y
    print("\nТест 4\nВхідні дані: x + ( y – z – [ x + x ] + { [ z – z – y  + ( y ) } ) - z\nРезультат: ", formula_checker('x + ( y – z – [ x + x ] + { [ z – z – y  + ( y ) } ) - z'))
    #Запис формули відповідає правилам
    print("\nТест 5\nВхідні дані: x + ( y – z – [ x + x ] + { [ z – z – y ] + ( y ) } ) - z\nРезультат: ", formula_checker('x + ( y – z – [ x + x ] + { [ z – z – y ] + ( y ) } ) - z'))
    #Запис формули не відповідає правилам: формула закінчується знаком -
    print("\nТест 6\nВхідні дані: x + ( y – z – [ x + x ] + { [ z – z – y ] + ( y ) } ) -\nРезультат: ", formula_checker('x + ( y – z – [ x + x ] + { [ z – z – y ] + ( y ) } ) -'))
    #Запис формули не відповідає правилам: формула закінчується символом a, що не відповідає правилам
    print("\nТест 7\nВхідні дані: x + ( y – z – [ x + x ] + { [ z – z – y ] + ( y ) } ) - a\nРезультат: ", formula_checker('x + ( y – z – [ x + x ] + { [ z – z – y ] + ( y ) } ) - a'))
    #Запис формули не відповідає правилам: немає аргументу опісля знаку + та кількість знаків подвоєно
    print("\nТест 8\nВхідні дані: (x++)\nРезультат: ", formula_checker('(x++)'))
main()
