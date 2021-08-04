from copy import deepcopy

lista1 = []
lista2 = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    lista1.append(name)
    lista2.append(score)

lista3 = deepcopy(lista2)
lista3.sort()
lista03 = sorted(set(lista3))
nota01 = []
nota = lista03[1]

nota01 = [i for i, item in enumerate(lista2) if item == nota]
nome01 = [lista1[i] for i in nota01]

nome01.sort()
print(end='\n'.join(nome01))