# contagem regressiva de 10 até 0 com intervalo de um segundo entre cada contagem
from time import sleep
from emoji import emojize
for contagem in range(10, -1, -1):
    sleep(1) #em cada laço vai contar 1 segundo
    print(contagem)
sleep(1)
print(emojize(':tada::tada::tada: \033[36mFELIZ ANO NOVO\033[m :tada::tada::tada:', use_aliases=True))
print('')
sleep(3)
print('\033[7mCTRL + F5 PARA VOLTAR\033[m')
