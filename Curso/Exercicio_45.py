import random
from time import sleep

def resultado():
      if comp1 == op:
            print('Empate')
      elif comp1 - 1 == op:
            print('Derrota')
      elif comp1 - 2 == op:
            print('Vitória')
      elif op == 1 and comp1 == 0:
            print('Vitória')
      elif op == 2 and comp1 == 0:
            print('Derrota')
      elif op == 2 and comp1 == 1:
            print('Vitória')
      print('-=' * 8)

print('Suas opções:\n'
      '[ 0 ] PEDRA\n'
      '[ 1 ] PAPEL\n'
      '[ 2 ] TESOURA')

op = int(input('Qual sua opção:'))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 8)

valor = ['PEDRA','PAPEL','TESOURA']
comp = random.choice(valor)
comp1 = valor.index(comp)
op1 = valor.pop(op)

print(f'Você escolheu {op1}')
print(f'Computador jogou {comp}')

'''if op == 0:
      if comp == 'PEDRA':
            print('Empate')
            print('-=' * 8)
      elif comp == 'PAPEL':
            print('Derrota')
            print('-=' * 8)
      elif comp == 'TESOURA':
            print('Vitória')
            print('-=' * 8)
elif op == 1:
      if comp == 'PEDRA':
            print('Vitória')
            print('-=' * 8)
      elif comp == 'PAPEL':
            print('Empate')
            print('-=' * 8)
      elif comp == 'TESOURA':
            print('Derrota')
            print('-=' * 8)
elif op == 2:
      if comp == 'PEDRA':
            print('Derrota')
            print('-=' * 8)
      elif comp == 'PAPEL':
            print('Vitória')
            print('-=' * 8)
      elif comp == 'TESOURA':
            print('Empate')
            print('-=' * 8)'''
resultado()