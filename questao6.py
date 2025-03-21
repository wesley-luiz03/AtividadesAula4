primeiro_nome = input("Digite seu primeiro nome: ")

letras_primeiro_nome = set(primeiro_nome)

contador = 0

while True:
    letra = input("Digite uma letra (Z para sair): ")
    
    if letra == "z":
        break
    
    if letra in letras_primeiro_nome:
        contador += 1
        
print(f"Quantidade de letras lidas que percetecem ao seu nome: {contador}")