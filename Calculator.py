def calculator():
    print('Simple Calculator')
    print('Here are the operations you can perform: _+ - * /, **,//,%')
    num1 = float(input('Enter first number:'))
    num2 = float(input('enter second number:'))
    operation = input('enter operation:')
    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1-num2)
    elif operation == '*':
        print(num1*num2)
    elif operation == '/':
        print(num1/num2)
    elif operation == '**':
        print(num1**num2)
    elif operation == '//':
        print(num1//num2)
    elif operation == '%':
        print(num1 % num2)
    else:
        print('Invalid operation')
        return
    
      
calculator()