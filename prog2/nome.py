'''
1) Crie um arquivo chamado nome.py e nele escreva um programa em Python que solicite ao usuário para digitar o seu próprio nome. 
O programa deve dar as boas vindas mostrando a seguinte mensagem “Bem Vindo  <nome do usuario>”
'''

import os

os.system('cls')
os.system('clear')

nome = input("Qual o seu nome: ")

print(f'Bem Vindo {nome}')