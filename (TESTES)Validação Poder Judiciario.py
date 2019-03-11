Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> TRF = [1ª:0000100-15.2008.4.01.0000, 
       2ª:0000100-15.2008.4.02.0000,
       3ª:0000100-15.2008.4.03.0000,
       4ª:0000100-15.2008.4.04.0000,
       5ª:0000100-15.2008.4.05.0000, 
      ]
SyntaxError: invalid syntax
>>> TRF = [1:0000100-15.2008.4.01.0000, 
       2:0000100-15.2008.4.02.0000,
       3:0000100-15.2008.4.03.0000,
       4:0000100-15.2008.4.04.0000,
       5:0000100-15.2008.4.05.0000, 
      ]
SyntaxError: invalid syntax
>>> TRF = [1 0000100-15.2008.4.01.0000, 
       2 0000100-15.2008.4.02.0000,
       3 0000100-15.2008.4.03.0000,
       4 0000100-15.2008.4.04.0000,
       5 0000100-15.2008.4.05.0000, 
      ]
SyntaxError: invalid token
>>> TRF = [ 0000100-15.2008.4.01.0000, 
        0000100-15.2008.4.02.0000,
        0000100-15.2008.4.03.0000,
        0000100-15.2008.4.04.0000,
        0000100-15.2008.4.05.0000, 
      ]
SyntaxError: invalid token
>>>  TRF = ["1ª:0000100-15.2008.4.01.0000", 
       "2ª:0000100-15.2008.4.02.0000",
       "3ª:0000100-15.2008.4.03.0000",
       "4ª:0000100-15.2008.4.04.0000",
       "5ª:0000100-15.2008.4.05.0000", 
      ]
SyntaxError: unexpected indent
>>> TRF = ["1ª:0000100-15.2008.4.01.0000", 
       "2ª:0000100-15.2008.4.02.0000",
       "3ª:0000100-15.2008.4.03.0000",
       "4ª:0000100-15.2008.4.04.0000",
       "5ª:0000100-15.2008.4.05.0000", 
      ]

>>> TRF
['1ª:0000100-15.2008.4.01.0000', '2ª:0000100-15.2008.4.02.0000', '3ª:0000100-15.2008.4.03.0000', '4ª:0000100-15.2008.4.04.0000', '5ª:0000100-15.2008.4.05.0000']
>>> type(TRF)
<class 'list'>
>>> print(TRF[0])
1ª:0000100-15.2008.4.01.0000
>>> processo_cnj = 0000100-15.2008.4.01.0000
SyntaxError: invalid token
>>> processo_cnj = "0000100-15.2008.4.01.0000"
>>> NNNNNNN = [0:6]
SyntaxError: invalid syntax
>>> NNNNNNN = processo_cnj[0:6]
>>> NNNNNNN
'000010'
>>> NNNNNNN = processo_cnj[0:7]
>>> NNNNNNN
'0000100'
>>> DD = [8:10]
SyntaxError: invalid syntax
>>> DD = processo_cnj[8:10]
>>> DD
'15'
>>> AAAA = processo_cnj[11:15]
>>> AAAA
'2008'
>>> J.TR = processo_cnj[16:20]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    J.TR = processo_cnj[16:20]
NameError: name 'J' is not defined
>>> J_TR = processo_cnj[16:20]
>>> J_TR
'4.01'
>>> OOOO = processo_cnj [21:25]
>>> OOOO
'0000'
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.4.05.0000 
Traceback (most recent call last):
  File "C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py", line 16, in <module>
    if J.TR == TRF[0]:
NameError: name 'J' is not defined
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.4.05.0000 
 Tribunal Reginal Federal da 5ª Região
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.4.01.0000 
 Tribunal Reginal Federal da 5ª Região
