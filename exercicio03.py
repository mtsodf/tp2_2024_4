# Exercício 03
"""
Você foi encarregado de realizar uma simulação para analisar o comportamento de um dado de seis faces (numerado de 1 a 6). Para isso, siga os passos abaixo:

Crie uma função chamada simular_lancamento_dado que simule o lançamento de um dado 100 vezes. A função deve retornar uma lista com os resultados dos lançamentos, ou seja, números inteiros entre 1 e 6.

Usando os dados gerados pela função, responda às perguntas abaixo:

a) Qual foi o número que mais apareceu nos lançamentos?
b) Qual foi o número que menos apareceu?
c) Qual é a frequência de cada número (de 1 a 6) nos 100 lançamentos?
d) Qual foi a porcentagem de vezes que o número 6 apareceu nos lançamentos?

Escreva uma função analisar_resultados_dado que receba a lista de resultados dos lançamentos e responda às perguntas acima.

# Exemplo de saída esperada:

Lançamentos: [3, 6, 2, 1, 5, 4, 6, ..., 2]
Número que mais apareceu: 6
Número que menos apareceu: 1
Frequência de cada número: {1: 12, 2: 15, 3: 20, 4: 18, 5: 17, 6: 18}
Porcentagem de 6: 18%

"""


def simular_lancamento_dado():
    return None


def analisar_resultados_dado(lancamentos):
    pass


def main():
    lancamentos = simular_lancamento_dado()
    analisar_resultados_dado(lancamentos)


if __name__ == "__main__":
    main()
