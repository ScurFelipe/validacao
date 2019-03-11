processo_cnj = input("Digite o número do processo: ")
numero_sequecial = processo_cnj[0:7] # NNNNNNN
digito_verificador = processo_cnj[8:10] # DD
ano_do_ajuizamento = processo_cnj[11:15] # AAAA
poder_judiciario = processo_cnj[16] # J
tribunal_do_segmento = processo_cnj[18:20] # TR
unidade_de_origem = processo_cnj[21:25] # OOOO

Poder_Judiciario = {'1': 'Supremo Tribunal Federal',
                    '2': 'Conselho Nacional de Justiça',
                    '3': 'Superior Tribunal de Justiça',
                    '4': 'Justiça Federal',
                    '5': 'Justiça do Trablho',
                    '6': 'Justiça Eleitoral',
                    '7': 'Justiça Militar da União',
                    '8': 'Justiça dos Estados e do Distrito Federal e Territórios',
                    '9': 'Justiça Militar Estadual',
                    }

orgao = Poder_Judiciario.get(poder_judiciario)
print('Numero do Processo:', numero_sequecial)
print('Digito Verificador:', digito_verificador)
print('Ano do processo:', ano_do_ajuizamento)
print('Segmento do Poder Judiciário:', orgao)