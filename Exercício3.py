import json

faturamento_json = '''
{
"faturamento": [1000, 2000, 3000, 0, 1500, 0, 1800, 1200, 2300, 4500]
}
'''


dados = json.loads(faturamento_json)['faturamento']

faturamento_valido = [valor for valor in dados if valor > 0]

menor_valor = min(faturamento_valido)
maior_valor = max(faturamento_valido)

media_mensal = sum(faturamento_valido) / len(faturamento_valido)

dias_acima_da_media = len([valor for valor in faturamento_valido if valor > media_mensal])

print(f"Menor valor de faturamento: R${menor_valor:.2f}")
print(f"Maior valor de faturamento: R${maior_valor:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")