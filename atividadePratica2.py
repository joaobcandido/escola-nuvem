#Conversor de Moeda

valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = round(valor_reais / taxa_dolar, 2)
valor_euro = round(valor_reais / taxa_euro, 2)

print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Valor em dólares: US$ {valor_dolar:.2f}")
print(f"Valor em euros: € {valor_euro:.2f}")

#Calculadora de Desconto
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20

valor_desconto = round(preco_original * (porcentagem_desconto / 100), 2)
preco_final = round(preco_original - valor_desconto, 2)

print(f"Produto: {nome_produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {porcentagem_desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")

#Calculadora de Média Escolar
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

media = round((nota1 + nota2 + nota3) / 3, 2)

print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média final: {media:.2f}")

#Calculadora de Consumo de Combustível
distancia = 300  
combustivel = 25  

consumo_medio = round(distancia / combustivel, 2)

print(f"Distância percorrida: {distancia} km")
print(f"Combustível gasto: {combustivel} litros")
print(f"Consumo médio: {consumo_medio} km/l")