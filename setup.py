# Program used to set up all the folders and readmes because I like to try things and I am lazy to do it one by one

import os

numTpcs = 8

for i in range(numTpcs):
    os.makedirs(f'TPC{i + 1}', exist_ok=True)

    readmeContent = f"""<h1 align="center">TPC{i + 1}</h1>

## Autor
- Pedro Silva
- A100745

## Descrição

## Funcionamento
    """
    
    readmePath = os.path.join(f'TPC{i + 1}', "README.md")
    with open(readmePath, "w", encoding="utf-8") as f:
        f.write(readmeContent)
