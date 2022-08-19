def sum(a, b):
    print((a['top'] * b['bottom'])+(a['bottom'] * b['top']), '/', a['bottom'] * b['bottom'])

def sub(a, b):
    print((a['top'] * b['bottom'])-(a['bottom'] * b['top']), '/', a['bottom'] * b['bottom'])

def multiply(a, b):
    print(a['top'] * b['top'], '/', a['bottom'] * b['bottom'])

def divide(a, b):
    print(a['top'] * b['bottom'], '/', a['bottom'] * b['top'])

while True:
    a = {'top': int(input("Fraction 1 - Top: ")), 'bottom': int(input("Fraction 1 - Bottom: "))}
    b = {'top': int(input("Fraction 2 - Top: ")), 'bottom': int(input("Fraction 2 - Bottom: "))}
    choice = input("Operation (+, -, *, /, exit):")
    if choice == '+': sum(a, b)
    elif choice == '-': sub(a, b)
    elif choice == '*': multiply(a, b)
    elif choice == '/': divide(a, b)
    elif choice == 'exit': break
    else: print("Wrong operation")