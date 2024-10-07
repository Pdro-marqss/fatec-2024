import os;
import random;

os.system('cls');
os.system('clear');

print('''
Ex13 - Dados do piratas do caribe
''');

contador = 0;
valor_total_sorteado = 0;

while contador < 6:
  numero_sorteado = random.randint(1, 6);
  valor_total_sorteado += numero_sorteado;
  contador = contador + 1;

print('''
Um dado de 1 a 6 foi jogado 6 vezes e os valores somados !!!
      
Tente adivinhar o valor da soma desses numeros. Lembrando que as
possibilidades são de 6 a 36.
''');

is_numero_escolhido_valido = False;

while is_numero_escolhido_valido == False:
  numero_do_jogador = int(input("Qual o valor do chute ? "));

  if(numero_do_jogador < 6 or numero_do_jogador > 36):
    print("Numero invalido, tente um numero de 6 a 36");
    numero_do_jogador = int(input("Qual o valor do chute ? "));
  else:
    is_numero_escolhido_valido = True;

tentativa_do_computador = random.randint(6, 36);

if abs(valor_total_sorteado - numero_do_jogador) < abs(valor_total_sorteado - tentativa_do_computador):
  print(f"Valor da soma dos dados: {valor_total_sorteado}");
  print(f"Valor escolhido pelo jogador: {numero_do_jogador}");
  print(f"Valor escolhido pela maquina: {tentativa_do_computador}");
  print("O numero digitado pelo jogador é mais próximo. Você ganhou !!!");
elif abs(valor_total_sorteado - tentativa_do_computador) < abs(valor_total_sorteado - numero_do_jogador):
  print(f"Valor da soma dos dados: {valor_total_sorteado}");
  print(f"Valor escolhido pelo jogador: {numero_do_jogador}");
  print(f"Valor escolhido pela maquina: {tentativa_do_computador}");
  print("O numero digitado pela maquina é mais próximo. Você perdeu :(");
else:
  print(f"Valor da soma dos dados: {valor_total_sorteado}");
  print(f"Valor escolhido pelo jogador: {numero_do_jogador}");
  print(f"Valor escolhido pela maquina: {tentativa_do_computador}");
  print("EMPATE");
