operacoes = {
    "adicao": lambda x, y: x + y,
    "subtracao": lambda x, y: x - y,
    "divisao": lambda x, y: x / y,
    "multiplicacao": lambda x, y: x * y
}


def menu():
    print("""
        0 adicao
        1 subtracao
        2 divisao
        3 multiplicacao
        4 Outros números
        5 Sair
    """)


x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

while True:
    menu()
    op = input("Digite a operação: ")

    if op == "0":
        resultado = operacoes["adicao"](x, y)
        print(f"O resultado de {x} + {y} é {resultado}")
    elif op == "1":
        resultado = operacoes["subtracao"](x, y)
        print(f"O resultado de {x} - {y} é {resultado}")
    elif op == "2":
        resultado = operacoes["divisao"](x, y)
        print(f"O resultado de {x} / {y} é {resultado}")
    elif op == "3":
        resultado = operacoes["multiplicacao"](x, y)
        print(f"O resultado de {x} x {y} é {resultado}")
    elif op == "4":
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))
        menu()
    elif op == "5":
        break