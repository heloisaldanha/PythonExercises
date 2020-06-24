
nome = str(input('Qual o seu nome? ')).strip().title()
if nome == 'Heloísa':
    print('\033[31mQue lindo nome você tem!\033[m')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Ana':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Gabriel Enzo João Breno':
    print('Belo nome masculino!')
else:
    print('Seu nome é bem normal!')
print('Prazer em te conhecer, {}!'.format(nome))