# tabuada
n = int(input('Digite um número e direi sua tabuada: '))
for tabuada in range (1, 10+1):
    print('{:2} x {} = {}'.format(tabuada, n, tabuada * n))