def resumo(num, a, d):
    print('--' * 10)
    print('  RESUMO DO VALOR  ')
    print('--' * 10)
    print(f'''Preço analisado: {moeda(num):^10}
Dobro do preço: {dobro(num, True):^12}
Metade do Preco:{metade(num, True):^12}
{a} de aumento: {aumento(num, a, True):^14}
{d} de redução: {diminuir(num, a, True):^15}''')
    print('-' * 10)


def moeda(msg):
    f = str(f'R${msg:.2f} '.replace('.', ','))
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
