# Exercício 2

lista = []

frutas = {
    'Banana': 'R$ 3.50',
    'Melancia': 'R$ 7.50',
    'Morango': 'R$ 5.00',
}

while True:
    print('Quintanda:')
    print('1: Ver cesta')
    print('2: Adicionar frutas')
    print('3: Checkout')
    print('4: Sair')

    opcoes = int(input("Selecione a opção desejada: "))
    print('\n')

    if opcoes == 1:
        print('----------------------------')
        print('Cesta:')
        banana = lista.count('Banana')
        melancia = lista.count('Melancia')
        morango = lista.count('Morango')
        if banana > 0:
            print(f'{banana}x banana(s)')
        if melancia > 0:
            print(f'{melancia}x melancia(s)')
        if morango > 0:
            print(f'{morango}x morango(s)')
        if morango == 0 and banana == 0 and melancia == 0:
            print('Você não possui nada na cesta!')
        print('----------------------------')
        print('\n')

    while opcoes == 2:
        print('Menu de frutas:')
        print('Escolha a fruta desejada:')
        print('1 - Banana: R$ 3.50.')
        print('2 - Melancia: R$ 7.50.')
        print('3 - Morango: R$ 5.00.')
        print('4 - Voltar')
        fruta = int(input('Selecione à opção desejada: '))
        if fruta == 1:
            lista.append("Banana")
            print("Banana adicionada com sucesso!")
        elif fruta == 2:
            lista.append("Melancia")
            print("Melancia adicionada com sucesso!")
        elif fruta == 3:
            lista.append("Morango")
            print("Morango adicionado com sucesso!")
        elif fruta == 4:
            break
        else:
            print("Opção inválida!")
        print('\n')

    if opcoes == 3:
        banana = lista.count('Banana')
        melancia = lista.count('Melancia')
        morango = lista.count('Morango')
        total_compras = (float(banana) * 3.50) + (float(melancia) * 7.50) + (float(morango) * 5.00)
        print(f'Total de compras: R$ {total_compras}')
        print('Cesta de compras: ')  # Não sei como posso fazer esta parte.
        print('\n')
    if opcoes == 4:
        break
print('Obrigado, volte sempre!')