############################################
print("1. Classificador de Idade")
idade = int(input("Digite sua idade: "))

if 0 <= idade <= 12:
    print("Criança")
elif 13 <= idade <= 17:
    print("Adolescente")
elif 18 <= idade <= 59:
    print("Adulto")
elif idade >= 60:
    print("Idoso")
else:
    print("Idade inválida")


##################################################
print("2. Calculadora de IMC")
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")

##########################################################
print("3. Conversor de Temperatura")
def celsius_para_fahrenheit(c):
    return c * 9/5 + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C/F/K): ").upper()
destino = input("Unidade de destino (C/F/K): ").upper()

if origem == destino:
    resultado = temp
elif origem == "C" and destino == "F":
    resultado = celsius_para_fahrenheit(temp)
elif origem == "C" and destino == "K":
    resultado = celsius_para_kelvin(temp)
elif origem == "F" and destino == "C":
    resultado = fahrenheit_para_celsius(temp)
elif origem == "F" and destino == "K":
    resultado = fahrenheit_para_kelvin(temp)
elif origem == "K" and destino == "C":
    resultado = kelvin_para_celsius(temp)
elif origem == "K" and destino == "F":
    resultado = kelvin_para_fahrenheit(temp)
else:
    print("Conversão inválida.")
    exit()

print(f"Temperatura convertida: {resultado:.2f} {destino}")

#############################################################
print("4. Verificador de Ano Bissexto")
ano = int(input("Digite o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")
