from random import randint, choice
from time import sleep


class Protagonista:
    def __init__(self, nome, vivo=True, level=0, poder=20, vida=100):
        self.nome = nome
        self.vivo = vivo
        self.level = level
        self.poder = poder
        self.vida_max = vida
        self.vida_atual = self.vida_max

    def atacar(self, inimigo):
        print('-=' * 50)
        sleep(2)
        print('Sua vez de atacar! Pressione ENTER para rolar o dado!')
        input()
        print('Rolando o dado...')
        sleep(2)
        d20 = randint(1, 20)
        print(f'\nVocê tirou {d20} no d20!')
        sleep(2)

        if 1 <= d20 <= 5:
            dano = randint(1, 6)
            print(f'\n{inimigo.nome} desviou do ataque e deu \033[33m{dano:.2f} de dano\033[m no seu HP')
            self.vida_atual -= dano
            if self.vida_atual <= 0:
                self.vivo = False

        elif 6 <= d20 <= 9:
            dano = self.poder * 0.5
            print(f'\n{inimigo.nome} bloqueou parcialmente o seu ataque, tomando apenas '
                  f'\033[33m{dano:.2f} de dano físico\033[m')
            inimigo.vida -= dano

        elif 10 <= d20 <= 17:
            dano = self.poder
            print(f'\nVocê acertou {inimigo.nome} em cheio, causando \033[33m{dano:.2f} de dano\033[m físico!')
            inimigo.vida -= dano

        else:
            d6 = randint(1, 6)
            bonus = 1 + (d6 * 10 / 100)
            dano = self.poder * bonus
            print('\nHabilidade \033[35mHEAVY ATTACK\033[m ativada! Bonus de 1d6 a mais de dano!')
            sleep(2)
            print('\nPressiona ENTER para rolar o dado!')
            input()
            print('Rolando o dado...')
            sleep(2)
            print(f'\nBônus de \033[35m{d6*10}%\033[m ativado!')
            sleep(2)
            print(f'\nVocê acertou um golpe certeiro na cabeça de {inimigo.nome}, causando '
                  f'\033[33m{dano:.2f} de dano\033[m físico e a mesma quantidade em dano emocional!')
            inimigo.vida -= dano

        if inimigo.vida > 0:
            print('-=' * 50)
            sleep(2)
            print(f'\nVida atual de {self.nome}: {self.vida_atual:.2f} HP')
            print(f'Vida atual de {inimigo.nome}: {inimigo.vida:.2f} HP\n')
        else:
            print('-=' * 50)
            sleep(2)
            print(f'\nVocê matou {inimigo.nome}!\n')
            inimigo.vivo = False
            print('-=' * 50)

    def level_up(self):
        if self.vida_atual < self.vida_max:
            self.vida_atual += self.vida_max * 0.45

            if self.vida_atual > self.vida_max:
                self.vida_atual = self.vida_max

            elif self.vida_atual <= self.vida_max * 0.20:
                self.vida_atual += self.vida_max * 0.10

        self.vida_max *= 1.20
        self.level += 1
        self.poder *= 1.25

        return print(f'{self.nome} subiu de nível!\nStatus atual:\n'
                     f'\033[36mNível\033[m = {self.level}\n'
                     f'\033[35mPoder\033[m = {self.poder:.2f}\n'
                     f'\033[32mVida Atual/Máxima:\033[m {self.vida_atual:.2f}/{self.vida_max:.2f} HP')
