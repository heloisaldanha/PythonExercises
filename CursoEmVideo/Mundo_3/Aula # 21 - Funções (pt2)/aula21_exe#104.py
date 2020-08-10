'''
Crie um programa que tenha a função leiaint(), que vai funcionar semelhante à função input(), só que fazendo
a validação para aceitar apenas um valor numérico inteiro.
'''

def leiaint(mensagem):
    paraInt = False  #paraInt se o número for inteiro
    valor = 0
    while True:
        numero = str(input(mensagem))
        if numero.isnumeric():
            valor = int(numero)
            paraInt = True
        else:
            print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        if paraInt:
            break
    return valor

numero = leiaint('Digite um número: ')
print(f'Você digitou o valor {numero}.')