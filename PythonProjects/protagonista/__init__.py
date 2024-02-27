from random import randint, choice
from time import sleep


class Protagonista:
    def __init__(self, nome, vivo=True, level=1, poder=20, vida=100):
        self.nome = nome
        self.vivo = vivo
        self.level = level
        self.poder = poder
        self.vida_max = vida
        self.vida_atual = self.vida_max
        self.mochila = [{'item': 'Poção de cura Fraca', 'quantidade': 5},
                        {'item': 'Poção de cura Média', 'quantidade': 3},
                        {'item': 'Poção de cura Forte', 'quantidade': 1},
                        {'item': 'Poção de Força', 'quantidade': 1}]

    def fugir(self, inimigo):  # Define a penalidade para fuga do combate

        print('-=' * 50)
        sleep(2)
        print(f'Você decidiu fugir do combate!\n')
        sleep(2)
        print(f'Role um d4 para determinar sua \033[31mPenalidade!\033[m\n')
        sleep(2)
        d4 = randint(1, 4)
        print(f'Pressione ENTER para jogar o dado!')
        input()
        print(f'Você tirou {d4}! Penalidade aplicada:\n')
        sleep(2)

        if d4 == 1:
            print(f'Redução de 10% no dano de ataque pro resto do jogo!\n')
            print(f'Seu FC passou de \033[34m{self.poder}\033[m para \033[32m{self.poder * 0.9}\033[m')
            self.poder *= 0.9

        elif d4 == 2:
            print(f'Redução de 20% da vida atual!\n')
            print(f'Você perdeu \033[34m{self.vida_atual * 0.2}\033[m pontos de vida! '
                  f'Novo HP = \033[32m{self.vida_atual * 0.8}\033[m pontos')
            self.vida_atual *= 0.8

        elif d4 == 3:
            print(f'Você perdeu um item aleatório da sua mochila!\n')
            item = choice(self.mochila)
            while True:
                if item['quantidade'] <= 0:
                    item = choice(self.mochila)
                else:
                    break
            item['quantidade'] -= 1
            print(f'Uma unidade de \033[34m{item['item']}\033[m foi removida do seu inventário! '
                  f'Nova quantidade = \033[32m{item['quantidade']}\033[m')

            for itens in self.mochila:
                if itens['item'] == item['item']:
                    itens['quantidade'] = item['quantidade']

        else:
            print('Redução de 10% na vida máxima pro resto do jogo!\n')
            print(f'Seu HP máximo passou de \033[34m{self.vida_max}\033[m para \033[32m{self.vida_max * 0.9} pontos!')
            self.vida_max *= 0.9
            if self.vida_max < self.vida_atual:
                self.vida_atual = self.vida_max

        print(f'\nVocê fugiu do {inimigo.tipo} com sucesso!')
        inimigo.vivo = False

    def usar_item(self):  # Define o item que o protagonista decidiu usar, removendo uma unidade do item utilizado!

        print('-=' * 50)
        sleep(2)
        print(f'Itens disponíveis na mochila:\n')
        sleep(1)
        indice = 0
        for idx, valor in enumerate(self.mochila):
            if self.mochila[idx]['quantidade'] > 0:
                print(f'\t{indice}) {self.mochila[idx]["item"]} = {self.mochila[idx]["quantidade"]}')
                indice += 1

        escolhas = range(len(self.mochila))

        while True:
            resposta = int(input('\nQual será a sua escolha? '))
            if resposta not in escolhas:
                print('Por favor, digite um resposta válida!')
                print('-=' * 50)
            else:
                break

        item = self.mochila[resposta]['item']
        quantidade = int(self.mochila[resposta]['quantidade'])

        if item == 'Poção de cura Fraca':
            print(f'\nVocê escolheu o item "Poção de cura Fraca"! 15 pontos de Vida foram recuperados')
            self.vida_atual += 15
            if self.vida_atual > self.vida_max:
                self.vida_atual = self.vida_max
            print(f'\nVida atual de {self.nome}: {self.vida_atual:.2f} HP')
            quantidade -= 1

        elif item == 'Poção de cura Média':
            print(f'\nVocê escolheu o item "Poção de cura Fraca"! 25 pontos de Vida foram recuperados')
            self.vida_atual += 25
            if self.vida_atual > self.vida_max:
                self.vida_atual = self.vida_max
            print(f'\nVida atual de {self.nome}: {self.vida_atual:.2f} HP')
            quantidade -= 1

        elif item == 'Poção de cura Forte':
            print(f'\nVocê escolheu o item "Poção de cura Forte"! 50 pontos de Vida foram recuperados')
            self.vida_atual += 50
            if self.vida_atual > self.vida_max:
                self.vida_atual = self.vida_max
            print(f'\nVida atual de {self.nome}: {self.vida_atual:.2f} HP')
            quantidade -= 1

        else:
            buff = randint(4, 8)
            print(f'\nVocê escolheu o item "Poção de Força"! {buff} pontos de FC foram adicionados permanentemente!')
            self.poder += buff
            print(f'\nNovo FC de {self.nome}: {self.poder:.2f} FC')
            quantidade -= 1

        self.mochila[resposta]['quantidade'] = quantidade

        print('-=' * 50)
        sleep(2)
        print(f'Itens remanescentes na mochila:')
        indice = 0
        for idx, valor in enumerate(self.mochila):
            if self.mochila[idx]['quantidade'] > 0:
                print(f'\t{indice + 1}) {self.mochila[idx]["item"]} = {self.mochila[idx]["quantidade"]}')
                indice += 1

    def turno(self, inimigo):  # Aqui é definido o turno onde o protagonista escolhe sua ação

        print('-=' * 50)
        print(f'{self.nome}, é o seu turno!\n')
        sleep(2)
        print(f'Escolha qual será a sua ação:\n'
              f'\n\t1) Atacar o {inimigo.tipo}\n'
              f'\t2) Usar um item consumível\n'
              f'\t3) Fugir do combate\n')
        escolhas = [1, 2, 3]
        while True:
            resposta = int(input('Qual será a sua escolha? '))
            if resposta not in escolhas:
                print('Por favor, digite um resposta válida!')
                print('-=' * 50)
            else:
                break
        if resposta == 1:
            self.atacar(inimigo)
        elif resposta == 2:
            self.usar_item()
        else:
            self.fugir(inimigo)

    def atacar(self, inimigo):  # O nome diz por si só, um d20 é lançado para determinar o sucesso do ataque

        print('-=' * 50)
        sleep(2)
        print('Você escolheu atacar! Pressione ENTER para rolar o dado!')
        input()
        print('Rolando o dado...')
        sleep(2)
        d20 = randint(1, 20)
        print(f'\nVocê tirou {d20} no d20!')
        sleep(2)

        if 1 <= d20 <= 5:
            dano = randint(1, 6)
            print(f'\nO {inimigo.tipo} desviou do ataque e deu \033[33m{dano:.2f} de dano\033[m no seu HP')
            self.vida_atual -= dano
            if self.vida_atual <= 0:
                self.vivo = False

        elif 6 <= d20 <= 9:
            dano = self.poder * 0.5
            print(f'\nO {inimigo.tipo} bloqueou parcialmente o seu ataque, tomando apenas '
                  f'\033[33m{dano:.2f} de dano físico\033[m')
            inimigo.vida -= dano

        elif 10 <= d20 <= 17:
            dano = self.poder
            print(f'\nVocê acertou o {inimigo.tipo} em cheio, causando \033[33m{dano:.2f} de dano\033[m físico!')
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
            print(f'\nVocê acertou um golpe certeiro na cabeça do {inimigo.tipo}, causando '
                  f'\033[33m{dano:.2f} de dano\033[m físico!')
            inimigo.vida -= dano

        if inimigo.vida > 0:
            print('-=' * 50)
            sleep(2)
            print(f'\nVida atual de {self.nome}: {self.vida_atual:.2f} HP')
            print(f'Vida atual do {inimigo.tipo}: {inimigo.vida:.2f} HP\n')
        else:
            print('-=' * 50)
            sleep(2)
            print(f'\nVocê matou o {inimigo.tipo}!\n')
            inimigo.vivo = False

    def level_up(self):  # Toda vez que a dungeon é completada, o protagonista ganha buff nos atributos

        if self.vida_atual < self.vida_max:
            self.vida_atual += self.vida_max * 0.45

            if self.vida_atual > self.vida_max:
                self.vida_atual = self.vida_max

            elif self.vida_atual <= self.vida_max * 0.20:
                self.vida_atual += self.vida_max * 0.10

        self.vida_max *= 1.20
        self.level += 1
        self.poder *= 1.25

        return print(f'{"-=" * 50}\n'
                     f'{self.nome} subiu de nível!\nStatus atual:\n'
                     f'\033[36mNível\033[m = {self.level}\n'
                     f'\033[35mPoder\033[m = {self.poder:.2f}\n'
                     f'\033[32mVida Atual/Máxima:\033[m {self.vida_atual:.2f}/{self.vida_max:.2f} HP\n'
                     f'{"-=" * 50}')

    def info(self):
        print('-=' * 50)
        print(f'{self.nome}, você recebeu a benção do \033[35mGUERREIRO\033[m!')
        sleep(2)
        print(f'\nSeus status são:')
        sleep(2)
        print(f'\t\033[32mVida Máxima\033[m: {self.vida_max} HP')
        sleep(2)
        print(f'\t\033[33mPoder de combate\033[m: {self.poder} FC')
        sleep(2)
        print(f'\t\033[36mNível atual\033[m: {self.level}')
        sleep(2)
        print(f'\nItens disponíveis na sua mochila:')
        for itens in self.mochila:
            sleep(2)
            if itens['quantidade'] > 1:
                print(f'\t{itens["quantidade"]} unidades de \033[34m{itens["item"]}\033[m')
            else:
                print(f'\t{itens["quantidade"]} unidade de \033[34m{itens["item"]}\033[m')
        print('-=' * 50)
