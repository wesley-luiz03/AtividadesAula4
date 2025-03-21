refri = 2.0
pizzap = 8.0
pizzam = 12.0
pizzag = 16.0

qnt_refri = int(input("Quantidade de Refrigerante: "))
qnt_pizzap = int(input("Quantidade de Pizza Pequena: "))
qnt_pizzam = int(input("Quantidade de Pizza Média: "))
qnt_pizzag = int(input("Quantidade de Pizza Grande: "))
qnt_pessoas = int(input("Quantidade de Pessoas: "))

total_conta = (qnt_refri * refri +
               qnt_pizzap * pizzap +
               qnt_pizzam * pizzam +
               qnt_pizzag * pizzag)

taxa_garcom = total_conta * 0.10
total_com_taxa = total_conta + taxa_garcom

valor_por_pessoa = total_com_taxa / qnt_pessoas

print(f"\nValor total da conta: R$ {total_com_taxa:.2f}")
print(f"Cada pessoa deve pagar: R$ {valor_por_pessoa:.2f}")

