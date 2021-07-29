def Mensagem():
    print(f'O atleta tem {idade} anos.')


from datetime import datetime

'''Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER'''

nascimento = int(input('Digite data da nascimento: '))
ano_atual = int(datetime.today().strftime('%Y'))
Idade = nascimento - ano_atual
idade = abs(Idade)

if idade in range(0,10):
    Mensagem()
    print('Classificação: MIRIM')
elif idade in range(10, 15):
    Mensagem()
    print(f'Classificação: INFANTIL')
elif idade in range(16, 19):
    Mensagem()
    print(f'Classificação: JÚNIOR')
elif idade in range(20, 26):
    Mensagem()
    print(f'Classificação: SÊNIOR')

else:
    Mensagem()
    print(f'Classificação: MASTER')
