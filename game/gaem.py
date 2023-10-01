from random import choice, randint



def vizualizar():
    with open('palavras.txt', 'r+') as f:
        for line in f.readlines():
            print(line)
        f.close()


def sortear():
    palavra = []
    with open('palavras.txt', 'r') as f:
        sorte = f.read()
        palavra.append(sorte.split())
        sorteado = choice(palavra)
        p = sorteado[randint(0, len(sorteado))]
        return p


def tentativa():
    chance = 5
    letras_usuario = list()
    certo = []
    palavra = sortear()
    while True:
        chute = str(input('Chute uma letrar: '))
        letras_usuario.append(chute)
        for l in palavra.lower():
            if l in letras_usuario:
                print(l, end=' ')
                certo.append(l)
            else:
                print('_', end=' ')
        print()
        if chute not in palavra.lower():
            chance -= 1
            print(f'Voce tem {chance} vidas')
        ganhou = True
        for letra in palavra:
            if letra.lower() not in letras_usuario:
                ganhou = False

        if ganhou:
            print('Parabens Voce advinou')
            break
        elif chance == 0 or ganhou:
            print(f'Você perdeu. A palavra era {palavra}')
            break


def jogo():
    print('Bem vindo ao jogo da forca!')
    print('Voce tera 5 tentativas para adivinhar a palavra que estou pensando(nao perde se acertar a letra)')
    print('TEMA: animal que começa com a letra C')
    tentativa()


print(sortear())

if __name__ == "__main__":
    jogo()
