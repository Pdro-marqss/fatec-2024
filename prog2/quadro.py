''''
2) Crie um arquivo chamado quadro.py, e nele escreva o código para desenhar um quadro com 5 linhas por 10 colunas e preenchimento vazio conforme abaixo : 
##########
#        #
#        #
#        #         
##########
Desafio I : Modifique o programa para imprimir tudo isso usando apenas um comando print
Desafio II: Modifique o programa e o tamanho do quadro para imprimir o texto “Programação II” dentro do quadro.
'''

import os

os.system('cls')
os.system('clear')

print("Resolução principal: ")

base = '##########'
corner = '#        #'

lines = 5

i = 0

while i < lines:
  i = i + 1
  if i == 1 or i == lines:
    print(base)
  else: 
    print(corner)


# Desafio I
print()
print("Desafio I: ")

print(
'''
##########
#        #
#        #
#        #
##########
  '''
)


# Desafio II
print()
print("Desafio II: ")

print(
'''
##################
#                #
#                #
# Programação II #
#                #
#                #
##################
  '''
)