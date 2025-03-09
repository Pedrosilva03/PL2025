from ply import lex
import re

tokens = [
    'LISTAR',
    'MOEDA',
    'SELECIONAR',
    'SALDO',
    'ADICIONAR',
    'SAIR',
]

menu = """
        Bem-vindo à máquina de venda automática.
        Comandos disponíveis:
        - LISTAR
        - MOEDA <quantia>e e/ou <quantia>c
        - SELECIONAR <produto>  
        - SALDO
        - ADICIONAR <cod_produto> <quantidade>
        - SAIR
        """

def t_LISTAR(t):
    r'LISTAR'
    print("""maq:\ncod | nome | quantidade |  preço\n------------------------------------""")
    for produto in t.lexer.stock['stock']:
        print(f"{produto['cod']} | {produto['nome']} | {produto['quantidade']} | Preço: {produto['preco']}\n")
    return t

def t_MOEDA(t):
    r'MOEDA\s((2e|1e|50c|20c|10c|5c|2c|1c)(?:\s*,\s*(2e|1e|50c|20c|10c|5c|2c|1c))*)'  
    moedas = re.findall(r'(2e|1e|50c|20c|10c|5c|2c|1c)', t.value)
    for moeda in moedas:
        valor = re.findall(r'\d{1,2}', moeda)[0]
        currency = moeda[-1]
        if currency == 'c':
            t.lexer.saldo += round(int(valor) / 100,2)
        else:
            t.lexer.saldo += round(float(valor),2)
    t_SALDO(t)
    return t

def t_SELECIONAR(t):
    r'SELECIONAR\s\w+'
    cod = t.value.split()[1]
    for item in t.lexer.stock['stock']:
        if item['cod'] == cod:
            if t.lexer.saldo < item['preco']:
                print("Saldo insuficiente")
                break
            if item['quantidade'] > 0:
                item['quantidade']-= 1
                t.lexer.saldo -= item['preco']
            else:
                print("Produto esgotado")
            break
    else:
        print("Produto esgotado")
    t_SALDO(t)
    return t

def t_SALDO(t):
    r'SALDO'
    euros = round(int(t.lexer.saldo),2)
    cents = round(int((t.lexer.saldo - euros) * 100),2)
    print(f"maq: Saldo = {euros}e{cents}c")
    return t

def t_ADICIONAR(t):
    r'ADICIONAR\s\w+\s\w+'
    cod = t.value.split()[1]
    quantidade = t.value.split()[2]

    for item in t.lexer.stock['stock']:
        if item['cod'] == cod:
            item['quantidade'] += int(quantidade)
            print("Adicionado")
            break
    else:
        nome = input("Este é um novo produto. Insira o nome:")
        preco = int(input("Insira também o preço do produto:"))
        t.lexer.stock['stock'].append({"cod": cod, "nome": nome, "quantidade": int(quantidade), "preco": preco})
    return t

def t_SAIR(t):
    r'SAIR'
    moedas = {'2e': 0, '1e': 0, '50c': 0, '20c': 0, '10c': 0, '5c': 0, '2c': 0, '1c': 0}
    valores_moedas = {'2e': 2.00, '1e': 1.00, '50c': 0.50, '20c': 0.20, '10c': 0.10, '5c': 0.05, '2c': 0.02, '1c': 0.01}

    moedas_necessarias = []

    for moeda, valor in valores_moedas.items():
        quantidade = int(t.lexer.saldo // valor)
        moedas[moeda] = quantidade
        t.lexer.saldo -= quantidade * valor

        if quantidade > 0:
            for _ in range(quantidade):
                moedas_necessarias.append(moeda)
                
    print(f'Pode retirar o seu troco: {", ".join(moedas_necessarias)}')
    
    t.lexer.estado = 0
    return t

def t_error(t):
    t.lexer.skip(1)

def start(stock):
    lexer = lex.lex()

    lexer.stock = stock
    lexer.saldo = 0

    print(menu)

    lexer.estado = 1

    while lexer.estado != 0:
        lexer.input(input("Introduza uma opção:"))
        token = lexer.token()
        if not token:
            print("Comando inválido")

    return lexer.stock