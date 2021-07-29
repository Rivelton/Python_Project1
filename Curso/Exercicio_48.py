'''Exercício Python 048: Faça um programa que calcule a soma entre todos os números que
são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
valor = 0
for cont in range(1, 500):
    if cont % 3 == 0:
        valor += cont
print(valor)