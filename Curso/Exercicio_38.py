n1 = int(input('digite um número: '))
n2 = int(input('digite o segundo número: '))

if n1 > n2:
    print(f'O primeiro número {n1} é maior que o segundo {n2}')
elif n2 > n1:
    print(f'o segundo número {n2} é maior que o primeiro {n1}')
else:
    print('Os dois números são iguais')
