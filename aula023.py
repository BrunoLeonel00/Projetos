try:
    a = int(input('Digite um numeroo: '))
    b = int(input('digite mais um numero: '))
    r = a / b
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que voce digitou')
except ZeroDivisionError:
    print(f'O valor 0 nao é divisivel')
except KeyboardInterrupt:
    print('o usuario  preferiu nao digitar os valores')
else:
    print(f'O resultado é {r}')
finally:
    print('volte sempre ')
