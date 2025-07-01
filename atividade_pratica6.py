

import random
import string
import requests

print("Exercício 1: Gerador de senha aleatória")

def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

try:
    qtd = int(input("Informe a quantidade de caracteres da senha: "))
    if qtd < 1:
        print("Quantidade deve ser maior que zero.")
    else:
        print("Senha gerada:", gerar_senha(qtd))
except ValueError:
    print("Digite um número inteiro válido.")


########################################################################################
print("Exercício 2: Perfil de usuário aleatório (Random User Generator")

url = "https://randomuser.me/api/"
resp = requests.get(url)
if resp.status_code == 200:
    data = resp.json()
    user = data['results'][0]
    nome = f"{user['name']['first']} {user['name']['last']}"
    email = user['email']
    pais = user['location']['country']
    print(f"Nome: {nome}\nEmail: {email}\nPaís: {pais}")
else:
    print("Erro ao obter usuário aleatório.")

################################################################################
print("Exercício 3: Consulta de endereço pelo CEP (ViaCEP")

cep = input("Digite o CEP (somente números): ").strip()
url = f"https://viacep.com.br/ws/{cep}/json/"
resp = requests.get(url)
if resp.status_code == 200:
    data = resp.json()
    if "erro" in data:
        print("CEP não encontrado.")
    else:
        print(f"Logradouro: {data['logradouro']}")
        print(f"Bairro: {data['bairro']}")
        print(f"Cidade: {data['localidade']}")
        print(f"Estado: {data['uf']}")
else:
    print("Erro ao consultar o CEP.")


##############################################################
print("Exercício 4: Cotação de moeda estrangeira (AwesomeAPI")



moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").strip().upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
resp = requests.get(url)
if resp.status_code == 200:
    data = resp.json()
    chave = f"{moeda}BRL"
    if chave in data:
        info = data[chave]
        print(f"Valor atual: {info['bid']}")
        print(f"Valor máximo: {info['high']}")
        print(f"Valor mínimo: {info['low']}")
        print(f"Data/Hora atualização: {info['create_date']}")
    else:
        print("Moeda não encontrada.")
else:
    print("Erro ao consultar cotação.")


