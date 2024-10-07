import os;

os.system('cls');
os.system('clear');

print('''
Ex11 - Cálculo de méida aritmética e mediana
Digite 20 numeros e veja a média e mediana deles
''');

contador = 0;
valoresDigitados = [];

while contador < 20:
  valorAtualDoLoop = int(input(f"[{contador}-20] Digite o valor: "));
  valoresDigitados.append(valorAtualDoLoop);
  contador += 1;
  os.system('cls');
  os.system('clear');

valoresDigitados.sort();
primeiroValorDoMeio = valoresDigitados[len(valoresDigitados) // 2 - 1];
segundoValorDoMeio = valoresDigitados[len(valoresDigitados) // 2];

print("Os valores digitados são: ", valoresDigitados);
print(f'''
Média: Soma de todos os valores digitados / numero de valores digitados.
Logo a média é {sum(valoresDigitados)} / {len(valoresDigitados)} = {(sum(valoresDigitados)) / len(valoresDigitados)}.

Mediana: Valores do meio do conjunto de dados, somados e divididos por 2 (em caso de conjunto de dados par). Caso seja impar é exatamente o valor do meio.
Logo a mediana é {primeiroValorDoMeio} + {segundoValorDoMeio} / 2 = {(primeiroValorDoMeio + segundoValorDoMeio) / 2}
''');