>>> TRF[0]
'1ª:0000100-15.2008.4.01.0000'
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 2ª:0000100-15.2008.4.02.0000
Tribunal Reginal Federal da 5ª Região
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.4.02.0000
Tribunal Reginal Federal da 2ª Região
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.4.02.0000
Tribunal Reginal Federal da 2ª Região
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.4.04.0000 
Tribunal Reginal Federal da 4ª Região
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.4.05.0000 
Tribunal Reginal Federal da 5ª Região
>>> processo_cnj = "0000000-11.2222.3.44.5555"
>>> NNNNNNN = processo_cnj[0:7]
>>> DD = processo_cnj[8:10]
>>> AAAA = processo_cnj [11:15]
>>> J_TR = processo_cnj[16:20]
>>> OOOO = processo_cnj [21:25]
>>> J_TR_OOOO = J_TR + OOOO
>>> J_TR_OOOO
'3.445555'
>>> J_TR_OOOO = [16:25]
SyntaxError: invalid syntax
>>> J_TR_OOOO = processo_cnj[16:25]
>>> J_TR_OOOO
'3.44.5555'
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0235
Tribunal Reginal Federal da 5ª Região
>>> Estados = ["Acre (AC)", "Alagoas (AL)", "Amapá (AP)", "Amazonas (AM)", "Bahia (BA)", "Ceará (CE)",
           "Distrito Federal (DF)", "Espírito Santo (ES)", "Goiás (GO)", "Maranhão (MA)", "Mato Grosso (MT)", "Mato Grosso do Sul (MS)"
           "Minas Gerais (MG)", "Pará (PA)", "Paraíba (PB)", "Paraná (PR)", "Pernambuco (PE)", "Piauí (PI)",
           "Rio de Janeiro (RJ)", "Rio Grande do Norte (RN)", "Rio Grande do Sul (RS)", "Rondônia (RO)", "Roraima (RR)", "Santa Catarina (SC)",
           "São Paulo (SP)", "Sergipe (SE)", "Tocantins (TO)",
           ]
>>> Estadps
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    Estadps
NameError: name 'Estadps' is not defined
>>> Estados
['Acre (AC)', 'Alagoas (AL)', 'Amapá (AP)', 'Amazonas (AM)', 'Bahia (BA)', 'Ceará (CE)', 'Distrito Federal (DF)', 'Espírito Santo (ES)', 'Goiás (GO)', 'Maranhão (MA)', 'Mato Grosso (MT)', 'Mato Grosso do Sul (MS)Minas Gerais (MG)', 'Pará (PA)', 'Paraíba (PB)', 'Paraná (PR)', 'Pernambuco (PE)', 'Piauí (PI)', 'Rio de Janeiro (RJ)', 'Rio Grande do Norte (RN)', 'Rio Grande do Sul (RS)', 'Rondônia (RO)', 'Roraima (RR)', 'Santa Catarina (SC)', 'São Paulo (SP)', 'Sergipe (SE)', 'Tocantins (TO)']
>>> print("Supremo", Estados[1])
Supremo Alagoas (AL)
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.5.08.0197 
Tribunais Regionais do Trabalho da 8ª Região
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.5.08.0197 
Tribunal Regional do Trabalho da 8ª Região
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.6.00.0000
Tribunal Superior Eleitoral
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.5.08.0197
Tribunal Regional do Trabalho da 8ª Região
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.5.08.0197
Traceback (most recent call last):
  File "C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py", line 138, in <module>
    elif J_TR_OOOO == TRVF:
NameError: name 'J_TR_OOOO' is not defined
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.4.03.9001
Tribunal Reginal Federal da 3ª Região
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.4.03.9001
Tribunal Reginal Federal da 3ª Região
>>> print ("Tribunal Regional Eleitoral do" Estado[0])
SyntaxError: invalid syntax
>>> print ("Tribunal Regional Eleitoral do", Estado[0])
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print ("Tribunal Regional Eleitoral do", Estado[0])
NameError: name 'Estado' is not defined
>>> print ("Tribunal Regional Eleitoral do", Estados[0])
Tribunal Regional Eleitoral do Acre (AC)
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.6.01.0000 
Traceback (most recent call last):
  File "C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py", line 148, in <module>
    elif J_TR_OOOO == SJ:
NameError: name 'J_TR_OOOO' is not defined
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.6.01.0000 
Traceback (most recent call last):
  File "C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py", line 220, in <module>
    elif J_TR_OOOO == VT[5]:
NameError: name 'J_TR_OOOO' is not defined
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.6.01.0000 
Tribunal Regional Eleitoral do Acre
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.6.09.0000 
Tribunal Regional Eleitoral do Goiás
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.8.26.0000 
Traceback (most recent call last):
  File "C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py", line 396, in <module>
    elif JTR_OOOO == AM[3]:
IndexError: list index out of range
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.8.26.0000 
Tribunal de Justiça do Tocantins
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.9.26.0000 
Tribunal de Justiça Militar do Estadi de São Paulo
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.9.21.0000 
Tribunal de Justiça Militar do Estado do Rio Grande do Sul
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.9.13.0000 
Tribunal de Justiça Militar do Estado de Minas Gerias
>>> 
= RESTART: C:/Users/Felipe Scur/Desktop/Sylex/Validação Poder Judiciario.py =
Digite o número do processo: 0000100-15.2008.9.13.0008
Tribunal de Justiça Militar do Estado de Minas Gerias
>>> 
