''''
Crie um programa chamado cabecalho.py que mostre o seguinte cabeçalho na tela:
****************************************************************************
******   Programação II -  2º Ciclo Jogos Digitais                    ******
******   Nome <nome do aluno>           RA <ra do aluno>              ******
******   Programa : <nome do programa>                                ******
****************************************************************************​
'''

import os

os.system('cls')
os.system('clear')

nome = input("Qual o seu nome ? ")
ra = input("Show de bola. Agora qual o seu RA ?")
nome_prog = input("E qual o nome desse programa python ?")

print(
f'''
****************************************************************************
******   Programação II -  2º Ciclo Jogos Digitais                    ******
******   Nome {nome}           RA {ra}                                ******
******   Programa : {nome_prog}                                       ******
****************************************************************************​
'''
)
