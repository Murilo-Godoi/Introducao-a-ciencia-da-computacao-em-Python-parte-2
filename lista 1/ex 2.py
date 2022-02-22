def soma_matrizes(m1, m2):
    if len(m1) == len(m2):
        soma = []
        for i in range(len(m1)):
            if len(m1[i]) == len(m2[i]):
                linha_soma = []
                for j in range(len(m1[i])):
                    linha_soma.append(m1[i][j] + m2[i][j])
            else:
                return False
            soma.append(linha_soma)
    else:
        return False
    return soma

m1 = [[1, 2, 3], [4, 5, 6]]
m2 = [[2, 3, 4], [5, 6, 7]]
print(soma_matrizes(m1,m2))