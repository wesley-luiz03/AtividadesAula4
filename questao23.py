num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

resultado = 0
contador = abs(num2)

while contador > 0:
    resultado += abs(num1)
    contador -= 1
    
    if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
        resultado = -resultado
    
    print(f"O produto de {num1} e {num2} é: {resultado}")
    
    