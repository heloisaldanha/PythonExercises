'''
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
- Até 9 anos: MIRIM.
- Até 14 anos: INFANTIL.
- Até 19 anos: JUNIOR.
- Até 20 anos: SÊNIOR.
- Acima: MASTER.
'''

from datetime import date
atual = date.today().year
born = int(input('''what is the athlete's year of birth? '''))
age = atual - born
print('''The athlete's age is {} yo.'''.format(age))
if age <= 9:
    print('''The athlete belongs to the MIRIM category!''')
elif age <= 14:
    print('''The athlete belongs to the INFANTIL category.''')
elif age <= 19:
    print('''The athlete belongs to the JUNIOR category!''')
elif age <= 25:
    print('''The athlete belongs to the SENIOR category!''')
else:
    print('''The athlete belongs to the MASTER category.''')
