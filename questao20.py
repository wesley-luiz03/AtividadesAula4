soma_impares = 0

for i in range(5):
    numeros = int(input(f"Digite o {i + 1}º número: "))
    
    if numeros % 2 != 0:
        soma_impares += numeros
 
print(f"A soma dos números ímpares lidos é: {soma_impares}")
