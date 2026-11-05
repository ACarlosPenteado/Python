operacao = input("Digite a operação: ")

while operacao != "saída":
    if operacao == "soma":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"O resultado da soma é: {resultado}")
    elif operacao == "subtração":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"O resultado da subtração é: {resultado}")
    elif operacao == "multiplicação":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"O resultado da multiplicação é: {resultado}")
    elif operacao == "divisão":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 / num2
        if num2 == 0:
            print("Erro: divisão por zero")
        else:
            print(f"O resultado da divisão é: {resultado}")
    else:
        print("Operação inválida")
    operacao = input("Digite a operação: ")
print("Obrigado por usar o programa!")
