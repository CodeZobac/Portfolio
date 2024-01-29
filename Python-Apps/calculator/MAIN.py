from art import logo
from replit import clear


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def divide(a, b):
    return a / b


def mult(a, b):
    return a * b


operations = {"+": add, "-": sub, "/": divide, "*": mult}


def calculadora():
    print(logo)
    num1 = float(input("Qual é o primeiro número? "))
    for operator in operations:
        print(operator)
    e = True
    while e:
        operador = input("Escolha um operador: ")
        num2 = float(input("Qual é o próximo número? "))
        calculador = operations[operador]
        resposta = calculador(num1, num2)
        print(f"{num1}{operador}{num2} = {resposta}")
        if input(
                f"Escreve 's' para continuares a calcular com {resposta} ou escreva 'n' para começar um novo cálculo: "
        ) == 's':
            num1 = resposta
        else:
            e = False
            clear()
            calculadora()


calculadora()