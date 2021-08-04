'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
pares. Se o valor digitado for ímpar, desconsidere-o.'''
valor = 0
for cont in range(0,6):
    num = int(input('digite um número:'))
    if num % 2 == 0:
        valor += num
print(valor)

