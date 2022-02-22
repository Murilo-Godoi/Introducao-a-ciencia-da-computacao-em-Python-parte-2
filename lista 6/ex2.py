def encontra_impares(lista):
    print('lista =', lista)
    if len(lista) == 0:
        return []
    item = lista.pop(0)
    print('item = ', item)
    if item % 2 != 0:
        print('oi')
        a = [item] + encontra_impares(lista)
        print(a)
        return a
    return encontra_impares(lista)


lista1 = [2, 3, 4]
lista = [2, 3, 4, 5, 6, 7, 123, 567, 322]
print(encontra_impares(lista))
