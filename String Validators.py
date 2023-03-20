
s = input()

lista = [[], [], [], [], []]

for i in s:
    lista[0].append(str(i.isalnum()))
    lista[1].append(str(i.isalpha()))
    lista[2].append(str(i.isdigit()))
    lista[3].append(str(i.islower()))
    lista[4].append(str(i.isupper()))

for i in range(0,5):
    if 'False' and 'True' in lista[i]:
        print('True')
    elif 'False' and not 'True' in lista[i]:
        print('False')
    elif 'True' and not 'False' in lista[i]:
        print('True')
      
