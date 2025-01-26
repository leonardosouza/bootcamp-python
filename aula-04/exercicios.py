# Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
numbers: list = []
for i in range(1, 11):
    numbers.append(i ** 2)
print(numbers);

# Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
languages: list = ["Python", "Java", "C++", "JavaScript"]
languages.remove("C++")
print(languages) 

# Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
livro: dict = {
    "titulo": "Aprendendo Python",
    "autor": "Ramalho",
    "ano": 2005
}

for key in livro.items():
    print(key[0], key[1])

# Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
word: str = "inconstitucional".replace(' ', "")
letters: dict = {}

for i in range(0, len(list(word))):
    if not letters.get(word[i]):
        letters[word[i]] = 1
    else:
        letters[word[i]] += 1

print(letters)

# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

nomes_frutas: list = ["maçã", "banana", "cereja"]
frutas: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total_compras = 0

for fruta in nomes_frutas:
    total_compras +=frutas[fruta]

print(total_compras)

