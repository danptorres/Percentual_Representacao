dados_faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

#Calcula o valor total de faturamento
faturamento_total = sum(dados_faturamento.values())

#Calcula o percentual de representação de cada estado
print("Percentual de representação de cada estado:")
for estado, faturamento in dados_faturamento.items():
    percentual = (faturamento / faturamento_total) * 100
    print(f"{estado}: {percentual:} %")