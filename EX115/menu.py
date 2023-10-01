import Modulo
from time import sleep

ler = open('Curso em video.txt', 'a')
while True:
    Modulo.texto('menu principal')
    Modulo.escolhas(['Mostrar a Lista', 'Adicionar uma Pessoa', 'Sair do programa'])
    op = Modulo.leia_int('Digite Sua opção: ')
    if op == 1:
        Modulo.texto('Pessoas cadastradas')
        Modulo.gerarTxt()
    elif op == 2:
        ler = open('Curso em video.txt', 'a')
        Modulo.texto('Cadastrar Pessoas')
        n = Modulo.salvar(str(input('Nome: ')), str(input('Idade: ')))
    if op == 3:
        Modulo.texto('Saindo do sistema')
        sleep(1)
        ler.close()
        break
print('Volte sempre')


