'''
Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.
'''
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[31mO site não está disponível no momento. Tente mais tarde.\033[m')
else:
    print('\033[36mO site está disponível! :)\033[m')
