def soma_lista(lista):
    print('oi')
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])


lista = [1,3,5,7,9]
