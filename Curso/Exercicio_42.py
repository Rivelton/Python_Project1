'''Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando
o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes'''

n1 = int(input('Primeiro seguimento: '))
n2 = int(input('Segundo seguimento: '))
n3 = int(input('Terceiro seguimento: '))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os seguimentos acima podem formar um triangulo', end=' ')
    if n1 == n2 == n3:
        print('Equilátero!')
    elif n1 != n2 == n3 :
        print('Isóceles!')
    elif n2 != n1 == n3 :
        print('Isóceles!')
    elif n3 != n1 == n2:
        print('Isóceles!')
    elif n1 != n2 != n3:
        print('Escaleno!')
else:
    print('Os segmentos não podem formar um triângulo')
