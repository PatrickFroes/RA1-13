# Gabriel Antony: misfasol
# Patrick Froes: PatrickFroes
# Grupo: RA1-3

import os


def estado_numero_ponto(entrada: str, tokens: list[tuple[str, str | None]]) -> tuple[str, str]:
    resto = entrada[0] # o resto começa com "."
    entrada = entrada[1:]
    while True:
        if entrada[0].isdigit():
            resto = resto + entrada[0]
            entrada = entrada[1:]
        elif entrada[0] == " ":
            entrada = entrada[1:]
            break
        else:
            raise Exception("achou coisa que era pra ser numero mas nao era:", entrada)

    return entrada, resto

def estado_numero(entrada: str, tokens: list[tuple[str, str | None]]) -> str:
    numero = entrada[0]
    entrada = entrada[1:]
    while True:
        if entrada[0].isdigit():
            numero = numero + entrada[0]
            entrada = entrada[1:]
        elif entrada[0] == ".":
            entrada, resto = estado_numero_ponto(entrada, tokens)
            numero = numero + resto
            break
        elif entrada[0] == " ":
            entrada = entrada[1:]
            break
        else:
            raise Exception("achou coisa que era pra ser numero mas nao era:", entrada)
    tokens.append(("NUMERO", numero))

    return entrada

def estado_operador(entrada: str, tokens: list[tuple[str, str | None]]) -> str:
    if entrada[0] == "+":
        tokens.append(("OPERADOR", "+"))
        entrada = entrada[1:]
    elif entrada[0] == "-":
        tokens.append(("OPERADOR", "-"))
        entrada = entrada[1:]
    elif entrada[0] == "*":
        tokens.append(("OPERADOR", "*"))
        entrada = entrada[1:]
    elif entrada[0] == "/":
        if entrada[1] == "/":
            tokens.append(("OPERADOR", "//"))
            entrada = entrada[2:]
        else:
            tokens.append(("OPERADOR", "/"))
            entrada = entrada[1:]
    elif entrada[0] == "%":
        tokens.append(("OPERADOR", "%"))
        entrada = entrada[1:]
    elif entrada[0] == "^":
        tokens.append(("OPERADOR", "^"))
        entrada = entrada[1:]
    return entrada

def estado_identificador(entrada: str, tokens: list[tuple[str, str | None]]) -> str:
    identificador = ""
    while entrada and entrada[0].isalpha() and entrada[0].isupper():
        identificador += entrada[0]
        entrada = entrada[1:]
    
    if identificador == "RES":
        tokens.append(("COMANDO", "RES"))
    else:
        tokens.append(("VARIAVEL", identificador))
    
    return entrada

def estado_parenteses(entrada: str, tokens: list[tuple[str, str | None]]) -> str:
    # tem que ter parenteses
    tokens.append(("PAREN_ABRE", None))
    entrada = entrada[1:].lstrip()

    # a primeira coisa depois de um parenteses é um numero ou variavel ou outro parenteses
    # caso de variavel
    if entrada[0].isalpha():
        entrada = estado_identificador(entrada, tokens)
    # caso de outro parenteses
    # caso de numero ou outro parenteses
    elif entrada[0].isdigit() or entrada[0] == "(":
        if entrada[0] == "(":
            entrada = estado_parenteses(entrada, tokens)
        elif entrada[0].isdigit():
            entrada = estado_numero(entrada, tokens)
        else:
            pass # impossivel
        entrada = entrada.lstrip()

        # se ja tem um numero ou parenteses, a segunda coisa é um numero ou variavel/RES ou outro parentees
        # caso de variavel/RES
        if entrada[0].isalpha():
            entrada = estado_identificador(entrada, tokens)
        # caso de numero ou parenteses
        elif entrada[0].isdigit() or entrada[0] == "(":
            if entrada[0] == "(":
                entrada = estado_parenteses(entrada, tokens)
            elif entrada[0].isdigit():
                entrada = estado_numero(entrada, tokens)
            else:
                pass # impossivel
            entrada = entrada.lstrip()

                # se tem 2 numeros ou parenteses, o terceiro é um operador
            entrada = estado_operador(entrada, tokens)

    entrada = entrada.lstrip()
    # tem que terminar com um parenteses fechando
    if entrada[0] == ")":
        tokens.append(("PAREN_FECHA", None))
        entrada = entrada[1:]
    else:
        raise Exception("tem que terminar com parenteses fechando", entrada)

    return entrada

def parseExpressao(entrada: str, tokens: list[tuple[str, str | None]]):
    entrada = entrada.strip()
    match entrada[0]:
        case "(":
            resto = estado_parenteses(entrada, tokens)
            if resto.strip() != "":
                raise Exception("tem coisa depois do ultimo parentese:", resto)
        case _:
            raise Exception("devia ter parenteses no comeco da expressao:", entrada)

entrada = [
    "((1 22.2 +) ((3 VAR) (2 RES) *) //)",
    "(5.12 16.71 +)",
]

tokens: list[tuple[str, str | None]] = []
[parseExpressao(linha, tokens) for linha in entrada]

print(f"{entrada = }")
[print(t) for t in tokens]
