pontuacao = {"vitoria": 3, "empate": 1}

vitorias = int(input("Digite a quantidade de vitórias: "))
empates = int(input("Digite a quantidade de empates: "))

pontos = (vitorias * pontuacao["vitoria"] + (empates * pontuacao["empate"]))

print(f"O time acumulou {pontos} pontos no campeonato.")