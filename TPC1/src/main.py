import counter

input_path = 'in.txt'

def reader():
    str = open(input_path, 'r').read()
    return str

def writer(output):
    print(output)

def main():
    input = reader()
    writer(counter.count(input))

if __name__ == "__main__":
    main()