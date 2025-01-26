import math

# # #### Inteiros (`int`)

# print("\n1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.")
# n1 = int(input("Insira o 1o numero: "))
# n2 = int(input("Insira o 2o numero: "))
# print(f"Soma: {n1 + n2}")

# print("\n2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.")
# num = int(input("Insira um numero: "))
# print(f"Resto da Divisão por 5: {num % 5}")

# print("\n3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.")
# try:
#     n1 = int(input("Insira o 1o numero: "))
#     n2 = int(input("Insira o 2o numero: "))
#     if (isinstance(n1, int) and 
#         isinstance(n2, int)):
#         print(f"Multiplicação: {n1 * n2}")
#     else:
#         print("Uai, aqui precisamos de números")
# except ValueError as e:
#     print("Ai não né!", e)

# print("\n4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.")
# try:
#     n1 = int(input("Insira o 1o numero: "))
#     n2 = int(input("Insira o 2o numero: "))
#     print(f"Divisão Inteira: {n1 // n2}")
# except ZeroDivisionError as e:
#     print("Tentou dividir por zero?", e)
# except KeyboardInterrupt:
#     print("De saida?")
# else:
#     print("funcionou!")
# finally:
#     print("passou por aqui!")

# print("\n5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.")
# num = int(input("Insira um numero: "))
# print(f"Elevado ao quadrado: {num ** 2}")

# # #### Números de Ponto Flutuante (`float`)

# print("\n6. Escreva um programa que receba dois números flutuantes e realize sua adição.")
# n1 = float(input("Insira o 1o numero: "))
# n2 = float(input("Insira o 2o numero: "))
# print(f"Soma: {n1 + n2}")

# print("\n7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.")
# n1 = float(input("Insira o 1o numero: "))
# n2 = float(input("Insira o 2o numero: "))
# print(f"Média: { (n1 + n2) / 2 }")

# print("\n8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).")
# base = float(input("Insira o numero base: "))
# expoente = float(input("Insira o numero expoente: "))
# print(f"Média: { base ** expoente }")

# print("\n9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.")
# temp = float(input("Insira a temperatura (graus celsius): "))
# print(f"Fahrenheit: { (temp * 9/5) + 32 }")

# print("\n10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.")
# raio = float(input("Insira o raio: "))
# area_do_circulo = math.pi * (raio ** 2)
# print(f"Area do Circulo: {area_do_circulo:.2f}")

# #### Strings (`str`)

# print("\n11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.")
# nome = input("Digite seu nome: ")
# print(nome.upper())

# print("\n12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.")
# nome = input("Digite seu nome: ")
# print(nome.split(" ")[0].upper())

# print("\n13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.")
# nome = input("Digite uma frase: ")
# print(nome.strip(" "))

# print("\n14. Faça um programa que peça ao usuário para digitar uma data no formato 'dd/mm/aaaa' e, em seguida, imprima o dia, o mês e o ano separadamente.")
# data = input("Digite uma data: ")
# data = data.split("/")
# print(f"Dia: {data[0]} Mês: {data[1]} Ano: {data[2]}")

# print("\n15. Escreva um programa que concatene duas strings fornecidas pelo usuário.")
# fist_name = input("Digite seu nome: ")
# last_name = input("Digite seu sobrenome: ")
# print(f"{fist_name} {last_name}")

# #### Booleanos (`bool`)
# print("\n16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.")
# try:
#     idade = int(input("Insira sua idade: "))
#     if idade >= 0 and idade <= 12:
#         print(f"Você tem {idade} anos e é uma criança");
#     elif idade >= 13 and idade <= 17:
#         print(f"Você tem {idade} anos e é um adolescente");
#     else:
#         print(f"Você tem {idade} anos e é um adulto");
# except ValueError as e:
#     print("Ocorreu esse erro:", e)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

print("\n18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.")
maior_de_idade = False

while maior_de_idade is not True:
    question = input("Você é maior de idade (S/N)?").upper()
    if question != "S" and question != "N":
        print("Você precisa responder S ou N")
    else:
        if question == "S":
            result = True
        else:
            result = False

        print(f"Você respondeu {str(result)} mas queria responder {str(not result)}")
        exit()


# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação