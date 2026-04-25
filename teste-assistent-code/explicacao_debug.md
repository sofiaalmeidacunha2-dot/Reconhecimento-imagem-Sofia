# Identificação e Correção de Erros em `debug.py`

Este arquivo documenta todos os erros encontrados no código original e as correções aplicadas.

## Erros Identificados

### 1. **Erro de Sintaxe - Aspas Faltantes (Linha 5)**

```python
# ERRO
item1 = float(input(Preço do item 1? ))

# CORRETO
item1 = float(input("Preço do item 1? "))
```

**Causa:** A string passada para `input()` não estava envolvida em aspas duplas. Python não consegue interpretar `Preço do item 1?` como uma string sem delimitadores.

**Impacto:** `SyntaxError` - o programa não executa.

---

### 2. **Erro de Tipo - String vs Float (Linha 21)**

```python
# ERRO
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# CORRETO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)
```

**Causa:** `input()` sempre retorna uma string. Ao tentar dividir uma string por 100 na linha 22, há um erro de tipo.

**Impacto:** `TypeError: unsupported operand type(s) for /: 'str' and 'int'`

---

### 3. **Erro de String Formatada - F-string Faltante (Linha 30)**

```python
# ERRO
print(" Item 2:        R$ {total_item2:.2f}")

# CORRETO
print(f" Item 2:        R$ {total_item2:.2f}")
```

**Causa:** A string não possui o prefixo `f`, então não é interpretada como uma f-string. Os chaves `{}` são exibidos como texto literalmente.

**Impacto:** Saída incorreta - exibe `{total_item2:.2f}` em vez do valor.

---

### 4. **Erro de Indentação (Linha 35-36)**

```python
# ERRO
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

# CORRETO
if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

**Causa:** O bloco `print()` não está indentado dentro do `if`. Em Python, a indentação é obrigatória para definir blocos de código.

**Impacto:** `IndentationError: expected an indented block`

---

### 5. **Erro de Tipo - Comparação com String (Linha 35)**

```python
# ERRO
if desconto_cupom > 0:  # desconto_cupom é string

# CORRETO
if desconto_cupom > 0:  # desconto_cupom agora é float (correção anterior)
```

**Causa:** Após a correção do erro 2, `desconto_cupom` é um `float`, permitindo a comparação com `0`.

**Impacto:** Sem a correção 2, haveria `TypeError: '>' not supported between instances of 'str' and 'int'`

---

## Resumo das Correções

| Linha | Erro | Tipo | Solução |
|-------|------|------|----------|
| 5 | `Preço do item 1?` sem aspas | Sintaxe | Adicionar aspas duplas |
| 21 | `input()` retorna string | Tipo | Converter com `float()` |
| 30 | F-string sem `f` | Formatação | Adicionar `f` antes da string |
| 35 | Indentação incorreta | Sintaxe | Indentar o `print()` |
| 35 | Comparar string com número | Tipo | Resolvido pela correção da linha 21 |

---

## Código Corrigido

O arquivo `debug.py` foi corrigido e agora funciona sem erros. O programa solicita dados do cliente, calcula totais e exibe um recibo formatado com cálculos de imposto e desconto.
