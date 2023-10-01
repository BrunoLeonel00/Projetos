from cryptography.fernet import Fernet


def carregar_chave():
    arquivo = open('key.key', 'rb')
    chave = arquivo.read()
    arquivo.close()

    return chave


wd = input('Digite sua senha mestre: ')
chave = carregar_chave() + wd.encode()
fer = Fernet(chave)

'''def ler_chave():
    chave = Fernet.generate_key()
    with open('key.key', 'wb') as arquivos_chave:
        arquivos_chave.write(chave)'''


def vizualizar():
    with open('gerenciador de senhas.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            usuario, senha = data.split('|')
            print("Usuário:", usuario, '| Senha',
                  fer.decrypt(senha.encode()).decode())


def adiconar():
    name = str(input('Digite seu nome: '))
    senha = input('Senha: ')

    with open('gerenciador de senhas.txt', 'a') as f:
        f.write(name + '|' + fer.encrypt(senha.encode()).decode() + '\n')


while True:
    mode = input(
        'Voce gostaria de adicionar uma nova senha, ou vizualizar as existentes(view, add), aperte S para sair? ').strip().lower()
    if mode == 's':
        break
    if mode == 'view':
        vizualizar()
    elif mode == 'add':
        adiconar()
    else:
        print('\033[1;31mValor incorreto\033[m')
