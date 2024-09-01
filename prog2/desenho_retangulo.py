''''
Faça um programa usando laços para desenhar um retangulo na tela utilizando números, solicitando que o usuário informe quantas linhas e quantas colunas o retangulo deve conter
Exemplo de Entrada:

linha ==> 5
colunas ==> 6

Exemplo de Saída:
123456
123456
123456
123456
123456
'''

import os

os.system('cls')
os.system('clear')

linhas = int(input("Quantas linhas esse retangulo vai ter ? "))
colunas = int(input("Quantas colunas esse retangulo vai ter ? "))

for line in range(linhas):
  for col in range(1, colunas + 1):
    print(col, end='')
  print()
  