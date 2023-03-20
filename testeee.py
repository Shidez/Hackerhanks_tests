import re

texto = "Fulano Beltrano da Silva é um nome comum no Brasil. Há muitas pessoas chamadas Fulano Beltrano da Silva."




fonte = re.sub(r"(fulano beltrano da silva(.|\s)*)", "", texto, flags=re.IGNORECASE)

print(fonte)


