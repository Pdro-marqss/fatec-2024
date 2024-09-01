''''
3) Crie um arquivo chamado nome_completo.py e escreva neste arquivo um programa que solicite o nome do usuário e depois solicite seu sobrenome. O programa deve imprimir o nome e o sobrenome concatenados na tela com um espaço no meio.
Ex.
Digite seu Nome : João
Digite seu Sobrenome : Silva
Seu nome completo é : João Silva
'''

import os

os.system('cls')
os.system('clear')

nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")

print(f"Seu nome completo é: {nome} {sobrenome}")