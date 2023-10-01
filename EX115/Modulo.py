
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


def linha():
    print('~' * 33)


def texto(txt):
    linha()
    print(f'{txt.center(33).upper()}')
    linha()


def escolhas(lista):
    co = 1
    for c in lista:
        print(f'{co} - {c}')
        co += 1



def gerarTxt():
    ler = open('Curso em video.txt', 'rt')
    for l in ler:
        dado = l.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]:<23} {dado[1]:>3} Anos')
    ler.close()



def salvar(nome, idade):
    ficha = open('Curso em video.txt', 'a')
    ficha.write(f'{nome};{idade}\n')
    ficha.close()
