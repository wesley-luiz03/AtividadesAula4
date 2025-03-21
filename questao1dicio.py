
#Preços do estabelecimento
precos = {
    "refrigerante": 2.0,
    "pizza_pequena": 8.0,
    "pizza_media": 12.0,
    "pizza_grande": 16.0
}

consumo = {}

for item in precos:
    consumo[item] = int(input(f"Quantidade de {item.replace('_', ' ')}: "))
    
qnt_pessoas = int(input("Quantidade de pessoas: "))

total_conta = sum(consumo[item] * precos[item] for item in precos)

taxa_garcom = total_conta * 0.10
total_conta_com_taxa = total_conta + taxa_garcom

valor_por_pessoa = total_conta_com_taxa / qnt_pessoas

print(f"\nValor total da conta: R$ {total_conta_com_taxa:.2f}")
print(f"Cada pessoa deve pagar: R$ {valor_por_pessoa:.2f}")
