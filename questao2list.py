numeros = []

while True:
    numero = int(input("Digite um número inteiro positivo (ou 0 para sair): "))
    
    if numero == 0:
        break
    
    numeros.append(numero)
    
if numeros:
    print(f"\nO maior número digitado foi: {max(numeros)}")
else:
    print("\nNenhum número foi digitado.")
    
