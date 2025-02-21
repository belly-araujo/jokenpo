import random
import time
jogadas = ('pedra', 'papel', 'tesoura')
placarh = 0
placarc = 0
placarc1 = 0
placarc2 = 0
placarj1 = 0
placarj2 = 0
modalidade = int(input('Bem-vindo(a) ao Jogo de Jokenpô!\nVamos começar!\n\nPrimeiro digite o número correspondente á modalidade desejada:\n\nComputador x Computador(1)\nHumano x Computador(2)\nHumano x Humano(3)\nNúmero escolhido:'))
while True:
    if modalidade == 2:
        jogada = int(input('\nEscolha sua jogada:\nPedra(1)\nPapel(2)\nTesoura(3)\nNúmero escolhido:'))
        time.sleep(0.5)
        print('JO')
        time.sleep(0.5)
        print('KEN')
        time.sleep(0.5)
        print('PO!')
        time.sleep(0.5)
        if jogada == 1:
            print('\nVocê escolheu pedra.')
        elif jogada == 2:
            print('\nVocê escolheu papel.')
        elif jogada == 3:    
            print('\nVocê escolheu tesoura.')
        else:
            print('\nEsse número não está dentre as opções.')
            break
        jogada_compu = random.choice(jogadas)
        print('O computador escolheu {}.'.format(jogada_compu))
        time.sleep(1)
        if jogada == 1 and jogada_compu == 'pedra':
            print('\nO jogo deu empate!')
        elif jogada == 1 and jogada_compu == 'papel':
            print('\nVocê perdeu!:(')
            placarc += 1
        elif jogada == 1 and jogada_compu == 'tesoura':
            print('\nVocê ganhou!!')
            placarh += 1
        elif jogada == 2 and jogada_compu == 'pedra':
            print('\nVocê ganhou!!')
            placarh += 1
        elif jogada == 2 and jogada_compu == 'papel':
            print('\nO jogo deu empate!')
        elif jogada == 2 and jogada_compu == 'tesoura':
            print('\nVocê perdeu!:(')
            placarc += 1
        elif jogada == 3 and jogada_compu == 'pedra':
            print('\nVocê perdeu!:(')
            placarc += 1
        elif jogada == 3 and jogada_compu == 'papel':
            print('\nVocê venceu!!')
            placarh += 1
        elif jogada == 3 and jogada_compu == 'tesoura':
            print('\nO jogo deu empate!')
        print('--------------PLACAR--------------')
        print('|   COMPUTADOR   |      VOCÊ     |')
        print('|       ' ,placarc,'      |      ', placarh, '      |')
        print('----------------------------------')
    if modalidade == 1:
        jogada_compu1 = random.choice(jogadas)
        jogada_compu2 = random.choice(jogadas)
        time.sleep(0.5)
        print('JO')
        time.sleep(0.5)
        print('KEN')
        time.sleep(0.5)
        print('PO!')
        time.sleep(0.5)
        print('O computador 1 escolheu {}.'.format(jogada_compu1))
        print('O computador 2 escolheu {}.'.format(jogada_compu2))
        if jogada_compu1 == 'pedra' and jogada_compu2 == 'pedra':
            print('\nO jogo deu empate!')
        elif jogada_compu1 == 'pedra' and jogada_compu2 == 'papel':
            print('\nComputador 1 perdeu!:(')
            placarc2 += 1
        elif jogada_compu1 == 'pedra' and jogada_compu2 == 'tesoura':
            print('\nComputador 1 ganhou!!')
            placarc1 += 1
        elif jogada_compu1 == 'papel' and jogada_compu2 == 'pedra':
            print('\nComputador 1 ganhou!!')
            placarc1 += 1
        elif jogada_compu1 == 'papel' and jogada_compu2 == 'papel':
            print('\nO jogo deu empate!')
        elif jogada_compu1 == 'papel' and jogada_compu2 == 'tesoura':
            print('\nComputador 1 perdeu!:(')
            placarc2 += 1
        elif jogada_compu1 == 'tesoura' and jogada_compu2 == 'pedra':
            print('\nComputador 1 perdeu!:(')
            placarc2 += 1
        elif jogada_compu1 == 'tesoura' and jogada_compu2 == 'papel':
            print('\nComputador 1 venceu!!') 
            placarc1 +=1
        elif jogada_compu1 == 'tesoura' and jogada_compu2 == 'tesoura':
            print('\nO jogo deu empate!')
        print('--------------PLACAR--------------')
        print('|   COMPUTADOR1  |   COMPUTADOR2 |')
        print('|       ' ,placarc1,'      |      ', placarc2, '      |')
        print('----------------------------------')
    if modalidade == 3:
        jogada1 = int(input('\nJogador 1, escolha sua jogada sem que o outro jogador veja!:\nPedra(1)\nPapel(2)\nTesoura(3)\nNúmero escolhido:'))
        jogada2 = int(input('\nJogador 2, escolha sua jogada sem que o Jogador 1 veja!:\nPedra(1)\nPapel(2)\nTesoura(3)\nNúmero escolhido:'))
        print('JO')
        time.sleep(0.5)
        print('KEN')
        time.sleep(0.5)
        print('PO!')
        time.sleep(0.5)
        if jogada1 == 1:
            print('\nJogador 1 escolheu pedra.')
        elif jogada1 == 2:
            print('\nJogador 1 escolheu papel.')
        elif jogada1 == 3:    
            print('\nJogador 1 escolheu tesoura.')
        if jogada2 == 1:
            print('Jogador 2 escolheu pedra.')
        elif jogada2 == 2:
            print('Jogador 2 escolheu papel.')
        elif jogada2 == 3:    
            print('Jogador 2 escolheu tesoura.')
        time.sleep(1)
        if jogada1 == 1 and jogada2 == 1:
            print('\nO jogo deu empate!')
        elif jogada1 == 1 and jogada2 == 2:
            print('\nJogador 2 venceu!')
            placarj2 += 1
        elif jogada1 == 1 and jogada2 == 3:
            print('\nJogador 1 venceu!')
            placarj1 += 1
        elif jogada1 == 2 and jogada2 == 1:
            print('\nJogador 1 venceu!')
            placarj1 += 1
        elif jogada1 == 2 and jogada2 == 2:
            print('\nO jogo deu empate!')
        elif jogada1 == 2 and jogada2 == 3:
            print('\nJogador 2 venceu!')
            placarj2 += 1
        elif jogada1 == 3 and jogada2 == 1:
            print('\nJogador 2 venceu!')
            placarj2 += 1
        elif jogada1 == 3 and jogada2 == 2:
            print('\nJogador 1 venceu!')
            placarj1 += 1
        elif jogada1 == 3 and jogada2 == 3:
            print('\nO jogo deu empate!')
        print('--------------PLACAR--------------')
        print('|    JOGADOR 1   |    JOGADOR 2  |')
        print('|       ' ,placarj1,'      |      ', placarj2, '      |')
        print('----------------------------------')
    time.sleep(2)
    continuar = input('Deseja jogar de novo?\nResponda com Sim ou Não:')
    if continuar != 'Sim':
        print('\nObrigado por jogar!')
        break