n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
print(f'Tirando {n1} e {n2}, a média do aluno é {média}')
if média >= 6:
    print('O aluno foi Aprovado')
else:
    print('O aluno foi Reprovado')