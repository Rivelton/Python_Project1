ano = int(input('Ano de nascimento: '))
idade = 2021 - ano
alistamento = (idade - 18)
data_correta = 2021 - (ano + 18)
print(f'Quem nasceu em {ano} tem {idade} anos em 2021')
if idade > 18:
    print(f'Seu alistamento deveria ter acontecido a {abs(alistamento)} anos')
    print(f'seu alistamento foi em {abs(data_correta - 2021)}')
elif 18 > idade:
    print(f'Ainda falta {abs(alistamento)} anos para seu alistamento')
    print(f'Seu alistamento vai ser em {abs(data_correta - 2021)}')
else:
    print('Seu alistamento deve acontecer este anos')