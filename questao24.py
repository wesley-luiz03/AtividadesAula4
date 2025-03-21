numeros_pares = []

while True:
    number = int(input("Digite um número positivo (0 para sair): "))
    
    if number == 0:
        break
    
    if number > 0 and number % 2 == 0:
        numeros_pares.append(number)
        
    if numeros_pares:
        media = sum(numeros_pares) / len(numeros_pares)
        print(f"Média dos números pares: {media:.2f}")
    else:
        print("Nenhum número par foi digitado.")