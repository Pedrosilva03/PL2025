from Obra import Obra

filepath = 'data/obras.csv'

# Função que une os dados que estavam separados por \n na descrição para que possam ser processados linha a linha
def splittedLinesProcess(splittedLines):
    processedLines = []

    currentLine = ""
    for splittedLine in splittedLines[1:]:
        if currentLine != "":
            currentLine += " " + splittedLine.strip()
        else:
            currentLine = splittedLine.strip()

        if splittedLine.split(";")[-1].startswith("O"):
            processedLines.append(currentLine)
            currentLine = ""

    return processedLines

def reader():
    lista_obras = []

    dataset = open(filepath, "r", encoding='utf-8')

    linhas = splittedLinesProcess(dataset.readlines())
    for linha in linhas:
        obra_data = linha.split(";") # Dar fix a isto (elemento extra)
        obra = Obra(*obra_data)
        lista_obras.append(obra)
        
    return lista_obras

def writer():
    pass

def main():
    lista_obras = reader()

if __name__ == "__main__":
    main()