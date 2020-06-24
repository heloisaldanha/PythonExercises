'''
Refaça o desafio #35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: Todos os lados iguais
- Isósceles: Dois lados iguais
- Escaleno: todos os lados diferentes.
'''
print('-='*20)
print('Analisador de triângulos')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('\033[1;34mOs segmentos acima PODEM FORMAR triângulo!!\033[m')
    if r1 == r2 == r3:
        print('É um triângulo \033[34mequilátero\033[m pois tem todos os lados iguais!')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('É um triângulo \033[34misósceles\033[m pois tem dois lados iguais.')
    else:
        print('É um triângulo \033[34mescaleno\033[m pois todos os lados são diferentes.')
else:
    print('\033[1;31mOs segmentos acima NÃO PODEM FORMAR triângulo!!!\033[m')