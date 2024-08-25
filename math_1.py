# Solicita o primeiro número do usuário
while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

# Solicita o segundo número do usuário
while True:
    try:
        num2 = float(input("Digite o segundo número: "))
        break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número válido.")

# Solicita ao usuário qual operação deseja realizar
print("\nEscolha uma operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

while True:
    operacao = input("Digite o número da operação desejada (1/2/3/4): ")
    if operacao in ['1', '2', '3', '4']:
        break
    else:
        print("Entrada inválida. Por favor, escolha uma operação válida.")

# Realiza a operação escolhida
if operacao == '1':
    resultado = num1 + num2
    print(f"\nO resultado da adição é: {resultado}")
elif operacao == '2':
    resultado = num1 - num2
    print(f"\nO resultado da subtração é: {resultado}")
elif operacao == '3':
    resultado = num1 * num2
    print(f"\nO resultado da multiplicação é: {resultado}")
elif operacao == '4':
    # Verifica se o divisor é zero antes de realizar a divisão
    if num2 != 0:
        resultado = num1 / num2
        print(f"\nO resultado da divisão é: {resultado}")
    else:
        print("\nErro: Divisão por zero não é permitida.")
