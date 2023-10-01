import modulos108

# reaproveitar mo modulo do ex107, e adiconar uma função que consiga mostrar os valores como um valor monetário formatado

num = float(input('Digite um numero: '))
print(f'A metadde de {modulos108.moeda(num)} é {modulos108.moeda(modulos108.metade(num))}')
print(f'O Dobro de {modulos108.moeda(num)} é {modulos108.moeda(modulos108.dobro(num))}')
print(f'Aumentando em 10%, temos {modulos108.moeda(modulos108.aumento(num, 10))}')
print(f'Diminuindo em 13%, temos {modulos108.moeda(modulos108.diminuir(num, 13))}')
