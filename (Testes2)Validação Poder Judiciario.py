Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:\Users\Felipe Scur\Desktop\Sylex\Validação\Validação Poder Judiciario(IF).py 
Digite o número do processo: 0000408-30.2014.2.00.0000
Conselho Nacional de Justiça
>>> 
 RESTART: C:\Users\Felipe Scur\Desktop\Sylex\Validação\Validação Poder Judiciario(IF).py 
Digite o número do processo: 0000100-15.2008.4(01 a 05).0010
>>> 
 RESTART: C:\Users\Felipe Scur\Desktop\Sylex\Validação\Validação Poder Judiciario(IF).py 
Digite o número do processo: 0000100-15.2008.4.03.0010
Tribunal Regional Federal da 3ª Região
>>> origem_do_processo
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    origem_do_processo
NameError: name 'origem_do_processo' is not defined
>>> x = {'a', 'b', 'c',}
>>> 
>>> x.get(values)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x.get(values)
AttributeError: 'set' object has no attribute 'get'
>>> x
{'a', 'c', 'b'}
>>> tyoex
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tyoex
NameError: name 'tyoex' is not defined
>>> type(x)
<class 'set'>
>>> x = {'a':'1', 'b':'2', 'c':'3',}
>>> type(x)
<class 'dict'>
>>> x.get(values)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    x.get(values)
NameError: name 'values' is not defined
>>> x.get(keys)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x.get(keys)
NameError: name 'keys' is not defined
>>> x.get(key)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    x.get(key)
NameError: name 'key' is not defined
>>> x.key
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x.key
AttributeError: 'dict' object has no attribute 'key'
>>> c.keys
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    c.keys
NameError: name 'c' is not defined
>>> x.keys
<built-in method keys of dict object at 0x0000023002466C60>
>>> x.keys()
dict_keys(['a', 'b', 'c'])
>>> x.values()
dict_values(['1', '2', '3'])
>>> x.get('values')
>>> x
{'a': '1', 'b': '2', 'c': '3'}
>>> values = x.get('values')
>>> values
>>> values
>>> x.values('get')
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    x.values('get')
TypeError: values() takes no arguments (1 given)
>>> x.get('keys')
>>> print
<built-in function print>
>>> print(keys)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(keys)
NameError: name 'keys' is not defined
>>> print('keys')
keys
>>> print(x.get('keys'))
None
>>> print(x.get('values'))
None
>>> print(x)
{'a': '1', 'b': '2', 'c': '3'}
>>> x([])
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    x([])
TypeError: 'dict' object is not callable
>>> for chave in x:
	print ([])

	
[]
[]
[]
>>> for chave in x:
	print (chave)

	
a
b
c
>>> for chave in x:
	print (valor)

	
Traceback (most recent call last):
  File "<pyshell#37>", line 2, in <module>
    print (valor)
NameError: name 'valor' is not defined
>>> for chave in x:
	print ([valor])

	
Traceback (most recent call last):
  File "<pyshell#39>", line 2, in <module>
    print ([valor])
NameError: name 'valor' is not defined
>>> for chave in x:
	print ([value])

	
Traceback (most recent call last):
  File "<pyshell#41>", line 2, in <module>
    print ([value])
NameError: name 'value' is not defined
>>> for chave in x:
	print (value)

	
Traceback (most recent call last):
  File "<pyshell#43>", line 2, in <module>
    print (value)
NameError: name 'value' is not defined
>>> for chave in x[{}]:
	print (valor)

	
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    for chave in x[{}]:
TypeError: unhashable type: 'dict'
>>> for valor in x[{}]:
	print (valor)

	
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    for valor in x[{}]:
TypeError: unhashable type: 'dict'
>>> print(x[key])
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    print(x[key])
NameError: name 'key' is not defined
>>> print(x[keys])
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    print(x[keys])
NameError: name 'keys' is not defined
>>> for key in x
SyntaxError: invalid syntax
>>> for key in x:
	print(x[key])

	
