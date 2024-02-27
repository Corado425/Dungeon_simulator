from inimigos import *
from protagonista import *


def dungeon(player, covil):
    print(f'\nVocê adentrou no covil dos {covil[0].tipo}\033[31ms\033[m\n')
    for inimigo in covil:

        if player.vivo:
            inimigo.info()

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
        print('-=' * 50)
        print(f'\nVocê completou a dungeon\n')
        player.level_up()

    else:
        print('\nGAME OVER!')


jogador = Protagonista(input('Qual o seu nome, guerreiro? '))
jogador.nome = f'\033[034m{jogador.nome}\033[m'
jogador.info()

covil_goblins = [Goblin() for x in range(1)]
covil_orcs = [Orc() for y in range(2)]
covil_trolls = [Troll() for z in range(2)]

dungeon(jogador, covil_goblins)
dungeon(jogador, covil_orcs)
dungeon(jogador, covil_trolls)
