def leia_int(msg):
    while True:
        try:
            ok = False
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[1;31mErro! Por favor insira um numero inteiro valido\033[m')
        except KeyboardInterrupt:
            print('\33[1;31mO usuario preferiu nao digitar os valores\033[m')
            break
        else:
            ok = True
        if ok:
            break
    return n


def leiaFloat(msg):
    while True:
        try:
            ok = False
            n = float(input(msg))
        except (TypeError, ValueError):
            print('\033[mErro, Por Favor insira um numero flutuante valido\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mO usuario preferi nao digitar os valores\033[m')
            break
        else:
            ok = True
        if ok:
            break
    return n


n = leia_int('Escreva um numero inteiro: ')
n1= leiaFloat('Escreva um numero float: ')
print(f'Voce digitou {n} e {n1}')
