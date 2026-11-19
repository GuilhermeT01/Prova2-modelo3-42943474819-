MINIMA = 21

def idade_permitida(idade):

    if type(idade) != int:
        return False

    if idade > 100:
        return False

    return idade >= MINIMA
