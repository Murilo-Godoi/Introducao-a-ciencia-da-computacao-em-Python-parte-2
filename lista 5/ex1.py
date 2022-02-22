
def busca(lista, elemento):
    maior = len(lista) - 1
    menor = 0
    while menor <= maior:
        meio = (maior + menor)//2
        print(meio)
        if lista[meio] == elemento:
            return meio
        elif lista[meio]< elemento:
            menor = meio + 1
        else:
            maior = meio - 1
    return False


