'''
Faça um programa que tenha a função notas() que pode receber várias notas de alunos
e vai retornar um dicionário com as seguintes informações:
- quantidade de notas
- a maior nota
- a menor nota
- a média da turma
- a situação
Adicione também docstrings à função.
'''

def notas(*todasNotas, situacao=False):
    '''
    -> Função para verificar as notas e a situação final de um aluno.
    :param notas: Todas as notas do aluno.
    :param situacao: Parâmetro não obrigatório para saber a situação final do aluno, de acordo com a média das notas.
    :return: Dicionário contendo a quantidade de notas armazenadas, a maior e menor nota, média e situação do aluno
    caso o parâmetro de situação seja exigido.
    '''
    armazenamentoNotas = {}
    armazenamentoNotas['total'] = len(todasNotas)
    armazenamentoNotas['maior'] = max(todasNotas)
    armazenamentoNotas['menor'] = min(todasNotas)
    armazenamentoNotas['media'] = sum(todasNotas) / len(todasNotas)
    if situacao:
        if armazenamentoNotas['media'] >= 7:
            armazenamentoNotas['situacao'] = 'BOA'
        elif armazenamentoNotas['media'] >= 5:
            armazenamentoNotas['situacao'] = 'RAZOÁVEL'
        else:
            armazenamentoNotas['situacao'] = 'RUIM'
    return armazenamentoNotas


resultado = notas(9, 10, 5.5, 2.5, 8.5, situacao=True)
print(resultado)