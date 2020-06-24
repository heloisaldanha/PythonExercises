'''
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela
abaixo:
- Abaixo de 18.5: ABAIXO DO PESO.
- Entre 18.5 e 25: PESO IDEAL.
- 25 até 30: SOBREPESO.
- 30 até 40: OBESIDADE.
- Acima de 40: OBESIDADE MÓRBIDA.
'''

peso = float(input('Digite o peso (em kg): '))
altura = float(input('Digite a altura (em metros): '))
imc = peso / (altura**2)
print('O valor do IMC é igual a {:.1f}.'.format(imc))
if imc < 18.5:
    print('\033[1;33mABAIXO DO PESO\033[m')
elif imc < 25:
    print('\033[1;34mPESO IDEAL!\033[m')
elif imc < 30:
    print('\033[1;33mSOBREPESO!\033[m')
elif imc < 40:
    print('\033[1;34mOBESIDADE\033[m')
else:
    print('\033[1;34mOBESIDADE MÓRBIDA\033[m')
