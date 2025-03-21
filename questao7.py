ano_nascimento = int(input("Digite o ano do seu nascimento: "))

soma = 0

for numero in range(1, ano_nascimento + 1):
    if numero % 3 == 0:
        soma += numero
        
print(f"A soma dos números inteiros divisíveis por 3 até {ano_nascimento} é: {soma}.")

