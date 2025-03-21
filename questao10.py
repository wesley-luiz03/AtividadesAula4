nome_mae = "Vania Maria"
nome_pai = "Emanuel Moreira"

nome = input("Digite seu nome e sobrenome: ").strip()
genero = input("Digite seu gênero (M para Masculino / F para Feminino): ").strip().upper()

if genero == "F":
    if nome == nome_mae:
        print("O nome digitado é o da sua mãe.")
    else:
        print("O nome digitado NÃO é o da sua mãe.")
        
elif genero == "M":
    if nome == nome_pai:
        print("O nome digitado é o do seu pai.")
    else:
        print("O nome digitado NÃO é o do seu pai.")
        
else:
    print("Gênero inválido. Digite M para Masculino e F para Feminino.")