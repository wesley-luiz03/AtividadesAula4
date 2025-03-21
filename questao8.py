num_int = int(input("Digite um número inteiro: "))
filhos = int(input("Quantos filhos você possui? "))
ano_nascimento = int(input("Digite o ano de seu nascimento: "))
primeiro_nome = input("Digite seu primeiro nome: ")
number_letras_nome = len(primeiro_nome)

if num_int == filhos:
    print("O número é igual a quantidade de filhos.")
else:
    print("O número é diferente da quantidade de filhos.")
    
if num_int == ano_nascimento:
    print("O número é igual ao ano de nascimento.")
else:
    print("O número é diferente do ano de nascimento.")
    
if num_int % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
    
if number_letras_nome > 0 and num_int % number_letras_nome == 0:
    print(f"O número é divisível pelo número de letras do seu nome ({number_letras_nome}).")
else:
    print(f"O número não é divisível pelo número de letras do seu nome ({number_letras_nome}).")