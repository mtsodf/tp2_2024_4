# Exercício 10
"""
Uma empresa de tecnologia quer analisar a performance de seus vendedores com base nas vendas realizadas durante o mês. Eles pediram que você desenvolva um programa para processar os dados de vendas e exibir o ranking dos vendedores com base no número de vendas realizadas.
Você deve criar uma função ranking_vendedores(vendedores) que receba uma lista de tuplas. Cada tupla contém dois elementos: o nome do vendedor (uma string) e o número de vendas realizadas (um número inteiro). A função deve retornar uma lista com os nomes dos vendedores ordenados do maior para o menor número de vendas. Se dois vendedores tiverem o mesmo número de vendas, eles devem ser ordenados em ordem alfabética.
"""


vendedores = [("Alice", 50), ("Bob", 75), ("Carlos", 50), ("Diana", 100), ("Eva", 75)]


def ranking_vendedores(vendedores):
    return None


def main():
    resultado = ranking_vendedores(vendedores)
    print("Ordem dos melhores vendoedores:", resultado)
