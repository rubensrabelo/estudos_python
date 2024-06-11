import re

string = """
Semântica é o estudo do significado. Incide sobre a relação entre significantes, tais como palavras, frases, sinais e símbolos, e o que eles representam, a sua denotação. A semântica linguística estuda o significado usado por seres humanos para se expressar através da linguagem.
"""

# Utilização do ou (|) em re
# print(re.findall(r"palavras|símbolos", string))

# . = Qualquer caractere (esceção quebra de linha)
# print(re.findall(r".emântica", string))

# [] = Conjunto de caractere
print(re.findall(r"[Ss]emântica", string))
print(re.findall(r"[a-zA-Z]emântica", string))
