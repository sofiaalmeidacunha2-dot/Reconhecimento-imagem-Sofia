# Explicação do código `eh_primo`

Este arquivo descreve a versão refatorada de `num_primos.py`, com estilo mais limpo e legível.

## O que é um número primo?

Um número primo é um número natural maior que 1 que só pode ser dividido por 1 e por ele mesmo.

## Estrutura do código

O código foi dividido em duas funções:

- `eh_primo(numero: int) -> bool`
- `_tem_divisor_por_6k_mais_um(numero: int) -> bool`

A função `eh_primo` trata os casos simples e usa a função auxiliar para verificar outros possíveis divisores.

## Código refatorado

```python
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
    """Verifica divisores usando a forma 6k ± 1."""
    divisor = 5
    while divisor * divisor <= numero:
        if numero % divisor == 0 or numero % (divisor + 2) == 0:
            return True
        divisor += 6
    return False
```

## Como a função funciona

1. `numero <= 1`
   - Retorna `False`, pois 0 e 1 não são primos.
2. `numero <= 3`
   - Retorna `True` para 2 e 3.
3. `numero % 2 == 0 or numero % 3 == 0`
   - Elimina múltiplos de 2 e 3 rapidamente.
4. `return not _tem_divisor_por_6k_mais_um(numero)`
   - Verifica se existe um divisor válido maior que 3.

### Função auxiliar

A função `_tem_divisor_por_6k_mais_um` verifica apenas os divisores do tipo `6k - 1` e `6k + 1`, que são os candidatos relevantes para números maiores que 3.

- Começa em 5
- Avança em passos de 6
- Verifica `divisor` e `divisor + 2`
- Para quando `divisor * divisor` ultrapassa o número

## Exemplo de uso

```python
def main() -> None:
    exemplo = 29
    print(f"{exemplo} é primo? {eh_primo(exemplo)}")


if __name__ == "__main__":
    main()
```

Essa versão segue um estilo mais limpo, com nomes mais descritivos, tipagem simples e função principal separada para facilitar a leitura e a manutenção.
