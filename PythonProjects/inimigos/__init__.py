from random import randint, choice
from time import sleep


class Goblin:
    nomes_goblin = ['\033[31mStradald\033[m', '\033[31mCrokokt\033[m', '\033[31mBregonk\033[m', '\033[31mZraald\033[m',
                    '\033[31mXiglegz\033[m', '\033[31mUbhigs\033[m', '\033[31mDring\033[m', '\033[31mStreec\033[m'
                    , '\033[31mPrur\033[m', '\033[31mDragdeat\033[m', '\033[31mCaamoikx\033[m', '\033[31mKraax\033[m']

    def __init__(self, vivo=True):
        self.nome = choice(self.nomes_goblin)
        self.nomes_goblin.remove(self.nome)  # Feito para não repetir os nomes
        self.vivo = vivo
        self.poder = randint(5, 10)
        self.vida = randint(35, 40)

    def atacar(self, protagonista):

        print('-=' * 50)
        sleep(2)
        print(f'Vez de {self.nome} atacar!')
        sleep(2)
        d20 = randint(1, 20)
        sleep(2)

        if 1 <= d20 <= 5:

            print(f'\n{self.nome} errou o ataque!')
            sleep(2)
            print(f'\n{protagonista.nome} ativou \033[35mATAQUE DE OPORTUNIDADE\033[m')
            sleep(2)
            print('\nPressione ENTER para rolar 1d6!')
            input()
            print('Rolando dado...')
            dano = randint(1, 6)
            sleep(2)
            print(f'\nVocê causou \033[33m{dano} de dano\033[m no HP de {self.nome}')
            self.vida -= dano
            if self.vida <= 0:
                self.vivo = False

        elif 6 <= d20 <= 9:
            dano = self.poder * 0.5
            print(f'\n{self.nome} acertou um ataque fraco! {protagonista.nome} recebeu \033[33m{dano:.2f} de dano\033[m'
                  f' físico')
            protagonista.vida_atual -= dano

        elif 10 <= d20 <= 17:
            dano = self.poder
            print(f'\n{self.nome} acertou {protagonista.nome} em cheio, causando \033[33m{dano:.2f} de dano\033[m '
                  f'físico!')
            protagonista.vida_atual -= dano

        else:
            dano = self.poder * 1.5
            print(f'\n{self.nome} ativou a habilidade \033[35mDILACERAR\033[m que causa 50% a mais de dano!')
            print(f'\n{protagonista.nome} sofreu \033[33m{dano:.2f} de dano\033[m físico!')
            protagonista.vida_atual -= dano

        if protagonista.vida_atual > 0:
            print('-=' * 50)
            sleep(2)
            print(f'\nVida atual de {protagonista.nome}: {protagonista.vida_atual:.2f} HP')
            print(f'Vida atual de {self.nome}: {self.vida:.2f} HP\n')

        else:
            print('-=' * 50)
            sleep(2)
            print(f'\nVocê foi morto por {self.nome}!\n')
            protagonista.vivo = False
            print('-=' * 50)

    def info(self, prota):
        return print(f'{prota.nome}, agora você enfrentará {self.nome}, um goblin com {self.poder} FC e {self.vida} HP')
