# Importar a lib re p/ usar expressões regulares no Python
import re

# Criação da variável string para utilizar as funções da lib
string = """
Semântica é o estudo do significado. Incide sobre a relação entre significantes, tais como palavras, frases, sinais e símbolos, e o que eles representam, a sua denotação. A semântica linguística estuda o significado usado por seres humanos para se expressar através da linguagem.
"""

# Utilização da função re.search() p/ encontrar a primeira recorrência da palavra procurada, caso não encontre retornará None
print(re.search(r"estudo", string))

# Encontrar todas as recorrência com re.findall()
print(re.findall(r"a", string))

# Substituir a palavra em um texto com re.sub()
print(re.sub(r"sinais", "SINAIS", string))

# salvar a expressão regular para a sua reutilização entre outros trechos do código
regex = re.compile(r"sinais")
print(regex.search(string))
