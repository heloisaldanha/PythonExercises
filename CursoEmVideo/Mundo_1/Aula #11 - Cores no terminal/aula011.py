from time import sleep
from emoji import emojize

print(emojize('\033[30mWhite\033[m :thought_balloon:', use_aliases=True))
sleep(1)
print(emojize('\033[31mRed\033[m :japanese_goblin:', use_aliases=True))
sleep(1)
print(emojize('\033[32mGreen\033[m :green_heart:', use_aliases=True))
sleep(1)
print(emojize('\033[33mYellow\033[m :smile:', use_aliases=True))
sleep(1)
print(emojize('\033[34mBlue\033[m :earth_americas:', use_aliases=True))
sleep(1)
print(emojize('\033[35mPurple\033[m :smiling_imp:', use_aliases=True))
sleep(1)
print(emojize('\033[36mBlue-green\033[m :ocean:', use_aliases=True))
sleep(1)
print(emojize('\033[mGray\033[m :rat:', use_aliases=True))
print('')
sleep(3)
print('PROCESSING...')
sleep(5)
print('-' * 5000)
print('\033[30;1m>>>EXIT\033[m')
print('-' * 5000)

# :sempre junto da string:
# : se colocar separadamente : dá erro
