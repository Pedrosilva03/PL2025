import parser

def main():
    rawLine = input("Enter line to be processed\n")
    
    if not rawLine:
        print("No valid line was detected")

    res = parser.parse(rawLine)

    print(f'{rawLine}\n\n{res}')

if __name__ == "__main__":
    main()