1
2
3
>>> processo_cnj = '0000408-30.2014.2.00.0000'
>>> JTR_OOOO = processo_cnj[16:25]
>>> entidade_maior = {'1.00': 'Supremo Tribunal Federal',
                  '2.00': 'Conselho Nacional de Justiça',
                  '3.00': 'Superior Tribunal de Justiça',
                  '4.90': 'Conselho de Justiça Federal',
                  '4.01': 'Tribunal Regional Federal da 1ª Região',
                  '4.02': 'Tribunal Regional Federal da 2ª Região',
                  '4.03': 'Tribunal Regional Federal da 3ª Região',
                  '4.04': 'Tribunal Regional Federal da 4ª Região',
                  '4.05': 'Tribunal Reguinal Federal da 5ª Região',
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
                  '5.00': 'Tribunal Superior do Trabalho',
                  '5.90': 'Conselho Superior da Justiça do Trabalho',
                  '5.01': '1ª Tribunal Regional do Trabalho',
                  '5.02': '2ª Tribunal Regional do Trabalho',
                  '5.03': '3ª Tribunal Regional do Trabalho',
                  '5.04': '4ª Tribunal Regional do Trabalho',
                  '5.05': '5ª Tribunal Regional do Trabalho',
                  '5.06': '6ª Tribunal Regional do Trabalho',
                  '5.07': '7ª Tribunal Regional do Trabalho',
                  '5.08': '8ª Tribunal Regional do Trabalho',
                  '5.09': '9ª Tribunal Regional do Trabalho',
                  '5.10': '10ª Tribunal Regional do Trabalho',
                  '5.11': '11ª Tribunal Regional do Trabalho',
                  '5.12': '12ª Tribunal Regional do Trabalho',
                  '5.13': '13ª Tribunal Regional do Trabalho',
                  '5.14': '14ª Tribunal Regional do Trabalho',
                  '5.15': '15ª Tribunal Regional do Trabalho',
                  '5.16': '16ª Tribunal Regional do Trabalho',
                  '5.17': '17ª Tribunal Regional do Trabalho',
                  '5.18': '18ª Tribunal Regional do Trabalho',
                  '5.19': '19ª Tribunal Regional do Trabalho',
                  '5.20': '20ª Tribunal Regional do Trabalho',
                  '5.21': '21ª Tribunal Regional do Trabalho',
                  '5.22': '22ª Tribunal Regional do Trabalho',
                  '5.23': '23ª Tribunal Regional do Trabalho',
                  '5.24': '24ª Tribunal Regional do Trabalho',
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
                  '6.00': 'Tribunal Superior Eleitoral',
                  '6.01': 'Tribunal Regional Eleitoral do Acre',
                  '6.02': 'Tribunal Regional Eleitoral de Alagoas',
                  '6.03': 'Tribunal Regional Eleitoral do Amapá',
                  '6.04': 'Tribunal Regional Eleitoral do Amazonas',
                  '6.05': 'Tribunal Regional Eleitoral da Bahia',
                  '6.06': 'Tribunal Regional Eleitoral do Ceará',
                  '6.07': 'Tribunal Regional Eleitoral do Distrito Federal e Territórios',
                  '6.08': 'Tribunal Regional Eleitoral do Espirito Santo',
                  '6.09': 'Tribunal Regional Eleitoral de Goiás',
                  '6.10': 'Tribunal Regional Eleitoral do Maranhão',
                  '6.11': 'Tribunal Regional Eleitoral do Mato Grosso',
                  '6.12': 'Tribunal Regional Eleitoral do Mato Grosso do Sul',
                  '6.13': 'Tribunal Regional Eleitoral de Minas Gerais',
                  '6.14': 'Tribunal Regional Eleitoral do Pará',
                  '6.15': 'Tribunal Regional Eleitoral da Paraíba',
                  '6.16': 'Tribunal Regional Eleitoral do Paraná',
                  '6.17': 'Tribunal Regional Eleitoral do Pernambuco',
                  '6.18': 'Tribunal Regional Eleitoral do Piauí',
                  '6.19': 'Tribunal Regional Eleitoral do Rio de Janeiro',
                  '6.20': 'Tribunal Regional Eleitoral do Rio Grande do Norte',
                  '6.21': 'Tribunal Regional Eleitoral do Rio Grande do Sul',
                  '6.22': 'Tribunal Regional Eleitoral de Rondônia',
                  '6.23': 'Tribunal Regional Eleitoral de Roraima',
                  '6.24': 'Tribunal Regional Eleitoral de Santa Catarina',
                  '6.25': 'Tribunal Regional Eleitoral de Sergipe',
                  '6.26': 'Tribunal Regional Eleitoral de São Paulo',
                  '6.27': 'Tribunal Regional Eleitoral do Tocantins',
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
                  '7.00': 'Superior Tribunal Militar',
                  '7.01': '1ª Circunscrição Judiciária Militar',
                  '7.02': '2ª Circunscrição Judiciária Militar',
                  '7.03': '3ª Circunscrição Judiciária Militar',
                  '7.04': '4ª Circunscrição Judiciária Militar',
                  '7.05': '5ª Circunscrição Judiciária Militar',
                  '7.06': '6ª Circunscrição Judiciária Militar',
                  '7.07': '7ª Circunscrição Judiciária Militar',
                  '7.08': '8ª Circunscrição Judiciária Militar',
                  '7.09': '9ª Circunscrição Judiciária Militar',
                  '7.10': '10ª Circunscrição Judiciária Militar',
                  '7.11': '11ª Circunscrição Judiciária Militar',
                  '7.12': '12ª Circunscrição Judiciária Militar',
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
                  '8.01': 'Tribunal de Justiça do Acre',
                  '8.02': 'Tribunal de Justiça de Alagoas',
                  '8.03': 'Tribunal de Justiça do Amapá',
                  '8.04': 'Tribunal de Justiça do Amazonas',
                  '8.05': 'Tribunal de Justiça da Bahia',
                  '8.06': 'Tribunal de Justiça do Ceará',
                  '8.07': 'Tribunal de Justiça do Distrito Federal e Territórios',
                  '8.08': 'Tribunal de Justiça do Espirtio Santo',
                  '8.09': 'Tribunal de Justiça de Goiás',
                  '8.10': 'Tribunal de Justiça do Maranhão',
                  '8.11': 'Tribunal de Justiça do Mato Grosso do Sul',
                  '8.12': 'Tribunal de Justiça do Mato Grosso do Sul',
                  '8.13': 'Tribunal de Justiça de Mina Gerais',
                  '8.14': 'Tribunal de Justiça do Pará',
                  '8.15': 'Tribunal de Justiça da Paraíba',
                  '8.16': 'Tribunal de Justiça do Paraná',
                  '8.17': 'Tribunal de Justiça do Pernambuco',
                  '8.18': 'Tribunal de Justiça do Piauí',
                  '8.19': 'Tribunal de Justiça do Rio de Janeiro',
                  '8.20': 'Tribunal de Justiça do Rio Grande do Norte',
                  '8.21': 'Tribunal de Justiça do Rio Grande do Sul',
                  '8.22': 'Tribunal de Justiça de Rondônia',
                  '8.23': 'Tribunal de Justiça de Roraima',
                  '8.24': 'Tribunal de Justiça de Santa Catarina',
                  '8.25': 'Tribunal de Justiça de Sergipe',
                  '8.26': 'Tribunal de Justiça de São Paulo',
                  '8.27': 'Tribunal de Justiça do Tocantins',
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
                  '9.13': 'Tribunal de Justiça Militar do Estado de Minas Gerais',
                  '9.21': 'Tribunal de Justiça Militar do Estado do Rio Grande do Sul',
                  '9.26': 'Tribunal de Justiça Militar do Estado de São Pauro',
                  '9.13.0008': 'Auditoria Militar do Estado de Minas Gerais',
                  '9.21.0008': 'Auditoria Militar do Estado do Rio Grande do Sul',
                  '9.26.0008': 'Auditoria Militar do Estado de São Paulo',
                  }
entidade_maior.get(JTR_OOOO)
print(entidade_maior)