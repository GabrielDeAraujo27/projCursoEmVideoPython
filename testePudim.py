import urllib
import urllib.request

try:
    x = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('O site pudim não está disponivel')
else:
    print('O site pudim está disponivel')