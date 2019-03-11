processo_cnj = input("Digite o número do processo: ")
#NNNNNNN-DD.AAAA.J.TR.OOOO
#Associação a uma variável.
NNNNNNN = processo_cnj[0:7]
DD = processo_cnj[8:10]
AAAA = processo_cnj[11:15]
J_TR = processo_cnj[16:20]
OOOO = processo_cnj[21:25]
JTR_OOOO = processo_cnj[16:25]

#Tribunais Regionais Federais 1ª a 5ª
TRF = ["4.01", 
       "4.02",
       "4.03",
       "4.04",
       "4.05", 
      ]
#Supremo Tribunal Federal
STF = "1.00"
#Conselho Nacional de Justiça
CNJ = "2.00"
#Superior Tribunal de Justiça
STJ = "3.00"
#Conselho de Justiça Federal
CJF = "4.90"
#Turmas Recursais/Vara Federal
TRVF = ["4.01.9001",
        "4.02.9001",
        "4.03.9001",
        "4.04.9001",
        "4.05.9001",
        ]
#Subseções Judiciarias/Juizado Especial Federal
SJ = ["4.01.0010",
      "4.02.0010",
      "4.03.0010",
      "4.04.0010",
      "4.05.0010",
      ]
#Tribunal Superior do Trabalho
TST = "5.00"
#Conselho Superior da Justiça do Trabalho
CSJT = "5.90"
#Tribunais Regionais do Trabalho 1ª a 24ª
TRT = ["5.01", "5.02", "5.03", "5.04", "5.05", "5.06",
       "5.07", "5.08", "5.09", "5.10", "5.11", "5.12",
       "5.13", "5.14", "5.15", "5.16", "5.17", "5.18",
       "5.19", "5.20", "5.21", "5.22", "5.23", "5.24",
       ]
#Varas do Trabalho
VT = ["5.01.0197", "5.02.0197", "5.03.0197", "5.04.0197", "5.05.0197", "5.06.0197",
      "5.07.0197", "5.08.0197", "5.09.0197", "5.10.0197", "5.11.0197", "5.12.0197",
      "5.13.0197", "5.14.0197", "5.15.0197", "5.16.0197", "5.17.0197", "5.18.0197",
      "5.19.0197", "5.20.0197", "5.21.0197", "5.22.0197", "5.23.0197", "5.24.0197",
      ]
#Tribunal Superior Eleitoral
TSE = "6.00"
#Tribunais Regionais Eleitorais
TRE = ["6.01", "6.02", "6.03", "6.04", "6.05", "6.06",
       "6.07", "6.08", "6.09", "6.10", "6.11", "6.12",
       "6.13", "6.14", "6.15", "6.16", "6.17", "6.18",
       "6.19", "6.20", "6.21", "6.22", "6.23", "6.24",
       "6.25", "6.26", "6.27",
       ]
#Zonas Eleitorais
ZE = ["6.01.0342", "6.02.0342", "6.03.0342", "6.04.0342", "6.05.0342", "6.06.0342",
      "6.07.0342", "6.08.0342", "6.09.0342", "6.10.0342", "6.11.0342", "6.12.0342",
      "6.13.0342", "6.14.0342", "6.15.0342", "6.16.0342", "6.17.0342", "6.18.0342",
      "6.19.0342", "6.20.0342", "6.21.0342", "6.22.0342", "6.23.0342", "6.24.0342",
      "6.25.0342", "6.26.0342", "6.27.0342",
      ]
#Superior Tribunal Militar
STM = "7.00"
#Circunscrições Judicárias Militar
CJM = ["7.01", "7.02", "7.03", "7.04", "7.05", "7.06",
      "7.07", "7.08", "7.09", "7.10", "7.11", "7.12",
      ]
#Auditorias Militares
AMSTM = ["7.01.0072", "7.02.0072", "7.03.0072", "7.04.0072", "7.05.0072", "7.06.0072",
      "7.07.0072", "7.08.0072", "7.09.0072", "7.10.0072", "7.11.0072", "7.12.0072",
      ]
#Tribunais de Justiça
TJ = ["8.01", "8.02", "8.03", "8.04", "8.05", "8.06",
      "8.07", "8.08", "8.09", "8.10", "8.11", "8.12",
      "8.13", "8.14", "8.15", "8.16", "8.17", "8.18",
      "8.19", "8.20", "8.21", "8.22", "8.23", "8.24",
      "8.25", "8.26", "8.27",
      ]
