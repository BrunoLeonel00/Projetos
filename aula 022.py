from utilidades import dados


# programa principla
num = int(input('Digite um numero: '))
fat = dados.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro é {dados.dobro(num)}')
print(f'E o triplo é {dados.triplo(num)}')
