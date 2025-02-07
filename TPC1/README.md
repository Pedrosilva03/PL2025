<h1 align="center">TPC1</h1>

## Autor
- Pedro Silva
- A100745

## Descrição

O objetivo é, dado um texto com vários tokens do tipo ```número || on || off || = || ou outro tipo de texto```, efetuar as seguintes operações:
- Somar todos os números encontrados dependendo do estado do switch
- Se o switch for ```on``` a soma está ligada
- Se o switch for ```off``` a soma está desligada
- Ao encontrar um ```=``` a soma é imprimida

## Funcionamento

- O programa lê o ficheiro [in](https://github.com/Pedrosilva03/PL2024/tree/main/TP3/in). A leitura a partir de um ficheiro facilita o teste com inputs maiores
- Procura por todas as ocorrências de números, switches ou ```=``` e coloca-as numa lista
- Corre essa lista e dependendo do estado do switch, efetua somas
- A cada ```=```, vai colocando a soma acumulada até ao momento numa lista
- Por fim essa lista é convertida para string e o resultado é escrito no ```stdout````
    