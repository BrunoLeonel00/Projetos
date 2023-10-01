def resumo(num, a, d):
    print('--' * 10)
    print('  RESUMO DO VALOR  ')
    print('--' * 10)
    print(f'''Preço analisado: {moeda(num):^10}
Dobro do preço: {moeda(dobro(num)):^12}
Metade do Preco:{moeda(metade(num)):^12}
{a} de aumento: {moeda(aumento(num, a)):^14}
{d} de redução: {moeda(diminuir(num, a)):^15}''')
    print('-' * 10)


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
