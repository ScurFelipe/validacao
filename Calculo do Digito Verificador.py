processo_cnj = input("Digite o número do processo: ")
numero_sequecial = processo_cnj[0:7]
digito_verificador = processo_cnj[8:10]
ano_do_ajuizamento = processo_cnj[11:15]
poder_judiciario = processo_cnj[16]
tribunal_do_segmento = processo_cnj[18:20]
unidade_de_origem = processo_cnj[21:25]

#D1 D0 = 98 – (N6 N5 N4 N3 N2 N1 N0 A3 A2 A1 A0 J2 T1 R0 O3 O2 O1 O0 01 00 módulo 97)

parenteses = numero_sequecial + ano_do_ajuizamento + poder_judiciario + tribunal_do_segmento + unidade_de_origem + "00"
conta = 98 - (int(parenteses) % 97)
string_conta = str(conta).zfill(2) 

if digito_verificador == string_conta:
    print('Número de Processo Válido')
else:
    print('Número de Processo Inválido')  

print('Numero do Processo:', numero_sequecial)
print('Digito Verificador:', digito_verificador)
print('Ano do processo:', ano_do_ajuizamento)