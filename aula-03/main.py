import re

cpf = "281.562.058-80"
cpf = re.sub("[.-]", "", cpf)
masked = ""

for i in range(0, len(cpf)):
    if i >= 2 and i <= 7:
        masked += "x"
    else:
        masked += cpf[i]

print(masked)