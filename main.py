def soma(a, b):
    return a + b

def subtração(a, b):
    return a - b

def multiplicação(a, b):
    return a * b

def divisão(a, b)
    return a / b

print("selecionar a operação que deseje realizar")
print("soma[+]")
print("subtração[-]")
print("multiplicação[*]")
print("divisão[/]")

escolha = input("informe a sua operação: ")

numero_1 = int(input("informe o primeiro numero: "))
numero_2 = int(input("informe o segundo numero: "))

if escolha == "+":
    print(soma(nemero_1, numero_2))

elif escolha == "-":
    print(subtração(numero_1, numero_2))

elif escolha == "*":
    print(multiplicação(numero_1, numero_2))

elif escolha == "/":
    print(multiplicação(numero_1, numero_2))

else:
    print("escolha uma função valida")