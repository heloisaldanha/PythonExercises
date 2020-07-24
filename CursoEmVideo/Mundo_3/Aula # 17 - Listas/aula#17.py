'''
num = 2, 5, 9, 1
num[2] = 3
print(num)
-----------> dá erro porque as tuplas não mudam.

num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
print(num)
print('Essa lista tem {} elementos'.format(len(num)))
'''

valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print('Na posição {} encontrei o valor {}!'.format(c, v))
print('Cheguei ao final da lista.')




