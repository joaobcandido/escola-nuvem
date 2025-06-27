
print("Atividade 1: Calculadora com tratamento de erros")
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        op = input("Digite a operação (+, -, *, /): ")

        if op not in ['+', '-', '*', '/']:
            print("Operação inválida. Tente novamente.")
            continue

        if op == '+':
            resultado = num1 + num2
        elif op == '-':
            resultado = num1 - num2
        elif op == '*':
            resultado = num1 * num2
        elif op == '/':
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
                continue
            resultado = num1 / num2

        print(f"Resultado: {resultado}")
        break

    except ValueError:
        print("Entrada inválida. Por favor, digite números válidos.")

##############################################################
print("Atividade 2: Registro de notas e cálculo da média")

notas = []

while True:
    entrada = input("Digite uma nota (0-10) ou 'fim' para encerrar: ")
    if entrada.lower() == 'fim':
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim'.")

if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi inserida.")

###################################################################

print("Atividade 3: Verificação de senha forte")

while True:
    senha = input("Digite uma senha forte (ou 'sair' para encerrar): ")
    if senha.lower() == 'sair':
        print("Encerrando programa.")
        break
    if len(senha) >= 8 and any(char.isdigit() for char in senha):
        print("Senha forte cadastrada com sucesso!")
        break
    else:
        print("Senha fraca. Deve ter pelo menos 8 caracteres e conter ao menos um número.")

####################################################################

print("Atividade 4: Par ou ímpar com contagem ")

pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")
    if entrada.lower() == 'fim':
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é par.")
            pares += 1
        else:
            print(f"{numero} é ímpar.")
            impares += 1
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")