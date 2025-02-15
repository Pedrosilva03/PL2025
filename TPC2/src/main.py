from Obra import Obra
import stats

filepath = 'data/obras.csv'

# Function that removes the line separators in the middle of the description and generates proper lines to be processed
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

# Function that removes the description and handles cases where it could be splitted by accident
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

def writer(sortedComposers, periodCount, musicPerPeriod):
    print(f'Compositores:')
    for composer in sortedComposers:
        print(composer)
    print("\n")

    print(f'Obras por período:')
    for period, count in periodCount.items():
        print(f'{period}: {count}')
    print("\n")

    print(f'Músicas por período:')
    for period, obras in musicPerPeriod.items():
        print(f'{period}: {obras}')
        print("---------------------")

def main():
    lista_obras = reader()

    sortedComposers = stats.sortComposers(lista_obras)
    periodCount = stats.countMusicByPeriod(lista_obras)
    musicPerPeriod = stats.musicByPeriod(lista_obras)

    writer(sortedComposers, periodCount, musicPerPeriod)

if __name__ == "__main__":
    main()