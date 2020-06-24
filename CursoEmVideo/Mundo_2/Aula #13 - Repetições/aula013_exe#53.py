# saber se o que foi digitado, ao contrário, é a mesma coisa.

phrase = input('Type a phrase: ').strip().upper()
for c in range(len(phrase) - 1, - 1, - 1):
    print(c)