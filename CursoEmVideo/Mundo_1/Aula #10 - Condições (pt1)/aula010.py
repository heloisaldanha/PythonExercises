nome = str(input('Qual o seu nome? ')).strip()
lista = nome.split()
if 'Saldanha' in nome:
    print('Que nome lindo você tem!')
else:
    print('Que nome mais "ok""')
print('Bom dia, {}.'.format(lista[0]))

''' O lista[0] é pra chamar o usuário apenas pelo primeiro nome
se colocar um nome muito grande, ele vai responder o nome grande'''