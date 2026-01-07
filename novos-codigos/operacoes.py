num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# Evitar erro caso o segundo número seja zero
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Não é possível dividir por zero."

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
