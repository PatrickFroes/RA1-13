# Gabriel Antony: misfasol
# Patrick Froes: PatrickFroes
# Grupo: RA1-3

import os


def numero_ponto(entrada: str, tokens: list[tuple[str, str | None]]) -> tuple[str, str]:
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
            entrada, resto = numero_ponto(entrada, tokens)
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

def gerarAssembly(tokens: list[tuple[str, str | None]]) -> str:
    variaveis: set[str] = set()
    numeros: set[str] = set()

    for (tipo, valor) in tokens:
        if tipo == "NUMERO":
            if valor is None:
                raise Exception("valor e None", valor)
            numeros.add(valor)
        elif tipo == "VARIAVEL":
            if valor is None:
                raise Exception("valor e None", valor)
            variaveis.add(valor)
        
    # print(variaveis)
    # print(numeros)
    
    saida = open("saida.s", "w")

    saida.write(".global _start\n.arch armv7ve\n.text\n_start:\n\n")
    saida.write("\tmov r7, #0\n")

    qtd_paren = 0
    ult_tok = ("", "")
    for (tipo, valor) in tokens:
        match tipo:
            case "PAREN_ABRE":
                qtd_paren += 1

            case "PAREN_FECHA":
                qtd_paren -= 1
                if qtd_paren == 0:
                    saida.write("\t// terminou linha, printar ela\n")
                    saida.write("\tvpop {d0}\n")
                    saida.write("\tbl print_double\n")
                    saida.write("\tvpush {d0}\n")
                    saida.write("\tsub r7, #1\n")

            case "NUMERO":
                if valor is None:
                    print(f"{valor} é None")
                    os._exit(1)
                saida.write(f"\t// numero {valor}\n")
                saida.write(f"\tldr r0, =num_{valor.replace(".", "_")}\n")
                saida.write(f"\tvldr d0, [r0]\n")
                saida.write("\tvpush {d0}\n")
                saida.write("\tadd r7, #1\n")

            case "COMANDO":
                match valor:
                    case "RES":
                        saida.write(f"\t// res\n")
                        saida.write("\tvpop {d0}\n")
                        saida.write("\tvcvt.s32.f64 s0, d0\n")
                        saida.write("\tvmov r0, s0\n") # r0 tem qnt linhas pra tras a gnt quer
                        saida.write("\tadd r0, r7\n")
                        saida.write("\tsub r0, #2\n")
                        saida.write("\tmov r1, #8\n")
                        saida.write("\tmul r0, r1\n")
                        saida.write("\tadd r0, sp\n")
                        saida.write("\tvldr d0, [r0]\n")
                        saida.write("\tvpush {d0}\n")

            case "VARIAVEL":
                if ult_tok[0] == "PAREN_ABRE":
                    # pegando valor da var
                    saida.write(f"\t// pegar valor da var: {valor}\n")
                    saida.write(f"\tldr r0, =var_{valor}\n")
                    saida.write(f"\tvldr d0, [r0]\n")
                    saida.write("\tvpush {d0}\n")
                    saida.write("\tadd r7, #1\n")
                else:
                    # guardando valor
                    saida.write(f"\t// guardando valor da var: {valor}\n")
                    saida.write("\tvpop {d0}\n")
                    saida.write(f"\tldr r0, =var_{valor}\n")
                    saida.write(f"\tvstr d0, [r0]\n")
                    saida.write("\tvpush {d0}\n")

            case "OPERADOR":
                match valor:
                    case "+":
                        saida.write("\t// +\n")
                        saida.write("\tvpop {d0, d1}\n")
                        saida.write("\tvadd.f64 d0, d1\n")
                        saida.write("\tvpush {d0}\n")
                        saida.write("\tsub r7, #1\n")

                    case "-":
                        saida.write("\t// -\n")
                        saida.write("\tvpop {d0, d1}\n")
                        saida.write("\tvsub.f64 d0, d1, d0\n")
                        saida.write("\tvpush {d0}\n")
                        saida.write("\tsub r7, #1\n")
                        
                    case "*":
                        saida.write("\t// *\n")
                        saida.write("\tvpop {d0, d1}\n")
                        saida.write("\tvmul.f64 d0, d1, d0\n")
                        saida.write("\tvpush {d0}\n")
                        saida.write("\tsub r7, #1\n")

                    case "/":
                        saida.write("\t// /\n")
                        saida.write("\tvpop {d0, d1}\n")
                        saida.write("\tvdiv.f64 d0, d1, d0\n")
                        saida.write("\tvpush {d0}\n")
                        saida.write("\tsub r7, #1\n")
                        
                    case "//":
                        saida.write("\t// //\n")
                        saida.write("\tvpop {d0, d1}\n")
                        saida.write("\tbl meu_div\n")
                        saida.write("\tvpush {d0}\n")
                        saida.write("\tsub r7, #1\n")

                    case "%":
                        saida.write("\t// %\n")
                        saida.write("\tvpop {d0, d1}\n")
                        saida.write("\tbl meu_mod\n")
                        saida.write("\tvpush {d0}\n")
                        saida.write("\tsub r7, #1\n")

                    case "^":
                        saida.write("\t// ^\n")
                        saida.write("\tvpop {d0, d1}\n")
                        saida.write("\tbl meu_pow\n")
                        saida.write("\tvpush {d0}\n")
                        saida.write("\tsub r7, #1\n")
                        
                    case _:
                        print(f"operador ainda não suportado: {valor}")
                        os._exit(1)
        ult_tok = (tipo, valor)
    saida.write("\t// loop infinito\n")
    saida.write("\tb .\n")

    # funcao de printar double, recebe em d0
    saida.write("""
print_double:
	push {r4}
	push {r5}
	push {r6}
	// char[64]
	sub sp, #64
	// int neg = (v < 0); // r0
	vcmp.f64 d0, #0
	vmrs APSR_nzcv, FPSCR
	mov r0, #0
	movlt r0, #1
	// if (neg) v *= -1;
	mov r1, #-1
	vmov s9, r1
	vcvt.f64.s32 d1, s9
	cmp r0, #1
	vmuleq.f64 d0, d1
	// unsigned long inteiro = (unsigned long)v // r1
	vcvt.s32.f64 s9, d0
	vmov r1, s9
	// double razao = v - inteiro; // d1
	vcvt.f64.s32 d1, s9
	vsub.f64 d1, d0, d1
	// int i = 18; // r2
	mov r2, #18
	// char ult; // r3
	mov r3, #0
	
	// for (int ind = 0; ind < 63; ind++) buf[ind] = ' ';
	mov r4, #0 // ind
	mov r5, sp // index no buffer
	mov r6, #0 // buf[63] = 0;
	strb r6, [r5, #63]
	mov r6, #' ' // lit
print_limpar:
	strb r6, [r5]
	add r5, #1
	add r4, #1
	cmp r4, #63
	blt print_limpar
	// while (1) {
prim_loop:
	// ult = inteiro % 10;
	mov r3, r1
	mov r5, #10
	sdiv r4, r3, r5
	mls r3, r5, r4, r3
	// buf[i] = ult + '0';
	mov r4, sp // indice no buffer
	add r4, r2
	add r3, #'0'
	strb r3, [r4]
	// i -= 1;
	sub r2, #1
	// inteiro /= 10;
	mov r4, #10
	sdiv r1, r4
	// if ((inteiro == 0) || (i < 0)) break;
	cmp r1, #0
	beq saida_prim_loop
	cmp r2, #0
	blt saida_prim_loop
	b prim_loop
saida_prim_loop:
	// buf[19] = '.';
	mov r4, sp
	add r4, #19
	mov r5, #'.'
	strb r5, [r4]
	// if (neg) buf[i] = '-';
	cmp r0, #1
	mov r5, #' '
	moveq r5, #'-'
	mov r6, sp
	add r6, r2
	strb r5, [r6]
	// i = 20;
	mov r2, #20;
	// while (1)
seg_loop:
	// razao *= 10;
	mov r4, #10
	vmov s10, r4
	vcvt.f64.s32 d2, s10
	vmul.f64 d1, d2
	// ult = (int)razao;
	vcvt.s32.f64 s9, d1
	vmov r3, s9
	// buf[i] = ult + '0';
	mov r4, sp
	add r4, r2
	add r5, r3, #'0'
	strb r5, [r4]
	// razao -= ult;
	vmov s9, r3
	vcvt.f64.s32 d2, s9
	vsub.f64 d1, d2
	// i += 1;
	add r2, #1
	// if (i > 34) break;
	cmp r2, #34
	bgt saida_seg_loop
	b seg_loop
saida_seg_loop:
	// print(buf)
	sub sp, #12
	mov r0, #0
	str r0, [sp]
	mov r0, sp
	add r0, #12
	str r0, [sp, #4]
	mov r0, #64
	str r0, [sp, #8]
	mov r0, #5
	mov r1, sp
	svc #0x123456
	add sp, #12
	add sp, #64 // liberar bufer
	pop {r6}
	pop {r5}
	pop {r4}
	bx lr // return
""")

    # funcao div de inteiro
    # recebe x em d1, y em d0
    saida.write("""
meu_div:
	vdiv.f64 d0, d1, d0
	vcvt.s32.f64 s4, d0
	vcvt.f64.s32 d1, s4
	vsub.f64 d1, d0, d1
	vsub.f64 d0, d0, d1
	bx lr
""")
    # funcao mod
    # x - (y * (x // y))
    # recebe x em d1, y em d0
    saida.write("""
meu_mod:
	vmov.f64 d4, d0
	vmov.f64 d5, d1
	push {lr}
	bl meu_div
	pop {lr}
	vmul.f64 d0, d0, d4
	vsub.f64 d0, d5, d0
	bx lr
""")
    # funcao pow
    # recebe x em d1, y em d0
    saida.write("""
meu_pow:
	vcvt.s32.f64 s4, d0
	vmov r0, s4
	vmov.f64 d0, d1
loop_meu_pow:
	cmp r0, #1
	beq saida_meu_pow
	vmul.f64 d0, d0, d1
	sub r0, #1
	b loop_meu_pow
saida_meu_pow:
	bx lr
""")
    
    saida.write("\n.data\n")

    saida.write("// variaveis\n")
    for var in variaveis:
        saida.write(f"var_{var}: .double 0\n")
    saida.write("\n")
    
    saida.write("// numeros\n")
    for numero in numeros:
        saida.write(f"num_{numero.replace(".", "_")}: .double {numero}\n")
    
    saida.close()

    arq = open("saida.s", "r")
    ass = arq.read()
    arq.close()
    return ass

entrada = [
    "((2.5 1.0 -) 0.75 *)",
    "(22 7 /)",
    "(5 2 //)",
    "(10 4 %)",
    "(1.1 5 ^)",
    "(4 RES)",
    "(1 VAR)",
    "(VAR)",
    "(1.5 VAR)",
    "(VAR)",
    "((5 RES) ANT)",
    "((ANT) 1.86 +)",
    "(122 1 +)",
    "(543 (1 RES) +)",
]

tokens: list[tuple[str, str | None]] = []
[parseExpressao(linha, tokens) for linha in entrada]

print(f"{entrada = }")
[print(t) for t in tokens]
print()

assembly = gerarAssembly(tokens)
print("assembly:", assembly, sep="\n")
