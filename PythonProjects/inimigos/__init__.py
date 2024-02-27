from random import randint
from time import sleep


class Inimigo:
    def __init__(self, tipo, habilidade, vivo=True):
        self.vivo = vivo
        self.poder = randint(5, 10)
        self.vida = randint(30, 35)
        self.habilidade = f'\033[35m{habilidade}\033[m'
        self.tipo = f'\033[31m{tipo}\033[m'

    def ultimate(self, protagonista):
        return self.habilidade

    def atacar(self, protagonista):

        print('-=' * 50)
        sleep(2)
        print(f'Vez do {self.tipo} atacar!')
        sleep(2)
        d20 = randint(1, 20)
        sleep(2)

        if 1 <= d20 <= 5:

            print(f'\n{self.tipo} errou o ataque!')
            sleep(2)
            print(f'\n{protagonista.nome} ativou \033[35mATAQUE DE OPORTUNIDADE\033[m')
            sleep(2)
            print('\nPressione ENTER para rolar 1d6!')
            input()
            print('Rolando dado...')
            dano = randint(1, 6)
            sleep(2)
            print(f'\nVocê causou \033[33m{dano} de dano\033[m no HP do {self.tipo}')
            self.vida -= dano
            if self.vida <= 0:
                self.vivo = False

        elif 6 <= d20 <= 9:
            dano = self.poder * 0.5
            print(f'\nO {self.tipo} acertou um ataque fraco! {protagonista.nome} recebeu \033[33m{dano:.2f} '
                  f'de dano\033[m físico')
            protagonista.vida_atual -= dano

        elif 10 <= d20 <= 17:
            dano = self.poder
            print(f'\nO {self.tipo} acertou {protagonista.nome} em cheio, causando \033[33m{dano:.2f} de dano\033[m '
                  f'físico!')
            protagonista.vida_atual -= dano

        else:
            self.ultimate(protagonista)

        if protagonista.vida_atual > 0:
            print('-=' * 50)
            sleep(2)
            print(f'\nVida atual de {protagonista.nome}: {protagonista.vida_atual:.2f} HP')
            print(f'Vida atual do {self.tipo}: {self.vida:.2f} HP\n')

        else:
            print('-=' * 50)
            sleep(2)
            print(f'\nVocê foi morto pelo {self.tipo}!\n')
            protagonista.vivo = False
            print('-=' * 50)

    def info(self):

        print('-=' * 50)
        sleep(2)
        print(f'Você enfrentará um {self.tipo} com {self.poder} FC e {self.vida} HP')
        sleep(2)


class Goblin(Inimigo):
    def __init__(self, tipo='Goblin', habilidade='DILACERAR', vivo=True):
        super().__init__(tipo, habilidade, vivo)

    def ultimate(self, protagonista):
        d6 = (randint(1, 6) / 10) + 1
        dano = self.poder * d6
        print(f'\nO {self.tipo} ativou a habilidade \033[35m{self.habilidade}\033[m!')
        sleep(2)
        print(f'\nUm d6 será rolado para determinar o dano adicional')
        sleep(2)
        print(f'\nO {self.tipo} usou uma pequena faca para cortar o corpo de {protagonista.nome}, causando '
              f'\033[33m{dano:.2f} de dano\033[m!')
        protagonista.vida_atual -= dano


class Orc(Inimigo):
    def __init__(self, tipo='Orc', habilidade='ARREMESSO DE PEDRA', vivo=True):
        super().__init__(tipo, habilidade, vivo)
        self.vida = randint(35, 45)
        self.poder = randint(10, 15)

    def ultimate(self, protagonista):
        d6 = (randint(1, 6) / 10) + 1
        dano = self.poder * d6
        print(f'\nO {self.tipo} ativou a habilidade \033[35m{self.habilidade}\033[35m!')
        sleep(2)
        print(f'\nUm d6 será rolado para determinar o dano adicional')
        sleep(2)
        print(f'\nO {self.tipo} arrancou uma grande rocha fincada na parede, arremessando-a em {protagonista.nome}! '
              f'\033[33m{dano:.2f} de dano\033[m foi causado!')
        protagonista.vida_atual -= dano


class Troll(Inimigo):
    def __init__(self, tipo='Troll', habilidade='MORDIDA', vivo=True):
        super().__init__(tipo, habilidade, vivo)
        self.vida = randint(45, 60)
        self.poder = randint(15, 20)

    def ultimate(self, protagonista):
        d6 = (randint(1, 6) / 10) + 1
        dano = self.poder * d6
        print(f'\nO {self.tipo} ativou a habilidade \033[35m{self.habilidade}\033[35m!')
        sleep(2)
        print(f'\nUm d6 será rolado para determinar o dano adicional')
        sleep(2)
        print(f'\nO {self.tipo} mordeu o corpo de {protagonista.nome} com suas presas afiadas, '
              f'arrancando um pedaço de sua carne! \033[33m{dano:.2f} de dano\033[m foi causado!')
        protagonista.vida_atual -= dano
