''''
Crie um jogo de dados, onde:
O computador solicitará ao jogador para informar um número qualquer entre 1 e 6
O computador deve então, sortear um número entre 1 e 6
O programa deve mostrar na tela a seguinte informação:
VOCÊ GANHOU: caso o número escolhido pelo usuário seja igual do número sorteado
VOCÊ PERDEU: caso o número escolhido pelo usuário seja diferente do número sorteado
'''

import os
import random

os.system('cls')
os.system('clear')

print("> > > Jogo de dados < < <")
print("| Escolha um numero de 1 a 6 do dado e veja se acertou |")

numero_escolhido = int(input("Escolha um numero do dado (1 a 6): "))

numero_aleatório = random.randint(1, 6)

if numero_escolhido not in range(1, 7):
  print("O numero escolhido não é valido")
else:
  print(f"O numero escolhido é => {numero_escolhido}")
  print(f"E o numero sorteado é => {numero_aleatório}")
  if numero_escolhido == numero_aleatório:
    print("Parabéns. Você ganhou !!!")
  else:
    print("Infelizmente voce perdeu. Tente de novo")
    
    