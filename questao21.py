soma_impares = 0
contador = 0

while contador < 5:
        num = int(input(f"Digite o {contador + 1}º número inteiro: "))
        if 100 <= num <= 200 and num % 2 != 0:
            soma_impares += num
        contador += 1
        
print(f"A soma dos números impares entre 100 e 200 é: {soma_impares}")
