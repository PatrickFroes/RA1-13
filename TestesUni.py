import sys
from ParseEXP import parseExpressao

#teste para numero
def testar_numeros():
    casos = [
        "(5 3 +)",
        "(3.14 2.0 +)",
        "(0.5 2 *)",
    ]
    invalidos = [
        "(3.14.5 2.0 +)",
    ]
    
    passou = 0
    todos = len(casos) + len(invalidos)
    
    for expr in casos:
        tokens = []
        try:
            parseExpressao(expr, tokens)
            print(f"OK - {expr}")
            passou += 1
        except:
            print(f"ERRO - {expr}")
    
    for expr in invalidos:
        tokens = []
        try:
            parseExpressao(expr, tokens)
            print(f"ERRO - {expr}")
        except:
            print(f"OK - {expr}")
            passou += 1
    
    return passou, todos

#teste para operadores( um para cada tipo)
def testar_operadores():
    casos = [
        "(1 2 +)",
        "(5 3 -)",
        "(4 5 *)",
        "(10 2 /)",
        "(5 2 //)",
        "(10 3 %)",
        "(2 3 ^)"
    ]
    
    passou = 0
    for expr in casos:
        tokens = []
        try:
            parseExpressao(expr, tokens)
            if any(t[0] == "OPERADOR" for t in tokens):
                print(f"OK - {expr}")
                passou += 1
            else:
                print(f"ERRO - {expr}")
        except:
            print(f"ERRO - {expr}")
    
    return passou, len(casos)

#teste de parenteses
def testar_parenteses():
    casos = [
        "(1 2 +)",
        "((1 2 +) 3 *)",
        "(((1 2 +) 3 *) 4 -)",
    ]
    invalidos = [
        "(1 2 +",
        "1 2 +)",
    ]
    
    passou = 0
    todos = len(casos) + len(invalidos)
    
    for expr in casos:
        tokens = []
        try:
            parseExpressao(expr, tokens)
            print(f"OK - {expr}")
            passou += 1
        except:
            print(f"ERRO - {expr}")
    
    for expr in invalidos:
        tokens = []
        try:
            parseExpressao(expr, tokens)
            print(f"ERRO - {expr}")
        except:
            print(f"OK - {expr}")
            passou += 1
    
    return passou, todos

#teste para os comandos  requisitados
def testar_variaveis_comandos():
    casos = [
        ("(5 RES)", "RES"),
        ("(VAR 2 +)", "VAR"),
        ("(QUATRO 2 *)", "QUATRO"),
        ("((1 RES) QUATRO)", "QUATRO"),
    ]
    
    passou = 0
    for expr, token_esperado in casos:
        tokens = []
        try:
            parseExpressao(expr, tokens)
            if any(token_esperado in str(t) for t in tokens):
                print(f"OK - {expr}")
                passou += 1
            else:
                print(f"ERRO - {expr}")
        except:
            print(f"ERRO - {expr}")
    
    return passou, len(casos)

#teste completo
def testar_completos():
    casos = [
        "((1.5 2.0 *) (3.0 4.0 *) /)",
        "((1 2 +) 3 *)",
        "(((A B +) C *) D -)",
    ]
    
    passou = 0
    for expr in casos:
        tokens = []
        try:
            parseExpressao(expr, tokens)
            if len(tokens) > 0:
                print(f"OK - {expr}")
                passou += 1
            else:
                print(f"ERRO - {expr}")
        except:
            print(f"ERRO - {expr}")
    
    return passou, len(casos)

#teste de formato de token
def testar_formato_token():
    linha = "(1 2 +)"
    tokens = []
    parseExpressao(linha, tokens)
    
    certo = [
        ("PAREN_ABRE", None),
        ("NUMERO", "1"),
        ("NUMERO", "2"),
        ("OPERADOR", "+"),
        ("PAREN_FECHA", None)
    ]
    
    passou = 0
    for expr in [linha]:
        try:
            if tokens == certo:
                print(f"OK - {expr}")
                passou += 1
            else:
                print(f"ERRO - {expr}")
        except:
            print(f"ERRO - {expr}")
    
    return passou, 1



if __name__ == "__main__":
    
    p1, t1 = testar_numeros()
    print(f"Números: {p1}/{t1}\n")
    
    p2, t2 = testar_operadores()
    print(f"Operadores: {p2}/{t2}\n")
    
    p3, t3 = testar_parenteses()
    print(f"Parênteses: {p3}/{t3}\n")
    
    p4, t4 = testar_variaveis_comandos()
    print(f"Variáveis/Comandos: {p4}/{t4}\n")
    
    p5, t5 = testar_completos()
    print(f"Completos: {p5}/{t5}\n")
    
    p6, t6 = testar_formato_token()
    print(f"Formato de Tokens: {p6}/{t6}\n")
    
    total = p1 + p2 + p3 + p4 + p5 + p6
    total_testes = t1 + t2 + t3 + t4 + t5 + t6
    print(f"TOTAL: {total}/{total_testes}")
