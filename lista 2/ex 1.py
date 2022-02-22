

def maiusculas(frase):
    maiuscula = ''
    for i in frase:
        if ord(i)>=65 and ord(i)<=90:
            maiuscula += i
    return maiuscula

print(maiusculas('PrOgRaMaMoS em python!'))