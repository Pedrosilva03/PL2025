import converter

inFileName = "in/test1.md"
# Out file will be generated depending on the in file's name

def reader():
    inFile = open(inFileName, "r")
    return inFile.read()

def writer(convertedText):
    outFile = open(f'out/{inFileName[3:-3]}.html', "w") # Gets the name of the original file (removing the folder name and the format, which are consistent for any file name)
    outFile.write(convertedText)

def main():
    markdownText = reader()
    writer(converter.convert(markdownText))

if __name__ == "__main__":
    main()