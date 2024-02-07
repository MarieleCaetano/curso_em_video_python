import urllib
import urllib.request # necessario para usar a funcão de verificação de rede
# esse prog verifica se há conecçao com a internet, vendo se consegue acessar o site ou nao
try:
    site = urllib.request.urlopen('http://www.pudim.com.br/') #esse comando ve se um site esta funcionando
except urllib.request.URLError:
    print('o SITE não esta acessivel no momento')
else:
    print('consegui acessar o site com sucesso')
    print(site.read()) #mostra o site inteiro por meio dos códigos