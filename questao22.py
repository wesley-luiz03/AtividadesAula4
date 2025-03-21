numeros = []

for i in range(5):
        number = int(input(f"Digite o {i + 1}º número inteiro: "))
        numeros.append(number)
        
if numeros:
    print(f"O maior número fornecido foi: {max(numeros)}")
    print(f"O menor número fornecido foi: {min(numeros)}")