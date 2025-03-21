numeros = []

while True:
    num = int(input("Digite um número inteiro positivo (0 para sair): "))
    
    if num == 0:
        break
    
    numeros.append(num)
    
if numeros:
    print(f"O maior número digitado foi: {max(numeros)}")
else:
    print("Nenhum número foi digitado.")    