#Turmas Recursais
TR = ["8.01.9001", "8.02.9001", "8.03.9001", "8.04.9001", "8.05.9001", "8.06.9001",
      "8.07.9001", "8.08.9001", "8.09.9001", "8.10.9001", "8.11.9001", "8.12.9001",
      "8.13.9001", "8.14.9001", "8.15.9001", "8.16.9001", "8.17.9001", "8.18.9001",
      "8.19.9001", "8.20.9001", "8.21.9001", "8.22.9001", "8.23.9001", "8.24.9001",
      "8.25.9001", "8.26.9001", "8.27.9001",
      ]
#Foros de Origem de Tramitação
FOT = ["8.01.0235", "8.02.0235", "8.03.0235", "8.04.0235", "8.05.0235", "8.06.0235",
      "8.07.0235", "8.08.0235", "8.09.0235", "8.10.0235", "8.11.0235", "8.12.0235",
      "8.13.0235", "8.14.0235", "8.15.0235", "8.16.0235", "8.17.9001", "8.18.0235",
      "8.19.0235", "8.20.0235", "8.21.0235", "8.22.0235", "8.23.9001", "8.24.0235",
      "8.25.0235", "8.26.0235", "8.27.0235",
      ]
#Tribunais de Justiça Militar
TJM = ["9.13", #Estado de Minas Gerais
       "9.21", #Estado do Rio Grande do Sul
       "9.26", #Estado de São Palo
       ]
#Auditorias Militar
AM = ["9.13.0008",
      "9.21.0008",
      "9.26.0008",
    ]
Estados = ["Acre", "Alagoas", "Amapá", "Amazonas", "Bahia", "Ceará",
           "Distrito Federal", "Espírito Santo", "Goiás", "Maranhão", "Mato Grosso", "Mato Grosso do Sul"
           "Minas Gerais", "Pará", "Paraíba", "Paraná", "Pernambuco", "Piauí",
           "Rio de Janeiro", "Rio Grande do Norte", "Rio Grande do Sul", "Rondônia", "Roraima", "Santa Catarina",
           "São Paulo", "Sergipe", "Tocantins",
           ]

if J_TR == TRF[0]:
    print("Tribunal Regional Federal da 1ª Região")
elif J_TR == TRF[1]:
    print("Tribunal Regional Federal da 2ª Região")
elif J_TR == TRF[2]:
    print("Tribunal Regional Federal da 3ª Região")
elif J_TR == TRF[3]:
    print("Tribunal Regional Federal da 4ª Região")
elif J_TR == TRF[4]:
    print("Tribunal Regional Federal da 5ª Região")
elif J_TR == STF:
    print("Supremo Tribunal Federal")
elif J_TR == CNJ:
    print("Conselho Nacional de Justiça")
elif J_TR == STJ:
    print("Superior Tribunal de Justiça")
elif J_TR == CJF:
    print("Conselho da Justiça Federal")
elif JTR_OOOO == TRVF[0]:
    print("Turma Recursal/Vara Federal") #Confirmar com o Roberto, pois tem duas "Turma Recursal"
elif JTR_OOOO == TRVF[1]:
    print("Turma Recursal/Vara Federal") #Confirmar com o Roberto, pois tem duas "Turma Recursal"
elif JTR_OOOO == TRVF[2]:
    print("Turma Recursal/Vara Federal") #Confirmar com o Roberto, pois tem duas "Turma Recursal"
elif JTR_OOOO == TRVF[3]:
    print("Turma Recursal/Vara Federal") #Confirmar com o Roberto, pois tem duas "Turma Recursal"
elif JTR_OOOO == TRVF[4]:
    print("Turma Recursal/Vara Federal") #Confirmar com o Roberto, pois tem duas "Turma Recursal"
elif JTR_OOOO == SJ[0]:
    print("Subseção Judiciária") #Confirmar nome
elif JTR_OOOO == SJ[1]:
    print("Subseção Judiciária") #Confirmar nome
elif JTR_OOOO == SJ[2]:
    print("Subseção Judiciária") #Confirmar nome
elif JTR_OOOO == SJ[3]:
    print("Subseção Judiciária") #Confirmar nome
