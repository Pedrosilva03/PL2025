<h1 align="center">TPC5</h1>

## Autor
- Pedro Silva
- A100745

## Descrição

Uma máquina de vendas onde os utilizadores podem introduzir moedas, listar, comprar e adicionar produtos, e obter troco.
São disponibilizados os seguintes comandos:
- ```LISTAR``` Mostra todo o stock da máquina (código, nome, quantidade e preço)
- ```MOEDA <moeda1> <moeda2> ...``` Adiciona uma ou mais moedas à máquina junto com o tipo da moeda (```EXEMPLO: MOEDA 1e 20c 10c``` => Uma moeda de 1 euro, uma moeda de 20 cêntimos e uma moeda de 10 cêntimos)
- ```SELECIONAR <cod_produto>``` Seleciona um produto para compra
- ```SALDO``` Mostra o saldo atual dentro da máquina
- ```ADICIONAR <cod_produto> <quantidade>``` Permite repor stock de um produto caso o ```<cod_produto>``` já exista ou adicionar um produto novo caso não exista
- ```SAIR``` Devolve o troco ao utilizador e desliga a máquina
Estes comandos são também mostrados e explicados ao iniciar a máquina.

## Funcionamento

O programa deve ser executado com o comando ```python main.py <caminho para o ficheiro de stock>```
- O programa carrega o stock da máquina de um ficheiro ```.json``` parecido com [este](https://github.com/Pedrosilva03/PL2025/blob/main/TPC5/stock/stock.json), que deve ser passado como argumento
- Apresenta um menu inicial com instruções para a utilização da máquina
- Processa comandos introduzidos pelo utilizador de acordo com as instruções apresentadas
- Após o pedido de saída, atualiza o ficheiro de stock com o novo estado da máquina e coloca-o novamente no local inicialmente passado como argumento
