def moeda(msg):
    f = str(f'R${msg:.2f} ')
    return f


def metade(num, f=False):
    if f:
        d = moeda(num / 2)
    else:
        d = num / 2
    return d


def dobro(num, f=False):
    if f:
        m = moeda(num * 2)
    else:
        m = num * 2
    return m


def aumento(num, p, f=False):
    porcentagem = num + (p / 100 * num)
    if f:
        return moeda(porcentagem)
    else:
        return porcentagem


def diminuir(num, p, f=False):
    porcetagem = num - (p / 100 * num)
    if f:
        return moeda(porcetagem)
    else:
        return porcetagem
