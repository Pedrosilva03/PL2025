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

def removeDesc(splittedLine):
    while len(splittedLine) > 6:
        del splittedLine[1]

    return splittedLine

def reader():
    lista_obras = []

    dataset = open(filepath, "r", encoding='utf-8')

    linhas = splittedLinesProcess(dataset.readlines())
    for linha in linhas:
        obra_data = linha.split(";")
        obra = Obra(*removeDesc(obra_data))
        lista_obras.append(obra)
        
    return lista_obras

def writer():
    pass

def main():
    lista_obras = reader()

if __name__ == "__main__":
    main()