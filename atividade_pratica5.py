print("calcular gorjeta")
def calcular_gorjeta(porcentagem_gorjeta, conta):
    # porcentagem_gorjeta = float(input("Digite o valor da gorjeta em %: "))
    # conta = float(input("Digite o valor da conta: "))

    gorjeta = (porcentagem_gorjeta / 100)
    total = (gorjeta * conta) + conta

    # print(total)
    return total


result = calcular_gorjeta(10, 100)

print(result)

#############################################################
print("verificar se é palindromo")

def is_palindromo(texto):
    # Remove espaços e converte para minúsculas
    texto_limpo = ''.join(char.lower() 
                          for char in texto 
                          if char.isalnum())
    # Compara o texto com sua versão invertida
    return texto_limpo == texto_limpo[::-1]

# Exemplo de uso
frase = "O lobo ama o bolo"
resultado = is_palindromo(frase)

if resultado == True:
    resposta = "Sim"
else:
    resposta = "Não"

print(f"'{frase}' é um palíndromo? {resposta}")


##########################################################

print("ano para dia")
import datetime

def idade_em_dias(ano_nascimento):


    ano_atual = datetime.datetime.now().year

    idade = ano_atual - ano_nascimento
    dias = idade * 365
    
    return dias

result = idade_em_dias(2024)

print(result)