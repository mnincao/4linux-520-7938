nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))
nota3 = float(input("digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

if media > 6:
    print("voce esta aprovado")

elif media >= 4:
    print("Recuperacao")

else:
    print("Reprovado")

