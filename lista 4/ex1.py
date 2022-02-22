def ordenada(lista):
    for i in range(len(lista)):
        if i == len(lista) - 1:
            return True
        elif lista[i] > lista[i + 1]:
            return False
