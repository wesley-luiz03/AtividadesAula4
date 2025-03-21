soma_notas = 0
contador = 1

while contador <= 5:
    nota = float(input(f"Digite a nota do aluno {contador}: "))
    soma_notas += nota
    contador += 1
    
media_turma = soma_notas / 7

print(f"A média da turma é: {media_turma:.2f}")