elif JTR_OOOO == SJ[4]:
    print("Subseção Judiciária") #Confirmar nome
elif J_TR == TST:
    print("Tribunal Superior do Trabalho")
elif J_TR == CSJT:
    print("Conselho Superior da Justiça do Trabalho")
elif J_TR == TRT[0]:
    print ("Tribunal Regional do Trabalho da 1ª Região")
elif J_TR == TRT[1]:
    print ("Tribunal Regional do Trabalho da 2ª Região")
elif J_TR == TRT[2]:
    print ("Tribunal Regional do Trabalho da 3ª Região")
elif J_TR == TRT[3]:
    print ("Tribunal Regional do Trabalho da 4ª Região")
elif J_TR == TRT[4]:
    print ("Tribunal Regional do Trabalho da 5ª Região")
elif J_TR == TRT[5]:
    print ("Tribunal Regional do Trabalho da 6ª Região")
elif J_TR == TRT[6]:
    print ("Tribunal Regional do Trabalho da 7ª Região")
elif J_TR == TRT[7]:
    print ("Tribunal Regional do Trabalho da 8ª Região")
elif J_TR == TRT[8]:
    print ("Tribunal Regional do Trabalho da 9ª Região")
elif J_TR == TRT[9]:
    print ("Tribunal Regional do Trabalho da 10ª Região")
elif J_TR == TRT[10]:
    print ("Tribunal Regional do Trabalho da 11ª Região")
elif J_TR == TRT[11]:
    print ("Tribunal Regional do Trabalho da 12ª Região")
elif J_TR == TRT[12]:
    print ("Tribunal Regional do Trabalho da 13ª Região")
elif J_TR == TRT[13]:
    print ("Tribunal Regional do Trabalho da 14ª Região")
elif J_TR == TRT[14]:
    print ("Tribunal Regional do Trabalho da 15ª Região")
elif J_TR == TRT[15]:
    print ("Tribunal Regional do Trabalho da 16ª Região")
elif J_TR == TRT[16]:
    print ("Tribunal Regional do Trabalho da 17ª Região")
elif J_TR == TRT[17]:
    print ("Tribunal Regional do Trabalho da 18ª Região")
elif J_TR == TRT[18]:
    print ("Tribunal Regional do Trabalho da 19ª Região")
elif J_TR == TRT[19]:
    print ("Tribunal Regional do Trabalho da 20ª Região")
elif J_TR == TRT[20]:
    print ("Tribunal Regional do Trabalho da 21ª Região")
elif J_TR == TRT[21]:
    print ("Tribunal Regional do Trabalho da 22ª Região")
elif J_TR == TRT[22]:
    print ("Tribunal Regional do Trabalho da 23ª Região")
elif J_TR == TRT[23]:
    print ("Tribunal Regional do Trabalho da 24ª Região")
elif JTR_OOOO == VT[0]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[1]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[2]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[3]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[4]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[5]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[6]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[7]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[8]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[9]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[10]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[11]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[12]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[13]:
    prnt ("Vara do Trabalho")
elif JTR_OOOO == VT[14]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[15]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[16]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[17]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[18]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[19]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[20]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[21]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[22]:
    print ("Vara do Trabalho")
elif JTR_OOOO == VT[23]:
    print ("Vara do Trabalho")
elif J_TR == TSE:
    print ("Tribunal Superior Eleitoral")
elif J_TR == TRE[0]:
    print ("Tribunal Regional Eleitoral do", Estados[0])
elif J_TR == TRE[1]:
    print ("Tribunal Regional Eleitoral do", Estados[1])
elif J_TR == TRE[2]:
    print ("Tribunal Regional Eleitoral do", Estados[2])
elif J_TR == TRE[3]:
    print ("Tribunal Regional Eleitoral do", Estados[3])
elif J_TR == TRE[4]:
    print ("Tribunal Regional Eleitoral do", Estados[4])
elif J_TR == TRE[5]:
    print ("Tribunal Regional Eleitoral do", Estados[5])
elif J_TR == TRE[6]:
    print ("Tribunal Regional Eleitoral do", Estados[6])
elif J_TR == TRE[7]:
    print ("Tribunal Regional Eleitoral do", Estados[7])
elif J_TR == TRE[8]:
    print ("Tribunal Regional Eleitoral do", Estados[8])
