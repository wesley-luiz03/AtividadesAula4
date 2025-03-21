planetas = {
    1: "Mercúrio",
    2: "Vênus",
    3: "Terra",
    4: "Marte",
    5: "Júpiter",
    6: "Saturno",
    7: "Urano",
    8: "Netuno"
}

numero = int(input("Digite um número de 1 a 8: "))

if numero in planetas:
    print(f"O planeta correspondente é: {planetas[numero]}")
else:
    print("Opção inválida, tente novamente.")