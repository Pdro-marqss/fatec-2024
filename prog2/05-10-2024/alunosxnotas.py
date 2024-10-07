import os

os.system('cls');
os.system('clear');

print('''
Ex12 - Alunos X Notas
Guarda as 5 notas do semestre de 3 alunos em uma matriz e exibe um menu de opçoes
''');

def limpa_console():
  os.system('cls');
  os.system('clear');

def calcula_a_media(notas):
  media = sum(notas) / len(notas);
  return media;

def calcula_a_mediana(notas):
  notas.sort();
  quantidade_de_notas = len(notas);
  if quantidade_de_notas % 2 == 0:
    primeiro_numero_do_meio = notas[quantidade_de_notas // 2 - 1];
    segundo_numero_do_meio = notas[quantidade_de_notas // 2];
    mediana = (primeiro_numero_do_meio + segundo_numero_do_meio) / 2;
  else:
    numero_do_meio = quantidade_de_notas // 2;
    mediana = notas[numero_do_meio];
  return mediana;

matriz_de_notas_alunos = [
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 0]
];

while True:
  print('''
Menu de opções:
Digite a tecla numerica indicada para acessar a opção.

(1) Digitar as notas.
(2) Exibir as notas.
(3) Mostrar a maior nota.
(4) Monstrar a menor nota.
(5) Mostrar a média aritmética de cada aluno.
(6) Mostrar a mediana de cada aluno.
(7) Sair do programa.
''');

  opcao_selecionada = int(input("Qual opção deseja acessar ? "));

  if opcao_selecionada == 1:
    limpa_console();
    for aluno in range(3):
      for nota in range(5):
        matriz_de_notas_alunos[aluno][nota] = float(input(f"Digite a nota {nota + 1} do aluno {aluno + 1}: "));
    print("Matriz de notas atualizado: ", matriz_de_notas_alunos);

  elif opcao_selecionada == 2:
    limpa_console();
    for aluno in range(3):
      notas_do_aluno = matriz_de_notas_alunos[aluno];
      print(f"Notas do aluno {aluno+1}: {notas_do_aluno}");

  elif opcao_selecionada == 3:
    limpa_console();
    for aluno in range(3):
      maior_nota = max(matriz_de_notas_alunos[aluno]);
      print(f"A maior nota do aluno {aluno+1} é: {maior_nota}");

  elif opcao_selecionada == 4:
    limpa_console();
    for aluno in range(3):
      menor_nota = min(matriz_de_notas_alunos[aluno]);
      print(f"A menor nota do aluno {aluno+1} é: {menor_nota}");

  elif opcao_selecionada == 5:
    limpa_console();
    for aluno in range(3):
      media = calcula_a_media(matriz_de_notas_alunos[aluno]);
      print(f"A media do aluno {aluno + 1} é: {media}");

  elif opcao_selecionada == 6:
    limpa_console();
    for aluno in range(3):
      mediana = calcula_a_mediana(matriz_de_notas_alunos[aluno]);
      print(f"A mediana do aluno {aluno + 1} é: {mediana}");

  elif opcao_selecionada == 7:
    limpa_console();
    print("Saindo do programa...");
    break;

  else:
    limpa_console();
    print("Opção invalida. Tente uma das opções numéricas fornecidas (1-7)");