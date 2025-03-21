<h1 align="center">TPC6</h1>

## Autor
- Pedro Silva
- A100745

## Descrição
Analisador léxico e sintático para expressões aritméticas
- Avaliar lexicalmente e sintaticamente as expressões
- Calcular o seu valor

## Funcionamento
O programa é de execução única:

### Leitura de input
- O input é uma expressão aritmética a ser avaliada
- As expressões podem ser de vários tipos:
```
-> 2+3
-> 67-(2+3*4)
-> (9-2)*(13-4)
-> (9+2-3)*(12/4)
-> (9/3-2)*(13-4)
-> 2*(3+4)
-> 14/2+3*4
-> (2*3)*(4/1)+(12/4*3)
```

### Análise léxica
- O programa lê os operadores e transforma-os em tokens bem definidos:
- - Operadores
  - Parêntises
  - Números
```
Entrada: 3 + 5 * (2 - 1)
Tokens:  [NUMBER, PLUS, NUMBER, TIMES, LPAREN, NUMBER, MINUS, NUMBER, RPAREN]
```

### Análise sintática
- O programa constrói uma árvore de derivação para analisar a expressão
- A gramática é definida e utilizada para análise:
```
Rule 0     S' -> expression
Rule 1     expression -> expression PLUS term
Rule 2     expression -> expression MINUS term
Rule 3     expression -> term
Rule 4     term -> term TIMES factor
Rule 5     term -> term DIVIDE factor
Rule 6     term -> factor
Rule 7     factor -> NUMBER
Rule 8     factor -> LPAREN expression RPAREN
```

### Resultado
O resultado é imprimido na tela e o programa fecha
