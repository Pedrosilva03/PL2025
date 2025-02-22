<h1 align="center">TPC3</h1>

## Autor
- Pedro Silva
- A100745

## Descrição
O objetivo é, dado um ficheiro MD, converter para um ficheiro HTML segundo as seguintes instruções.

- Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"
```
  In: # Exemplo
  Out: <h1>Exemplo</h1>
```
- Bold: pedaços de texto entre "**":
```
  In: Este é um **exemplo** ...
  Out: Este é um <b>exemplo</b> ...
```
- Itálico: pedaços de texto entre "*":
```
  In: Este é um *exemplo* ...
  Out: Este é um <i>exemplo</i> ...
```
- Lista numerada:
```
  In:
    1. Primeiro item
    2. Segundo item
    3. Terceiro item

  Out:
    <ol>
      <li>Primeiro item</li>
      <li>Segundo item</li>
      <li>Terceiro item</li>
    </ol>
```
- Link: [texto](endereço URL)
```
  In: Como pode ser consultado em [página da UC](http://www.uc.pt)
  Out: Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>
```
- Imagem: ![texto alternativo](path para a imagem)
```
  In: Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ...
  Out: Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...
```

## Funcionamento
- O programa importa um ficheiro da pasta [in](https://github.com/Pedrosilva03/PL2025/tree/main/TPC3/in) e faz a sua leitura.
- Efetua a sua conversão usando expressões regulares para substituir os carateres de Markdown para carateres HTML.
- Escreve o texto convertido num ficheiro HTML.
- Coloca o resultado final na pasta [out](https://github.com/Pedrosilva03/PL2025/tree/main/TPC3/out).
    