elif J_TR == TRE[9]:
    print ("Tribunal Regional Eleitoral do", Estados[9])
elif J_TR == TRE[10]:
    print ("Tribunal Regional Eleitoral do", Estados[10])
elif J_TR == TRE[11]:
    print ("Tribunal Regional Eleitoral do", Estados[11])
elif J_TR == TRE[12]:
    print ("Tribunal Regional Eleitoral do", Estados[12])
elif J_TR == TRE[13]:
    print ("Tribunal Regional Eleitoral do", Estados[13])
elif J_TR == TRE[14]:
    print ("Tribunal Regional Eleitoral do", Estados[14])
elif J_TR == TRE[15]:
    print ("Tribunal Regional Eleitoral do", Estados[15])
elif J_TR == TRE[16]:
    print ("Tribunal Regional Eleitoral do", Estados[16])
elif J_TR == TRE[17]:
    print ("Tribunal Regional Eleitoral do", Estados[17])
elif J_TR == TRE[18]:
    print ("Tribunal Regional Eleitoral do", Estados[18])
elif J_TR == TRE[19]:
    print ("Tribunal Regional Eleitoral do", Estados[19])
elif J_TR == TRE[20]:
    print ("Tribunal Regional Eleitoral do", Estados[21])
elif J_TR == TRE[22]:
    print ("Tribunal Regional Eleitoral do", Estados[22])
elif J_TR == TRE[23]:
    print ("Tribunal Regional Eleitoral do", Estados[23])
elif J_TR == TRE[24]:
    print ("Tribunal Regional Eleitoral do", Estados[24])
elif J_TR == TRE[25]:
    print ("Tribunal Regional Eleitoral do", Estados[25])
elif J_TR == TRE[26]:
    print ("Tribunal Regional Eleitoral do", Estados[26])
elif JTR_OOOO == ZE[0]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[1]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[2]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[3]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[4]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[5]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[6]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[7]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[8]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[9]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[10]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[11]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[12]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[13]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[14]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[15]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[16]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[17]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[18]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[19]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[20]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[21]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[22]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[23]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[24]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[25]:
    print ("Zona Eleitoral")
elif JTR_OOOO == ZE[26]:
    print ("Zona Eleitoral")
elif J_TR == CJM[0]:
    print ("1ª Circunscrição Judiciária Militar")
elif J_TR == CJM[1]:
    print ("2ª Circunscrição Judiciária Militar")
elif J_TR == CJM[2]:
    print ("3ª Circunscrição Judiciária Militar")
elif J_TR == CJM[3]:
    print ("4ª Circunscrição Judiciária Militar")
elif J_TR == CJM[4]:
    print ("5ª Circunscrição Judiciária Militar")
elif J_TR == CJM[5]:
    print ("6ª Circunscrição Judiciária Militar")
elif J_TR == CJM[6]:
    print ("7ª Circunscrição Judiciária Militar")
elif J_TR == CJM[7]:
    print ("8ª Circunscrição Judiciária Militar")
elif J_TR == CJM[8]:
    print ("9ª Circunscrição Judiciária Militar")
elif J_TR == CJM[9]:
    print ("10ª Circunscrição Judiciária Militar")
elif J_TR == CJM[10]:
    print ("11ª Circunscrição Judiciária Militar")
elif J_TR == CJM[11]:
    print ("12ª Circunscrição Judiciária Militar")
elif JTR_OOOO == AMSTM[0]:
    print ("Auditoria Militar")
elif JTR_OOOO == AMSTM[1]:
    print ("Auditoria Militar")
elif JTR_OOOO == AMSTM[2]:
    print ("Auditoria Militar")
elif JTR_OOOO == AMSTM[3]:
    print ("Auditoria Militar")
elif JTR_OOOO == AMSTM[4]:
    print ("Auditoria Militar")
elif JTR_OOOO == AMSTM[5]:
    print ("Auditoria Militar")
elif JTR_OOOO == AMSTM[6]:
    print ("Auditoria Militar")
elif JTR_OOOO == AMSTM[7]:
    print ("Auditoria Militar")
elif JTR_OOOO == AMSTM[8]:
    print ("Auditoria Militar")
elif JTR_OOOO == AMSTM[9]:
    print ("Auditoria Militar")
