import os;

os.system('cls');
os.system('clear');

print('''
Exercicio 10
Matriz - Ordenação 3 numeros

Digite 3 numeros inteiros e o programa ira ordenalos em ordem crescente      
''');

primeiro_numero = int(input("Primeiro numero: "));
segundo_numero = int(input("Segundo numero: "));
terceiro_mumero = int(input("Terceiro numero: "));
lista_de_numeros = [];
lista_de_numeros += [primeiro_numero, segundo_numero, terceiro_mumero];

def numeros_em_ordem_crescente():
  for i in range(len(lista_de_numeros)):
    for j in range(0, len(lista_de_numeros) - i - 1):
      if lista_de_numeros[j] > lista_de_numeros[j + 1]:
        lista_de_numeros[j], lista_de_numeros[j + 1] = lista_de_numeros[j + 1], lista_de_numeros[j];
  return lista_de_numeros;

print(numeros_em_ordem_crescente());

