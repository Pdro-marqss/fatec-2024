''''
Faça um programa usando laços para desenhar um triangulo na tela utilizando (*), solicitando que o usuário informe quantas linhas o triangulo deve conter
'''

import os

os.system('cls')
os.system('clear')

print("DESENHAR TRIANGULO NA TELA")

linhas = int(input("Quantas linhas desenja ter no trinagulo ?"))

for line in range(1, linhas + 1):
  print("*" * line)
