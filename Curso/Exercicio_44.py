'''Exercício Python 044: Elabore um programa que calcule o valor a ser pago por
um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros'''

print('=' * 8, 'Lojas Lima', '=' * 8)

valor = int(input('Preço das compras: R$ '))
print('FORMAS DE PAGAMENTO \n[ 1 ] à vista dinheiro/cheque \n[ 2 ] à vista cartão \n'
      '[ 3 ] 2x no cartão \n[ 4 ] 3x ou mais no cartão')
escolha = int(input('Qual sua opção: '))
if escolha == 1:
      valor1 = (valor / 100) * 90
      print(f'Sua compra será à vista no valor de R${valor:.2f} sem juros\n'
            f'Sua compra ficara no valor de R${valor1:.2f} com desconto de 10%')
elif escolha == 2:
      valor2 = (valor / 100) * 95
      print(f'Sua compra será à vista no valor de R${valor:.f} sem juros\n'
            f'Sua compra ficara no valor de R${valor2:.2f} com desconto de 5%')
elif escolha == 3:
      print(f'Sua compra no valor de R${valor} ficara sem juros')
elif escolha == 4:
      valor4 = (valor / 100) * 120
      print(f'Sua compra será dividida em 3x ou mais no valor de R${valor:.2f}.\n'
            f'Sua compra ficará no valor de R${valor4:.2f} com juros de 20%')
