'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada km/h acima do limite'''

velocidade = float(input('Qual é a velociadade atual do carro? '))
if velocidade > 80:
    print('\033[31;1mMULTADO!\033[m \033[31mVocê execedeu o limite permitido que é de 80km/h.')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de \033[33mR${:.2f}\033[m.'.format(multa))
else:
    print('\033[32mTenha um bom dia! Dirija com segurança.')