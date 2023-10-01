def moeda(msg):
    f = str(f'R${msg:.2f} ')
    return f


def metade(num):
    return num / 2


def dobro(num):
    return num * 2


def aumento(num, p):
    porcentagem = num + (p / 100 * num)
    return porcentagem


def diminuir(num, p):
    porcetagem = num - (p / 100 * num)
    return porcetagem