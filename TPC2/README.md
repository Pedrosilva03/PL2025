<h1 align="center">TPC2</h1>

## Autor
- Pedro Silva
- A100745

## Descrição
Dado um dataset sobre algumas obras artísticas, retirar as seguintes estatísticas:
- Lista ordenada alfabeticamente dos compositores musicais
- Distribuição das obras por período: quantas obras catalogadas em cada período
- Dicionário em que a cada período está a associada uma lista alfabética dos títulos das obras desse período

## Funcionamento
- Primeiramente o [dataset](https://github.com/Pedrosilva03/PL2025/blob/main/TPC2/data/obras.csv) é importado e analisado (sem recorrer ao módulo CSV)
- Os dados importantes acerca das obras são organizados e guardados em memória
- São criadas as estatísticas referidas
- O resultado é imprimido no ```stdout```
