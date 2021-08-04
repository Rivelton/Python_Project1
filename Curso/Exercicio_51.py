'''Desenvolva um programa que leia o primeiro termo e a
razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.'''

print('=-' * 12)
print(' 10 termos de uma PA')
print('=-' * 12)

valor = int(input('digite o primeiro termo:'))
razao = int(input('Razão:'))
total = razao * 10 + valor

razao1 = 0

for l in range(valor,total,razao):
    razao1 += razao
    print(l, end=' -> ')
print(' Acabou')
