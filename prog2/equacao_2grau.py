''''
Crie um arquivo chamado equacao_2grau.py e faça um programa para calcular os valores de X1 e X2 para uma equação de 2º grau, o programa deve 
solicitar ao usuário para digitar os valores de (A, B, C) guardando este valores em variáveis, e em seguida deve calcular o valor do 
delta e depois calcular os valores de x1 e x2 após calcular mostre estes valores na tela.

Desafio: Modifique o programa para informar que não é possível calcular os valores de X1 e X2 caso o valor de delta seja menor que 0, 
e para mostrar apenas o valor de X1 caso o delta seja igual a 0.
'''

# Formula:         ax²+bx+c=0
# Achar ∆:         b²-4.a.c
# Achar raizes:    x = -b +- raiz de delta / 2.a

import os
import math

os.system('cls')
os.system('clear')

print("> > > Equação de segundo grau < < <")

a = float(input("Digite o valor de A => "))
b = float(input("Digite o valor de B => "))
c = float(input("Digite o valor de C => "))

delta = b**2 - 4 * a * c

if delta == 0:
  x = -b / (2 * a)
  print(f"O resultado é uma raiz real. X = {x}")
elif delta < 0:
  print("Não possui raizes reais")
else: 
  x1 = (-b + math.sqrt(delta) / (2 * a))
  x2 = (-b - math.sqrt(delta) / (2 * a))
  print(f'''
  Raizes da equação:
  x1 = {x1}
  x2 = {x2}
  ''')