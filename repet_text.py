# Solicita a string do usuário
texto = input("Digite a string: ")

# Solicita o número inteiro do usuário
# Usa um loop para garantir que o número seja um inteiro válido
while True:
    try:
        vezes = int(input("Digite o número de vezes que a string deve ser repetida: "))
        if vezes < 0:
            print("Por favor, digite um número inteiro não-negativo.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Repete a string o número de vezes informado
resultado = texto * vezes

# Exibe o resultado
print("Resultado da repetição:", resultado)
