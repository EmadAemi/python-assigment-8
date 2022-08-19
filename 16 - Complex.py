def sum(a, b):
    print(a['real'] + b['real'], '+', a['imaginary'] + b['imaginary'], 'i')


def sub(a, b):
    print(a['real'] - b['real'], '+', a['imaginary'] - b['imaginary'], 'i')


def multiply(a, b):
    print((a['real'] * b['real']) - (a['imaginary'] * b['imaginary']), '+',
          (a['imaginary'] * b['real']) - (a['real'] * b['imaginary']), 'i')


while True:
    a = {'real': int(input("Complex 1 - Real: ")), 'imaginary': int(input("Complex 1 - Imaginary: "))}
    b = {'real': int(input("Complex 2 - Real: ")), 'imaginary': int(input("Complex 2 - Imaginary: "))}
    choice = input("Operation (+, -, *, exit):")
    if choice == '+':
        sum(a, b)
    elif choice == '-':
        sub(a, b)
    elif choice == '*':
        multiply(a, b)
    elif choice == 'exit':
        break
    else:
        print("Wrong operation")
