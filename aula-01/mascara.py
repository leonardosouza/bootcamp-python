import re

cpf_input = input("Digite seu cpf:")
cpf_input = re.sub("[.-]", "", cpf_input)
print(f"{cpf_input[:2]}{'x'*6}{cpf_input[-3:]}")
