from typing import Iterable, Tuple


def calcular_estatisticas(valores: Iterable[int]) -> Tuple[int, float, int, int]:
    """Retorna total, média, maior e menor valor da sequência."""
    lista_valores = list(valores)
    if not lista_valores:
        raise ValueError("A lista de valores não pode estar vazia.")

    total = sum(lista_valores)
    media = total / len(lista_valores)
    maior_valor = max(lista_valores)
    menor_valor = min(lista_valores)

    return total, media, maior_valor, menor_valor


def main() -> None:
    numeros = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, media, maior, menor = calcular_estatisticas(numeros)

    print("total:", total)
    print("media:", media)
    print("maior:", maior)
    print("menor:", menor)


if __name__ == "__main__":
    main()