elif JTR_OOOO == AMSTM[10]:
    print ("Auditoria Militar")
elif JTR_OOOO == AMSTM[11]:
    print ("Auditoria Militar")
elif J_TR == TJ[0]:
    print ("Tribunal de Justiça do" ,Estados[0])
elif J_TR == TJ[1]:
    print ("Tribunal de Justiça do" ,Estados[1])
elif J_TR == TJ[2]:
    print ("Tribunal de Justiça do" ,Estados[2])
elif J_TR == TJ[3]:
    print ("Tribunal de Justiça do" ,Estados[3])
elif J_TR == TJ[4]:
    print ("Tribunal de Justiça do" ,Estados[4])
elif J_TR == TJ[5]:
    print ("Tribunal de Justiça do" ,Estados[5])
elif J_TR == TJ[6]:
    print ("Tribunal de Justiça do" ,Estados[6])
elif J_TR == TJ[7]:
    print ("Tribunal de Justiça do" ,Estados[7])
elif J_TR == TJ[8]:
    print ("Tribunal de Justiça do" ,Estados[8])
elif J_TR == TJ[9]:
    print ("Tribunal de Justiça do" ,Estados[9])
elif J_TR == TJ[10]:
    print ("Tribunal de Justiça do" ,Estados[10])
elif J_TR == TJ[11]:
    print ("Tribunal de Justiça do" ,Estados[11])
elif J_TR == TJ[12]:
    print ("Tribunal de Justiça do" ,Estados[12])
elif J_TR == TJ[13]:
    print ("Tribunal de Justiça do" ,Estados[13])
elif J_TR == TJ[14]:
    print ("Tribunal de Justiça do" ,Estados[14])
elif J_TR == TJ[15]:
    print ("Tribunal de Justiça do" ,Estados[15])
elif J_TR == TJ[16]:
    print ("Tribunal de Justiça do" ,Estados[16])
elif J_TR == TJ[17]:
    print ("Tribunal de Justiça do" ,Estados[17])
elif J_TR == TJ[18]:
    print ("Tribunal de Justiça do" ,Estados[18])
elif J_TR == TJ[19]:
    print ("Tribunal de Justiça do" ,Estados[19])
elif J_TR == TJ[20]:
    print ("Tribunal de Justiça do" ,Estados[20])
elif J_TR == TJ[21]:
    print ("Tribunal de Justiça do" ,Estados[21])
elif J_TR == TJ[22]:
    print ("Tribunal de Justiça do" ,Estados[22])
elif J_TR == TJ[23]:
    print ("Tribunal de Justiça do" ,Estados[23])
elif J_TR == TJ[24]:
    print ("Tribunal de Justiça do" ,Estados[24])
elif J_TR == TJ[25]:
    print ("Tribunal de Justiça do" ,Estados[25])
elif J_TR == TJ[26]:
    print ("Tribunal de Justiça do" ,Estados[26])
elif JTR_OOOO == TR[0]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[1]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[2]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[3]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[4]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[5]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[6]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[7]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[8]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[9]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[10]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[11]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[12]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[13]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[14]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[15]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[16]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[17]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[18]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[19]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[20]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[21]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[22]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[23]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[24]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[25]:
    print ("Turma Recursal")
elif JTR_OOOO == TR[26]:
    print ("Turma Recursal")
elif JTR_OOOO == FOT[0]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[1]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[2]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[3]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[4]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[5]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[6]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[7]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[8]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[9]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[10]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[11]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[12]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[13]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[14]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[15]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[16]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[17]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[18]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[19]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[20]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[21]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[22]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[23]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[24]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[25]:
    print ("Foro de Origem de Tramitação")
elif JTR_OOOO == FOT[26]:
    print ("Foro de Origem de Tramitação")
elif J_TR == TJM[0]:
    print ("Tribunal de Justiça Militar do Estado de Minas Gerias")
elif J_TR == TJM[1]:
    print ("Tribunal de Justiça Militar do Estado do Rio Grande do Sul")
elif J_TR == TJM[2]:
    print ("Tribunal de Justiça Militar do Estado de São Paulo")
elif JTR_OOOO == AM[0]:
    print ("Auditoria Militar")
elif JTR_OOOO == AM[1]:
    print ("Auditoria Militar")
elif JTR_OOOO == AM[2]:
    print ("Auditoria Militar")
