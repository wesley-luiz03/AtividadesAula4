number1 = int(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
number3 = int(input("Digite o terceiro número: "))

if number1 == number2 == number3:
    print("O três número são iguais!")
elif number1 == number2 or number1 == number3 or number3 == number2:
    print("Dois números são iguais!")
else:
    print("Nenhum dos números são iguais.")