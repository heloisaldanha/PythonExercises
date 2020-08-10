'''
Faça um mini sistema que utilize o interactive help do python. O usuário vai digitar o comando e o manual
vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
Obs.: use as cores.
'''

c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;43m',
     '\033[0;30;44m',
     '\033[0;30;45m',
     '\033[0;30;46m',
     '\033[7m')

def ajuda(comando):
    titulo(f'Acessando o manual do comando \'{comando}\'', 6)
    print(c[7], end='')
    help(comando)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


resposta = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 5)
    print('\033[0;30;43mEscreva o comando desejado ou FIM para encerrar.')
    resposta = str(input('\033[mFunção ou Biblioteca > '))
    if resposta.upper() == 'FIM':
        break
    else:
        ajuda(resposta)
titulo('ATÉ LOGO!', 1)

