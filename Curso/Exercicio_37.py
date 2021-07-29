num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINARIO
[ 2 ] converter para Octal
[ 3 ] coverter para Hexadecimal''')
opção = int(input('Qual sua opção: '))
if opção == 1:
    print('seu numero: {} é igual a {}'.format(num, bin(num)))
elif opção == 2:
    print('seu numero: {} é igual a {}'.format(num, oct(num)))
else:
    print('seu numero: {} é igual a {}'.format(num, hex(num)))