def menor_nome(nomes):
    menor = nomes[0]
    for nome in nomes:
        nome_correto = nome.strip()
        if len(nome_correto) < len(menor):
            menor = nome_correto
    return menor.capitalize()


