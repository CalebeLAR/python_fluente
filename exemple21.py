# Exemplo 2.1 - Cria uma lista de códigos Unicode (codepoints) a partir de uma string?
symbols = "$C£¥€n"
codes = []

for symbol in symbols:
    codes.append(ord(symbol))

codes  # [36, 162, 163, 165, 8364, 164]

# Exemplo 2.1 - Cria uma lista de códigos Unicode (codepoints) a partir de uma string, tomada dois
symbols = "$C£¥€n"
codes = [ord(symbol) for symbol in symbols]

codes

# m código Python, as quebras de linha são ignoradas entre pares [], {}
# ou (). Sendo assim, podemos criarlistas, listcomps, genexps, dicionários
# e outras estruturas com múltiplaslinhassem usar\, que é o escape nada
# elegante para continuação de linha
primeiros = "primeiro01 primeiro02 primeiro03 primeiro04".split()
segundos = "segundo01 segundo02 segundo03 segundo04".split()

codes_comprehensions = [(p, s) for p in primeiros for s in segundos]

codes_normal = []
for p in primeiros:
    for s in segundos:
        codes_normal.append((p, s))

