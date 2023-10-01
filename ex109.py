import modulo109


num = float(input('Digite um numero: '))
print(f'A metadde de {modulo109.moeda(num)} é {modulo109.metade(num, False)}')
print(f'O Dobro de {modulo109.moeda(num)} é {(modulo109.dobro(num, True))}')
print(f'Aumentando em 10%, temos {modulo109.aumento(num, 10, True)}')
print(f'Diminuindo em 13%, temos {modulo109.diminuir(num, 13, False)}')
