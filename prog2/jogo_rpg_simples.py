''''
Crie o código de um jogo de RPG bem simples de texto, com apenas 2 ambientes

1) Mostrar na tela o ambiente em que o jogador está, descrevendo o lugar
2) Pergunte para onte ele quer ir (N)orte, (S)ul, (L)este, (O)este)
3) Verificar se é possível ele fazer este movimento
4) E caso seja possível descreva o ambiente que ele se encontra no momento
'''

import os

os.system('cls')
os.system('clear')

isGameRunning = True
ambiente_atual = "Caverna"

print("> > > JOGO DE RPG < < <")

while isGameRunning:
  print("Voce está em uma caverna escura, cheia de criaturas mortais e armadilhas mortiferas ")
  print("Escolha uma direção para avançar: (N)orte, (S)ul, (L)este, (O)este")
  print("Ou então pressione X para sair do jogo")
  print()

  print(f"Ambiente atual: {ambiente_atual}")
  direcao = input("Escolhe a direção que deseja seguir => ").upper()

  if direcao == 'S':
    print("Voce achou uma saida que te levou para uma Floresta, próxima a um riacho.")
    ambiente_atual = "Floresta"
    print(f"Ambiente atual: {ambiente_atual}")
    print()
    isGameRunning = False
  elif direcao == 'N':
    print("Você deu de cara com um chupacabra do ruim, cheio de vontade de levar alguém pra conhecer jesus.")
    print("Você morreu...")
    print()
    print("G A M E  O V E R")
    isGameRunning = False
  elif direcao == 'X':
    print("Saindo do jogo...")
    isGameRunning = False
  else:
    print("Você bateu em uma parede, tente outra direção")
    print()
  

