import re

def count(input):
    tokens = re.findall(r'(on|off|=|-?\d+)', input, flags=re.IGNORECASE)

    somas = []
    soma_aux = 0
    behaviour = False
    for token in tokens:
        if token == '=':
            somas.append(soma_aux)
        elif token.lower() == 'on':
            behaviour = True
        elif token.lower() == 'off':
            behaviour = False
        else:
            if behaviour:
                soma_aux += int(token)
    return str(somas)