def incomodam(n):
    if not isinstance(n, int) or n<=0:
        return ''
    return "incomodam " + incomodam(n-1)

def elefantes(n, contagem = 0):
    if not isinstance(n, int) or n <= 0:
        return ''
    if contagem == n:
        return str(n) + ' elefantes ' + incomodam(n) + 'muito mais\n'
    contagem += 1
    if contagem == 1:
        return 'Um elefante incomoda muita gente\n' + elefantes(n, contagem)
    return str(contagem) + ' elefantes ' + \
           incomodam(contagem) + 'muito mais\n' + str(contagem) +' elefantes incomodam muita gente\n' + elefantes(n,contagem)

