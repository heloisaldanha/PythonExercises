'''FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE:
1 - QUANTAS VEZES APARECE A LETRA A
2 - EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
3 - EM QUE POSIÇÃO ELA APARECE PELA ÚLTIMA VEZ'''

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A letra A aparece na posição {} da frase'.format(frase.find('A') + 1))
print('A última letra A aparece na posição {}'.format(frase.rfind('A') + 1))

# .rfind pega a primeira letra da direita pra esquerda.