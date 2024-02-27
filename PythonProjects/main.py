from inimigos import *
from protagonista import *


def dungeon(player, covil):
    for inimigo in covil:

        if player.vivo:
            inimigo.info(player)

        while inimigo.vivo and player.vivo:

            if inimigo.vivo and player.vivo:

                if player.vivo:
                    player.turno(inimigo)
                else:
                    break

                if inimigo.vivo:
                    inimigo.atacar(player)
                else:
                    break

    if player.vivo:
        print(f'\nVocê completou a dungeon\n')
        player.level_up()

    else:
        print('\nGAME OVER!')


jogador = Protagonista(input('Qual o seu nome, guerreiro? '))
jogador.nome = f'\033[034m{jogador.nome}\033[m'

covil_goblins = [Goblin() for x in range(3)]
covil_orcs = [Orc() for y in range(2)]
covil_trolls = [Troll() for z in range(2)]

dungeon(jogador, covil_goblins)
dungeon(jogador, covil_orcs)
dungeon(jogador, covil_trolls)
