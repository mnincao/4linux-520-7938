cesta = {}
quantidade = 0
quitanda = {
    'Banana': 3.50,
    'Melancia': 7.50,
    'Morango': 5.00
}

def menu_principal():
    print()
    print("-" * 20)
    print("Bem-vindo à quitanda Pytheira!")
    print("1: Ver cesta")
    print("2: Adicionar frutas")
    print("3: Checkout")
    print("4: Sair")

def adicionar_fruta():
    quitanda_ks = list(quitanda.keys())
    while True:
        for (i, fruta) in enumerate(quitanda_ks):
            print(f"{i}: {fruta}")
        print('-1: Sair')

        entrada = int(input("Digite a fruta/opção desejada: "))

        if entrada == -1:
            break

        elif 0 <= entrada < len(quitanda_ks):
            fruta = quitanda_ks[entrada]
            cesta[fruta] = cesta.get(fruta, 0) + 1
        else:
            print("Digite uma opção válida.")

def calcula():
    total = 0
    for (fruta, quantidade) in cesta.items():
        total += quantidade * quitanda[fruta]
    print(f"Total: R$ {total}")

while True:
    menu_principal()

    entrada = int(input('Digite a opção desejada: '))

    if entrada == 4:
        print("Até logo!")
        break

    elif entrada == 1:
        print()
        print("Cesta de frutas:", cesta)

    elif entrada == 2:
        print("=" * 20)
        adicionar_fruta()

    elif entrada == 3:
        print("Cesta:", cesta)

        calcula()

    else:
            print("Digite uma opção válida.")



            