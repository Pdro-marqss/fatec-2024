''''
2) Faça um arquivo chamado soma.py e nele escreva o código para solicitar ao usuário que digite dois números, 
armazene estes números em variáveis e em seguida imprima a soma destes números na tela.
'''

import os

os.system('cls')
os.system('clear')

print("> > > Programa que soma 2 numeros < < <")

numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

print(f"Resultado -> {numero1 + numero2}")