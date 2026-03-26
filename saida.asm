.global _start
.arch armv7ve
.text
_start:

	mov r7, #0
	// numero 1
	ldr r0, =num_1
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// numero 1
	ldr r0, =num_1
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// +
	vpop {d0, d1}
	vadd.f64 d0, d1
	vpush {d0}
	sub r7, #1
	// terminou linha, printar ela
	vpop {d0}
	bl print_double
	vpush {d0}
	sub r7, #1
	// numero 1
	ldr r0, =num_1
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// res
	vpop {d0}
	vcvt.s32.f64 s0, d0
	vmov r0, s0
	add r0, r7
	sub r0, #2
	mov r1, #8
	mul r0, r1
	add r0, sp
	vldr d0, [r0]
	vpush {d0}
	// numero 2
	ldr r0, =num_2
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// ^
	vpop {d0, d1}
	bl meu_pow
	vpush {d0}
	sub r7, #1
	// terminou linha, printar ela
	vpop {d0}
	bl print_double
	vpush {d0}
	sub r7, #1
	// numero 1
	ldr r0, =num_1
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// res
	vpop {d0}
	vcvt.s32.f64 s0, d0
	vmov r0, s0
	add r0, r7
	sub r0, #2
	mov r1, #8
	mul r0, r1
	add r0, sp
	vldr d0, [r0]
	vpush {d0}
	// guardando valor da var: QUATRO
	vpop {d0}
	ldr r0, =var_QUATRO
	vstr d0, [r0]
	vpush {d0}
	// terminou linha, printar ela
	vpop {d0}
	bl print_double
	vpush {d0}
	sub r7, #1
	// pegar valor da var: QUATRO
	ldr r0, =var_QUATRO
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// numero 2
	ldr r0, =num_2
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// *
	vpop {d0, d1}
	vmul.f64 d0, d1, d0
	vpush {d0}
	sub r7, #1
	// terminou linha, printar ela
	vpop {d0}
	bl print_double
	vpush {d0}
	sub r7, #1
	// pegar valor da var: QUATRO
	ldr r0, =var_QUATRO
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// numero 1
	ldr r0, =num_1
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// -
	vpop {d0, d1}
	vsub.f64 d0, d1, d0
	vpush {d0}
	sub r7, #1
	// terminou linha, printar ela
	vpop {d0}
	bl print_double
	vpush {d0}
	sub r7, #1
	// pegar valor da var: QUATRO
	ldr r0, =var_QUATRO
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// numero 4.001
	ldr r0, =num_4_001
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// /
	vpop {d0, d1}
	vdiv.f64 d0, d1, d0
	vpush {d0}
	sub r7, #1
	// terminou linha, printar ela
	vpop {d0}
	bl print_double
	vpush {d0}
	sub r7, #1
	// numero 100
	ldr r0, =num_100
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// numero 3
	ldr r0, =num_3
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// //
	vpop {d0, d1}
	bl meu_div
	vpush {d0}
	sub r7, #1
	// terminou linha, printar ela
	vpop {d0}
	bl print_double
	vpush {d0}
	sub r7, #1
	// numero 100
	ldr r0, =num_100
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// numero 23
	ldr r0, =num_23
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// %
	vpop {d0, d1}
	bl meu_mod
	vpush {d0}
	sub r7, #1
	// terminou linha, printar ela
	vpop {d0}
	bl print_double
	vpush {d0}
	sub r7, #1
	// numero 1
	ldr r0, =num_1
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// numero 2.5
	ldr r0, =num_2_5
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// +
	vpop {d0, d1}
	vadd.f64 d0, d1
	vpush {d0}
	sub r7, #1
	// numero 1
	ldr r0, =num_1
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// numero 2.5
	ldr r0, =num_2_5
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// +
	vpop {d0, d1}
	vadd.f64 d0, d1
	vpush {d0}
	sub r7, #1
	// pegar valor da var: QUATRO
	ldr r0, =var_QUATRO
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// *
	vpop {d0, d1}
	vmul.f64 d0, d1, d0
	vpush {d0}
	sub r7, #1
	// /
	vpop {d0, d1}
	vdiv.f64 d0, d1, d0
	vpush {d0}
	sub r7, #1
	// terminou linha, printar ela
	vpop {d0}
	bl print_double
	vpush {d0}
	sub r7, #1
	// numero 99
	ldr r0, =num_99
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// numero 7
	ldr r0, =num_7
	vldr d0, [r0]
	vpush {d0}
	add r7, #1
	// /
	vpop {d0, d1}
	vdiv.f64 d0, d1, d0
	vpush {d0}
	sub r7, #1
	// terminou linha, printar ela
	vpop {d0}
	bl print_double
	vpush {d0}
	sub r7, #1
	// loop infinito
	b .

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

meu_div:
	vdiv.f64 d0, d1, d0
	vcvt.s32.f64 s4, d0
	vcvt.f64.s32 d1, s4
	vsub.f64 d1, d0, d1
	vsub.f64 d0, d0, d1
	bx lr

meu_mod:
	vmov.f64 d4, d0
	vmov.f64 d5, d1
	push {lr}
	bl meu_div
	pop {lr}
	vmul.f64 d0, d0, d4
	vsub.f64 d0, d5, d0
	bx lr

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

.data
// variaveis
var_QUATRO: .double 0

// numeros
num_7: .double 7
num_23: .double 23
num_3: .double 3
num_2_5: .double 2.5
num_99: .double 99
num_1: .double 1
num_2: .double 2
num_4_001: .double 4.001
num_100: .double 100
