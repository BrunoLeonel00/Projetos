

def enum(num):
    ok = False
    while not ok:
        entrada = str(input(num)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'Erro. \"{entrada}\" invalida ')

        else:
            ok = True
            return float(entrada)

