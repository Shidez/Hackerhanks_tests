N = int(input())

#teste de versão numero 3

lista = []

def list_commands (x):
    if x[0] == "insert":
        x.remove(x[0])
        x = [int(i) for i in x]
        lista.insert(x[0], x[1])
    elif x[0] == "remove":
        x.remove(x[0])
        x = [int(i) for i in x]
        lista.remove(x[0])
    elif x[0] == "append":
        x.remove(x[0])
        x = [int(i) for i in x]
        lista.append(x[0])
    elif x[0] == "sort":
        x.remove(x[0])
        x = [int(i) for i in x]
        lista.sort()
    elif x[0] == "reverse":
        x.remove(x[0])
        x = [int(i) for i in x]
        lista.reverse()
    elif x[0] == "pop":
        x.remove(x[0])
        x = [int(i) for i in x]
        lista.pop()
    elif x[0] == "print":
        print(lista)
        
for i in range(0, N):
    x = str(input()).split()
    list_commands(x)
