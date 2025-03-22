number = int(input("Digite um número: "))

if number < 0:
    print("Não existe fatorial para número negativo")
else:
    fatorial = 1
    for i in range(1, number + 1):
        fatorial *= i
    
    print(f"O fatorial de {number} é: {fatorial}")
    