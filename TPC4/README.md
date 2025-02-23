<h1 align="center">TPC4</h1>

## Autor
- Pedro Silva
- A100745

## Descrição
O objetivo é construir um analizador léxico para uma linguagem de queries
- Podem ser escritas frases do seguinte tipo
```
# DBPedia: obras de Chuck Berry
SELECT ?nome ?desc WHERE {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```

## Funcionamento
- O programa divide a frase de input por tokens e analiza-os da seguinte forma:
   - **Palavras-chave**: `SELECT`, `WHERE`, `LIMIT`
   - **Variáveis**: `?s`, `?nome`, `?desc`
   - **Prefixos RDF**: `dbo:MusicalArtist`, `foaf:name`
   - **Strings com idioma**: `"Chuck Berry"@en`
   - **Símbolos de estrutura**: `{ } .`
   - **Comentários**: `# ...`
- Imprime no terminal o resultado da análise
    
