processo_cnj = input("Digite o número do processo: ")
#NNNNNNN-DD.AAAA.J.TR.OOOO
#Associação a uma variável.
NNNNNNN = processo_cnj[0:7]
DD = processo_cnj[8:10]
AAAA = processo_cnj[11:15]
J_TR = processo_cnj[16:20]
OOOO = processo_cnj[21:25]
JTR_OOOO = processo_cnj[16:25]

#Numero de Processos nos Órgãos do Poder Judiciário
entidade_maior = {'1.00.0000': 'Supremo Tribunal Federal',
                  '2.00.0000': 'Conselho Nacional de Justiça',
                  '3.00.0000': 'Superior Tribunal de Justiça',
                  '4.90.0000': 'Conselho de Justiça Federal',
                  '4.01.0000': 'Tribunal Regional Federal da 1ª Região',
                  '4.02.0000': 'Tribunal Regional Federal da 2ª Região',
                  '4.03.0000': 'Tribunal Regional Federal da 3ª Região',
                  '4.04.0000': 'Tribunal Regional Federal da 4ª Região',
                  '4.05.0000': 'Tribunal Reguinal Federal da 5ª Região',
                  '4.01.9001': 'Turma Recursal do TRF da 1ª Região',
                  '4.02.9001': 'Turma Recursal do TRF da 2ª Região',
                  '4.03.9001': 'Turma Recursal do TRF da 3ª Região',
                  '4.04.9001': 'Turma Recursal do TRF da 4ª Região',
                  '4.05.9001': 'Turma Recursal do TRF da 5ª Região',
                  '4.01.0010': 'Subseções Judiciarias do TRF da 1ª Região',
                  '4.02.0010': 'Subseções Judiciarias do TRF da 2ª Região',
                  '4.03.0010': 'Subseções Judiciarias do TRF da 3ª Região',
                  '4.04.0010': 'Subseções Judiciarias do TRF da 4ª Região',
                  '4.05.0010': 'Subseções Judiciarias do TRF da 5ª Região',
                  '5.00.0000': 'Tribunal Superior do Trabalho',
                  '5.90.0000': 'Conselho Superior da Justiça do Trabalho',
                  '5.01.0000': '1ª Tribunal Regional do Trabalho',
                  '5.02.0000': '2ª Tribunal Regional do Trabalho',
                  '5.03.0000': '3ª Tribunal Regional do Trabalho',
                  '5.04.0000': '4ª Tribunal Regional do Trabalho',
                  '5.05.0000': '5ª Tribunal Regional do Trabalho',
                  '5.06.0000': '6ª Tribunal Regional do Trabalho',
                  '5.07.0000': '7ª Tribunal Regional do Trabalho',
                  '5.08.0000': '8ª Tribunal Regional do Trabalho',
                  '5.09.0000': '9ª Tribunal Regional do Trabalho',
                  '5.10.0000': '10ª Tribunal Regional do Trabalho',
                  '5.11.0000': '11ª Tribunal Regional do Trabalho',
                  '5.12.0000': '12ª Tribunal Regional do Trabalho',
                  '5.13.0000': '13ª Tribunal Regional do Trabalho',
                  '5.14.0000': '14ª Tribunal Regional do Trabalho',
                  '5.15.0000': '15ª Tribunal Regional do Trabalho',
                  '5.16.0000': '16ª Tribunal Regional do Trabalho',
                  '5.17.0000': '17ª Tribunal Regional do Trabalho',
                  '5.18.0000': '18ª Tribunal Regional do Trabalho',
                  '5.19.0000': '19ª Tribunal Regional do Trabalho',
                  '5.20.0000': '20ª Tribunal Regional do Trabalho',
                  '5.21.0000': '21ª Tribunal Regional do Trabalho',
                  '5.22.0000': '22ª Tribunal Regional do Trabalho',
                  '5.23.0000': '23ª Tribunal Regional do Trabalho',
                  '5.24.0000': '24ª Tribunal Regional do Trabalho',
                  '5.01.0197': 'Vara do Trabalho do TRT da 1ª Região',
                  '5.02.0197': 'Vara do Trabalho do TRT da 2ª Região',
                  '5.03.0197': 'Vara do Trabalho do TRT da 3ª Região',
                  '5.04.0197': 'Vara do Trabalho do TRT da 4ª Região',
                  '5.05.0197': 'Vara do Trabalho do TRT da 5ª Região',
                  '5.06.0197': 'Vara do Trabalho do TRT da 6ª Região',
                  '5.07.0197': 'Vara do Trabalho do TRT da 7ª Região',
                  '5.08.0197': 'Vara do Trabalho do TRT da 8ª Região',
                  '5.09.0197': 'Vara do Trabalho do TRT da 9ª Região',
                  '5.10.0197': 'Vara do Trabalho do TRT da 10ª Região',
                  '5.11.0197': 'Vara do Trabalho do TRT da 11ª Região',
                  '5.12.0197': 'Vara do Trabalho do TRT da 11ª Região',
                  '5.13.0197': 'Vara do Trabalho do TRT da 13ª Região',
                  '5.14.0197': 'Vara do Trabalho do TRT da 14ª Região',
                  '5.15.0197': 'Vara do Trabalho do TRT da 15ª Região',
                  '5.16.0197': 'Vara do Trabalho do TRT da 16ª Região',
                  '5.17.0197': 'Vara do Trabalho do TRT da 17ª Região',
                  '5.18.0197': 'Vara do Trabalho do TRT da 18ª Região',
                  '5.19.0197': 'Vara do Trabalho do TRT da 19ª Região',
                  '5.20.0197': 'Vara do Trabalho do TRT da 20ª Região',
                  '5.21.0197': 'Vara do Trabalho do TRT da 21ª Região',
                  '5.22.0197': 'Vara do Trabalho do TRT da 22ª Região',
                  '5.23.0197': 'Vara do Trabalho do TRT da 23ª Região',
                  '5.24.0197': 'Vara do Trabalho do TRT da 24ª Região',
                  '6.00.0000': 'Tribunal Superior Eleitoral',
                  '6.01.0000': 'Tribunal Regional Eleitoral do Acre',
                  '6.02.0000': 'Tribunal Regional Eleitoral de Alagoas',
                  '6.03.0000': 'Tribunal Regional Eleitoral do Amapá',
                  '6.04.0000': 'Tribunal Regional Eleitoral do Amazonas',
                  '6.05.0000': 'Tribunal Regional Eleitoral da Bahia',
                  '6.06.0000': 'Tribunal Regional Eleitoral do Ceará',
                  '6.07.0000': 'Tribunal Regional Eleitoral do Distrito Federal e Territórios',
                  '6.08.0000': 'Tribunal Regional Eleitoral do Espirito Santo',
                  '6.09.0000': 'Tribunal Regional Eleitoral de Goiás',
                  '6.10.0000': 'Tribunal Regional Eleitoral do Maranhão',
                  '6.11.0000': 'Tribunal Regional Eleitoral do Mato Grosso',
                  '6.12.0000': 'Tribunal Regional Eleitoral do Mato Grosso do Sul',
                  '6.13.0000': 'Tribunal Regional Eleitoral de Minas Gerais',
                  '6.14.0000': 'Tribunal Regional Eleitoral do Pará',
                  '6.15.0000': 'Tribunal Regional Eleitoral da Paraíba',
                  '6.16.0000': 'Tribunal Regional Eleitoral do Paraná',
                  '6.17.0000': 'Tribunal Regional Eleitoral do Pernambuco',
                  '6.18.0000': 'Tribunal Regional Eleitoral do Piauí',
                  '6.19.0000': 'Tribunal Regional Eleitoral do Rio de Janeiro',
                  '6.20.0000': 'Tribunal Regional Eleitoral do Rio Grande do Norte',
                  '6.21.0000': 'Tribunal Regional Eleitoral do Rio Grande do Sul',
                  '6.22.0000': 'Tribunal Regional Eleitoral de Rondônia',
                  '6.23.0000': 'Tribunal Regional Eleitoral de Roraima',
                  '6.24.0000': 'Tribunal Regional Eleitoral de Santa Catarina',
                  '6.25.0000': 'Tribunal Regional Eleitoral de Sergipe',
                  '6.26.0000': 'Tribunal Regional Eleitoral de São Paulo',
                  '6.27.0000': 'Tribunal Regional Eleitoral do Tocantins',
                  '6.01.0342': 'Zona Eleitoral do Acre',
                  '6.02.0342': 'Zona Eleitoral do Alagoas',
                  '6.03.0342': 'Zona Eleitoral do Amapá',
                  '6.04.0342': 'Zona Eleitoral do Amazonas',
                  '6.05.0342': 'Zona Eleitoral da Bahia',
                  '6.06.0342': 'Zona Eleitoral do Ceará',
                  '6.07.0342': 'Zona Eleitoral do Distrito Federal e Teritórios',
                  '6.08.0342': 'Zona Eleitoral do Espirito Santo',
                  '6.09.0342': 'Zona Eleitoral de Goiás',
                  '6.10.0342': 'Zona Eleitoral do  Maranhão',
                  '6.11.0342': 'Zona Eleitoral do Mato Grosso ',
                  '6.12.0342': 'Zona Eleitoral do  Mato Grosso do Sul',
                  '6.13.0342': 'Zona Eleitoral de Minas Gerais',
                  '6.14.0342': 'Zona Eleitoral do Pará',
                  '6.15.0342': 'Zona Eleitoral da Paraíba',
                  '6.16.0342': 'Zona Eleitoral do Paraná',
                  '6.17.0342': 'Zona Eleitoral do Pernambuco',
                  '6.18.0342': 'Zona Eleitoral do Piauí',
                  '6.19.0342': 'Zona Eleitoral do Rio de Janeiro',
                  '6.20.0342': 'Zona Eleitoral do Rio Grande do Norte ',
                  '6.21.0342': 'Zona Eleitoral do Rio Grande do Sul',
                  '6.22.0342': 'Zona Eleitoral de Rondônia',
                  '6.23.0342': 'Zona Eleitoral de Roraima',
                  '6.24.0342': 'Zona Eleitoral de Santa Catarina',
                  '6.25.0342': 'Zona Eleitoral de Sergipe',
                  '6.26.0342': 'Zona Eleitoral de São Paulo',
                  '6.27.0342': 'Zona Eleitoral do Tocantins',
                  '7.00.0000': 'Superior Tribunal Militar',
                  '7.01.0000': '1ª Circunscrição Judiciária Militar',
                  '7.02.0000': '2ª Circunscrição Judiciária Militar',
                  '7.03.0000': '3ª Circunscrição Judiciária Militar',
                  '7.04.0000': '4ª Circunscrição Judiciária Militar',
                  '7.05.0000': '5ª Circunscrição Judiciária Militar',
                  '7.06.0000': '6ª Circunscrição Judiciária Militar',
                  '7.07.0000': '7ª Circunscrição Judiciária Militar',
                  '7.08.0000': '8ª Circunscrição Judiciária Militar',
                  '7.09.0000': '9ª Circunscrição Judiciária Militar',
                  '7.10.0000': '10ª Circunscrição Judiciária Militar',
                  '7.11.0000': '11ª Circunscrição Judiciária Militar',
                  '7.12.0000': '12ª Circunscrição Judiciária Militar',
                  '7.01.0072': 'Auditoria Minitar da 1ª Circunscrição Judiciária Militar',
                  '7.02.0072': 'Auditoria Minitar da 2ª Circunscrição Judiciária Militar',
                  '7.03.0072': 'Auditoria Minitar da 3ª Circunscrição Judiciária Militar',
                  '7.04.0072': 'Auditoria Minitar da 4ª Circunscrição Judiciária Militar',
                  '7.05.0072': 'Auditoria Minitar da 5ª Circunscrição Judiciária Militar',
                  '7.06.0072': 'Auditoria Minitar da 6ª Circunscrição Judiciária Militar',
                  '7.07.0072': 'Auditoria Minitar da 7ª Circunscrição Judiciária Militar',
                  '7.08.0072': 'Auditoria Minitar da 8ª Circunscrição Judiciária Militar',
                  '7.09.0072': 'Auditoria Minitar da 9ª Circunscrição Judiciária Militar',
                  '7.10.0072': 'Auditoria Minitar da 10ª Circunscrição Judiciária Militar',
                  '7.11.0072': 'Auditoria Minitar da 11ª Circunscrição Judiciária Militar',
                  '7.12.0072': 'Auditoria Minitar da 12ª Circunscrição Judiciária Militar',
                  '8.01.0000': 'Tribunal de Justiça do Acre',
                  '8.02.0000': 'Tribunal de Justiça de Alagoas',
                  '8.03.0000': 'Tribunal de Justiça do Amapá',
                  '8.04.0000': 'Tribunal de Justiça do Amazonas',
                  '8.05.0000': 'Tribunal de Justiça da Bahia',
                  '8.06.0000': 'Tribunal de Justiça do Ceará',
                  '8.07.0000': 'Tribunal de Justiça do Distrito Federal e Territórios',
                  '8.08.0000': 'Tribunal de Justiça do Espirtio Santo',
                  '8.09.0000': 'Tribunal de Justiça de Goiás',
                  '8.10.0000': 'Tribunal de Justiça do Maranhão',
                  '8.11.0000': 'Tribunal de Justiça do Mato Grosso do Sul',
                  '8.12.0000': 'Tribunal de Justiça do Mato Grosso do Sul',
                  '8.13.0000': 'Tribunal de Justiça de Mina Gerais',
                  '8.14.0000': 'Tribunal de Justiça do Pará',
                  '8.15.0000': 'Tribunal de Justiça da Paraíba',
                  '8.16.0000': 'Tribunal de Justiça do Paraná',
                  '8.17.0000': 'Tribunal de Justiça do Pernambuco',
                  '8.18.0000': 'Tribunal de Justiça do Piauí',
                  '8.19.0000': 'Tribunal de Justiça do Rio de Janeiro',
                  '8.20.0000': 'Tribunal de Justiça do Rio Grande do Norte',
                  '8.21.0000': 'Tribunal de Justiça do Rio Grande do Sul',
                  '8.22.0000': 'Tribunal de Justiça de Rondônia',
                  '8.23.0000': 'Tribunal de Justiça de Roraima',
                  '8.24.0000': 'Tribunal de Justiça de Santa Catarina',
                  '8.25.0000': 'Tribunal de Justiça de Sergipe',
                  '8.26.0000': 'Tribunal de Justiça de São Paulo',
                  '8.27.0000': 'Tribunal de Justiça do Tocantins',
                  '8.01.9001': 'Turma Recursal do Tribunal de Justiça do Acre',
                  '8.02.9001': 'Turma Recursal do Tribunal de Justiça de Alagoas',
                  '8.03.9001': 'Turma Recursal do Tribunal de Justiça do Amapá',
                  '8.04.9001': 'Turma Recursal do Tribunal de Justiça do Amazonas',
                  '8.05.9001': 'Turma Recursal do Tribunal de Justiça da Bahia',
                  '8.06.9001': 'Turma Recursal do Tribunal de Justiça do Ceará',
                  '8.07.9001': 'Turma Recursal do Tribunal de Justiça do Distrito Federal e Territórios',
                  '8.08.9001': 'Turma Recursal do Tribunal de Justiça do Espirtio Santo',
                  '8.09.9001': 'Turma Recursal do Tribunal de Justiça de Goiás',
                  '8.10.9001': 'Turma Recursal do Tribunal de Justiça do Maranhão',
                  '8.11.9001': 'Turma Recursal do Tribunal de Justiça do Mato Grosso',
                  '8.12.9001': 'Turma Recursal do Tribunal de Justiça do Mato Grosso do Sul',
                  '8.13.9001': 'Turma Recursal do Tribunal de Justiça de Mina Gerais',
                  '8.14.9001': 'Turma Recursal do Tribunal de Justiça Pará',
                  '8.15.9001': 'Turma Recursal do Tribunal de Justiça da Paraíba',
                  '8.16.9001': 'Turma Recursal do Tribunal de Justiçã do Paraná',
                  '8.17.9001': 'Turma Recursal do Tribunal de Justiça do Pernambuco',
                  '8.18.9001': 'Turma Recursal do Tribunal de Justiça do Piauí',
                  '8.19.9001': 'Turma Recursal do Tribunal de Justiça do Rio de Janeiro',
                  '8.20.9001': 'Turma Recursal do Tribunal de Justiça do Rio Grande do Norte',
                  '8.21.9001': 'Turma Recursal do Tribunal de Justiça do Rio Grande do Sul',
                  '8.22.9001': 'Turma Recursal do Tribunal de Justiça de Rondônia',
                  '8.23.9001': 'Turma Recursal do Tribunal de Justiça de Roraima',
                  '8.24.9001': 'Turma Recursal do Tribunal de Justiça de Santa Catarina',
                  '8.25.9001': 'Turma Recursal do Tribunal de Justiça de Sergipe',
                  '8.26.9001': 'Turma Recursal do Tribunal de Justiça de São Paulo',
                  '8.27.9001': 'Turma Recursal do Tribunal de Justiça do Tocantins',
                  '8.01.0235': 'Foro de Origem de Tramitação do Acre',
                  '8.02.0235': 'Foro de Origem de Tramitação de Alagoas',
                  '8.03.0235': 'Foro de Origem de Tramitação do Amapá',
                  '8.04.0235': 'Foro de Origem de Tramitação do Amazonas',
                  '8.05.0235': 'Foro de Origem de Tramitação da Bahia',
                  '8.06.0235': 'Foro de Origem de Tramitação do Ceará',
                  '8.07.0235': 'Foro de Origem de Tramitação do Distrito Federal e Territórios',
                  '8.08.0235': 'Foro de Origem de Tramitação do Espirito Santo',
                  '8.09.0235': 'Foro de Origem de Tramitação de Goiás',
                  '8.10.0235': 'Foro de Origem de Tramitação do Maranhão',
                  '8.11.0235': 'Foro de Origem de Tramitação do Mato Grosso',
                  '8.12.0235': 'Foro de Origem de Tramitação do Mato Grosso do Sul',
                  '8.13.0235': 'Foro de Origem de Tramitação de Minas Gerais',
                  '8.14.0235': 'Foro de Origem de Tramitação do Pará',
                  '8.15.0235': 'Foro de Origem de Tramitação da Paraíba',
                  '8.16.0235': 'Foro de Origem de Tramitação Paraná',
                  '8.17.9001': 'Foro de Origem de Tramitação do Pernambuco',
                  '8.18.0235': 'Foro de Origem de Tramitação do Piauí',
                  '8.19.0235': 'Foro de Origem de Tramitação do Rio Janeiro',
                  '8.20.0235': 'Foro de Origem de Tramitação do Rio Grande do Norte',
                  '8.21.0235': 'Foro de Origem de Tramitaçãodo Rio Grande do Sul',
                  '8.22.0235': 'Foro de Origem de Tramitação de Rondônia',
                  '8.23.9001': 'Foro de Origem de Tramitação de Roraima',
                  '8.24.0235': 'Foro de Origem de Tramitação de Santa Catarina',
                  '8.25.0235': 'Foro de Origem de Tramitação de Sergipe',
                  '8.26.0235': 'Foro de Origem de Tramitação de São Paulo',
                  '8.27.0235': 'Foro de Origem de Tramitação do Tocantins',
                  '9.13.0000': 'Tribunal de Justiça Militar do Estado de Minas Gerais',
                  '9.21.0000': 'Tribunal de Justiça Militar do Estado do Rio Grande do Sul',
                  '9.26.0000': 'Tribunal de Justiça Militar do Estado de São Pauro',
                  '9.13.0008': 'Auditoria Militar do Estado de Minas Gerais',
                  '9.21.0008': 'Auditoria Militar do Estado do Rio Grande do Sul',
                  '9.26.0008': 'Auditoria Militar do Estado de São Paulo',
                  }

valor = entidade_maior.get(JTR_OOOO)
print('Numero do Processo:', NNNNNNN)
print('Digito Verificador:', DD)
print('Ano do processo:', AAAA)
print('Número dos Processos nos Órgãos do Poder Judiciário:', valor)

