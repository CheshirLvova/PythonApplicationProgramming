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

##--------------------------------Задача 3--------------------------------------
##В текстовому файлі чи в текстовому рядку записана без помилок формула за такими правилами:
##формула ::= цифра | "S(" формула "," формула ")" | "D(" формула "," формула ")"
##цифра ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
##де S означає функцію суми двох аргументів, а D – функцію ділення.
##Обчислити як ціле число значення заданої формули.
##Наприклад, для D(8,S(2,1)) відповідь буде 2.
##Ідея розв'язку цієї задачі подібна до задачі 2 – обчислену частину записувати в стек.

def infixToPostfix(infixexpr):  #першу перетворюємо вхідні дані з інфіксної форми у постфіксну для подальшого опрацювання
    prec = {}
    prec["D"] = 3
    prec["S"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "0123456789":
            postfixList.append(token)
        elif token == '(' :
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.empty()) and \
                  (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)
    while not opStack.empty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

def postfixEval(postfixExpr):   #обчислюємо постфіксну форму запису
    if len(postfixExpr) == 1 and postfixExpr in "0123456789":   #перевірка, чи наша формула не є числом -> виведення числа, як результату
        return print(postfixExpr)
    else:
        operandStack = Stack()
        tokenList = postfixExpr.split()

        for token in tokenList:
            if token in "0123456789":
                operandStack.push(int(token))
            else:
                operand2 = operandStack.pop()
                operand1 = operandStack.pop()
                result = doMath(token,operand1,operand2)
                operandStack.push(result)
        return print(result)

def doMath(op, op1, op2):   #допоміжна функція для виконання ділення чи додавання двох аргументів
    op1 = int(op1)
    op2 = int(op2)
    if op == "D":
        return op1 // op2
    else:
        return op1 + op2
    
def main():
    #тестування 3 завдання
    print("Тест 1: \nвхідні дані: D(8,S(2,1)) \nРезультат:", end=" ")
    input_data = 'D(8,S(2,1))'
    data = ""
    for i in range(len(input_data)):
        if input_data[i] != ',':
            data+=input_data[i] + " "
    postfixEval(infixToPostfix(data))
    print("\nТест 2: \nвхідні дані: D(S(9,6),S(2,1)) \nРезультат:", end=" ")
    input_data = 'D(S(9,6),S(2,1))'
    data = ""
    for i in range(len(input_data)):
        if input_data[i] != ',':
            data+=input_data[i] + " "
    postfixEval(infixToPostfix(data))
    print("\nТест 3: \nвхідні дані: 8 \nРезультат:", end=" ")
    input_data = '8'
    data = ""
    for i in range(len(input_data)):
        if input_data[i] != ',':
            data+=input_data[i] + " "
    postfixEval(infixToPostfix(data))
main()
