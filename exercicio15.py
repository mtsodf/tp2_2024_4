"""
Cinco times de futebol participam de um campeonato. Cada time disputou 8 partidas, e os resultados de cada partida são representados por strings em uma lista, da seguinte forma:
    - 'V' para vitória,
    - 'E' para empate,
    - 'D' para derrota.

Sabendo que uma vitória vale 3 pontos, um empate vale 1 ponto e uma derrota não vale pontos, escreva uma função chamada calcular_pontos_campeao que recebe duas listas:

times: uma lista com os nomes dos times.
resultados: uma lista de listas, onde cada lista interna contém os resultados das 8 partidas para o time correspondente (na mesma ordem da lista de times).
A função deve calcular a pontuação total de cada time e retornar o nome do time campeão, ou seja, o time com a maior pontuação.

Se houver empate de pontos entre dois ou mais times, retorne uma lista com o nome de todos os times empatados.
"""


def calcular_pontos_campeao(times, resultados):
    return None


def main():
    # Exemplo de uso
    times = ["Time A", "Time B", "Time C", "Time D", "Time E"]
    resultados = [
        ["V", "E", "V", "D", "V", "E", "D", "V"],
        ["E", "D", "V", "V", "D", "V", "V", "D"],
        ["V", "V", "V", "E", "D", "V", "D", "E"],
        ["D", "E", "D", "V", "V", "E", "V", "D"],
        ["V", "D", "E", "E", "V", "D", "E", "V"],
    ]

    campeao = calcular_pontos_campeao(times, resultados)
    print("O campeao foi:", campeao)


if __name__ == "__main__":
    main()
