import random

print('''B  - BRANCO
A  - AMARELO
AZ - AZUL
V  - VERMELHO
L  - LARANJAR ''')
CORES = ['B', 'A', 'AZ', 'V', 'L']  # Cores para o nosso jogo
Tentativas = 10
comprimento_codigo = 4


def gerador_codigo():  # ira gerar de forma aleatória a sequência de cores para o nosso jogo
    codigo = []

    for _ in range(comprimento_codigo):
        color = random.choice(CORES)
        codigo.append(color)

    return codigo


# 2 = Usuario adivinhara o codigo

def advinhe_codigo():
    while True:
        adivinha = str(input('Adivinhar: ')).upper().split(' ')  # transforma a variavel em um lista

        if len(adivinha) != comprimento_codigo:
            print(f'Voce deve adivinhar {comprimento_codigo} cores, Ok.')
            continue

        for cor in adivinha:  # Percorre a lista do usuario
            if cor not in CORES:
                print(f'Cor invalida: {cor}. Tente novamente')
                break  # se a cor for invalida, o Código ira sair desse loop for, e fazer o While. Até as cores serem validas
        else:
            break
    return adivinha


def ver_codigo(adivinha, codigo_verdadeiro):
    contagem_cores = {}
    pos_correta = 0
    pos_incorreta = 0

    for cor in codigo_verdadeiro:
        if cor not in contagem_cores:
            contagem_cores[cor] = 0
        contagem_cores[cor] += 1

    for cor_adivinha, cor_real in zip(adivinha, codigo_verdadeiro):
        if cor_adivinha == cor_real:
            pos_correta += 1
            contagem_cores[cor_adivinha] -= 1

    for cor_adivinha, cor_real in zip(adivinha, codigo_verdadeiro):
        if cor_adivinha in contagem_cores and contagem_cores[cor_adivinha] > 0:
            pos_incorreta += 1
            contagem_cores[cor_adivinha] -= 1

    return pos_correta, pos_incorreta


def jogo():
    print(f'Bem vindo ao Mastermind, Voce deve adivinhar  o codigo em {Tentativas} tentativas')
    print('As cores validar sao', *CORES)

    codigo = gerador_codigo()
    for tentativas in range(1, Tentativas + 1):
        adinhar = advinhe_codigo()
        pos_correta, pos_incorrta = ver_codigo(adinhar, codigo)

        if pos_correta == comprimento_codigo:
            print(f'Voce adivinhou o codigo em {tentativas}.')
            break
        print(f'Posições correta: {pos_correta} | Posições incorreta: {pos_incorrta} ')

    else:
        print('Voce esgotou as tentativas, o codigo é', *codigo)


if __name__ == "__main__":
    jogo()