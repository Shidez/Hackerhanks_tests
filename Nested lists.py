lista = []
listanome = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    lista.append([name, score])

for i in range(len(lista)):
    if i == 0:
        maior = menor = lista[i][1]
    
    if lista[i][1] > maior:
        maior = lista[i][1]
    
    if lista[i][1] < menor:
        menor = lista[i][1]

for l in range(len(lista)):
    if lista[l][1] > menor and maior > lista[l][1]:
        maior = lista[l][1]

for j in range(len(lista)):
    if lista[j][1] == maior:
        listanome.append(lista[j][0])

listanome = sorted(listanome)

for i in listanome:
    print(i)
