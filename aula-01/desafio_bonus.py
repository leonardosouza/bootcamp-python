BONUS_FIXO = 1000
nome = input("Digite seu nome: ")
salario = float(input("Digite seu salario: "))
target = float(input("Digite seu target de bonus: "))

bonus = BONUS_FIXO + salario * target

print(f"Olá {nome}, o seu bônus foi de: {'{:.2f}'.format(bonus)}")