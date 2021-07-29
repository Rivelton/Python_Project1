if __name__ == '__main__':
    lista = []
    lista_nome = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lista.append(score)
        lista_nome.append(name)
        if len(lista) > 2:
            valo_maximo = max(lista)
            indice_valor_max = lista.index(valo_maximo)
            lista.remove(valo_maximo)
            lista_nome.pop(indice_valor_max)
    lista_nome.sort()
    print(lista_nome[0])
    print(lista_nome[1])



    '''
    5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output 0

Berry
Harry
    
    '''

