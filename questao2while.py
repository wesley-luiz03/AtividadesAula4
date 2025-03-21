maior_numero = 0

while True:
    numero = int(input("Digite um número inteiro positivo (Digite 0 para sair): "))
    
    if numero == 0:
        break
    
    if numero > maior_numero:
        maior_numero = numero
        
print(f"\nO maior número digitado foi: {maior_numero}")
