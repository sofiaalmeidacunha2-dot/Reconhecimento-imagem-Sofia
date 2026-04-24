def eh_primo(numero: int) -> bool:
    """Retorna True se o número informado for primo."""
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    return not _tem_divisor_por_6k_mais_um(numero)


def _tem_divisor_por_6k_mais_um(numero: int) -> bool:
    """Verifica divisores usando a forma 6k ± 1 para números maiores que 3."""
    divisor = 5
    while divisor * divisor <= numero:
        if numero % divisor == 0 or numero % (divisor + 2) == 0:
            return True
        divisor += 6
    return False


def main() -> None:
    exemplo = 29
    print(f"{exemplo} é primo? {eh_primo(exemplo)}")


if __name__ == "__main__":
    main()
