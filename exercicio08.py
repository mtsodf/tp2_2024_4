# Exercício 08
"""
Você está em uma situação de emergência e precisa se deslocar para o hospital mais próximo. A sua localização é dada pelas coordenadas (x, y)
Você tem as coordenadas de 30 hospitais na cidade, e seu objetivo é encontrar qual é o hospital mais próximo de sua posição para que possa chegar o mais rápido possível.

Crie uma função chamada encontrar_hospital_mais_proximo que recebe as coordenadas (x, y) da sua localização e uma lista de coordenadas de hospitais. A função deve retornar a posição do hospital mais próximo e sua distância para ele.


Obs: Lembre-se que a distância entre dois pontos (x1, y1) e (x2, y2) ser calculada usando a fórmula da distância euclidiana:
    distancia = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
"""


def encontrar_hospital_mais_proximo(sua_coordenada, hospitais):
    return None, -123456789.0


def main():
    sua_coordenada = (5, 10)  # Sua posição

    hospitais = [
        (12, 8),
        (3, 15),
        (8, 14),
        (6, 7),
        (13, 9),
        (4, 12),
        (5, 20),
        (7, 5),
        (11, 13),
        (9, 4),
        (1, 8),
        (3, 6),
        (6, 18),
        (10, 15),
        (14, 3),
        (2, 19),
        (8, 10),
        (7, 12),
        (9, 7),
        (5, 6),
        (3, 14),
        (4, 17),
        (11, 9),
        (2, 10),
        (13, 14),
        (12, 6),
        (9, 11),
        (5, 8),
        (8, 6),
        (4, 5),
    ]

    hospital_mais_proximo, distancia = encontrar_hospital_mais_proximo(
        sua_coordenada, hospitais)

    # Imprimir resultado
    print(f"Hospital mais próximo: {hospital_mais_proximo}")
    print(f"Distância: {distancia:.2f}")
