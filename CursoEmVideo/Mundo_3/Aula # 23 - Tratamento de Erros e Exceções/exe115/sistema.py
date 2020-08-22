from lib.interface import *  # esse asterisco é pra importar tudo que tá dentro de lib.interface
from lib.arquivo import *
from time import sleep

arquivo = 'teste.txt'
if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver Pessoas Cadastradas', 'Cadastrar Nova Pessoa', 'Sair do sistema'])
    if resposta == 1:
        # opção de listar o conteúdo de um arquivo
        lerArquivo(arquivo)
    elif resposta == 2:
        cabecalho('NOVO CADASTRO')
        try:
            nome = str(input('Nome: '))
        except KeyboardInterrupt:
            print('\033[31mPrograma interrompido pelo usuário!\033[m')
        idade = leiaint('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
