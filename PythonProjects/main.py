from inimigos import *
from protagonista import *


player = Protagonista(input('Qual o seu nome, guerreiro? '))
player.nome = f'\033[034m{player.nome}\033[m'
dungeon = [Goblin() for x in range(5)]


for goblin in dungeon:

    if player.vivo:
        goblin.info(player)

    while goblin.vivo and player.vivo:

        if goblin.vivo and player.vivo:

            if player.vivo:
                player.atacar(goblin)
            else:
                break

            if goblin.vivo:
                goblin.atacar(player)
            else:
                break

if player.vivo:
    print(f'\nVocê completou a dungeon\n')
    player.level_up()

else:
    print('\nGAME OVER!')
