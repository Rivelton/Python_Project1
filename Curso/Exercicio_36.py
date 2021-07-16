casa = int(input('Qual o valor da sua casa: '))
salario = int(input('Qual o valor do seu salario:'))
anos = int(input('Qunatos anos vai pagar'))
meses = anos * 12
mensalidade = casa / meses
porcentagem = salario / 100 * 30

print(f'para pagar uma casa de R$ {casa} em {anos}')
print(f'A prestação será de {mensalidade:.2f}')
if mensalidade > porcentagem :
    print(f'Seu mensaliadde de {mensalidade:.2f} ultrapassa os requisitos de sua renda de {porcentagem}, seu emprestimo foi negado')

else:
    print('seu emprestimo foi aprovado')
