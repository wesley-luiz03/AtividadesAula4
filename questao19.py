qnt_alunos = 5
soma_notas = 0

for i in range(qnt_alunos):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    soma_notas += nota
    
media_turma = soma_notas / 7

print(f"A média da turma é: {media_turma:.2f}")