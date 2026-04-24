# Explicação do código `eh_primo`

Este arquivo descreve o funcionamento da função `eh_primo` definida em `num_primos.py`, que verifica se um número inteiro é primo.

## O que é um número primo?

Um número primo é um número maior que 1 que só é divisível por 1 e por ele mesmo. Exemplos: 2, 3, 5, 7, 11.

## Funcionamento da função

```python
def eh_primo(n):
    """Retorna True se n for primo, caso contrário False."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

### Passo a passo

1. `if n <= 1: return False`
   - Números menores ou iguais a 1 não são primos.
2. `if n <= 3: return True`
   - Os números 2 e 3 são primos.
3. `if n % 2 == 0 or n % 3 == 0: return False`
   - Elimina rapidamente números pares e múltiplos de 3.
4. `i = 5`
   - Começa a verificar outros possíveis divisores a partir de 5.
5. `while i * i <= n:`
   - Não é preciso testar divisores maiores do que a raiz quadrada de `n`.
6. `if n % i == 0 or n % (i + 2) == 0: return False`
   - Verifica se `n` é divisível por `i` ou `i + 2`.
   - Isso usa o fato de que todos os primos maiores que 3 têm a forma `6k ± 1`.
7. `i += 6`
   - Avança para o próximo par de candidatos de forma eficiente.
8. `return True`
   - Se nenhum divisor foi encontrado, `n` é primo.

## Exemplo de uso

No bloco `if __name__ == "__main__":`, o código demonstra como chamar `eh_primo` e imprimir o resultado para um número de exemplo.

```python
if __name__ == "__main__":
    numero = 29
    print(f"{numero} é primo? {eh_primo(numero)}")
```

Essa explicação ajuda a entender a lógica e a otimização usada para verificar se um número é primo em Python.
