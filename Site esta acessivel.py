import urllib.request
try:
    with urllib.request.urlopen('http://pudim.com.br') as response:
        html = response.read()
except:
    print('O site nao esta acessivel')
else:
    print('O site esta acessivel')