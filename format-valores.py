"""
Formatando valores com modificadores

:s = Texto (string)
:d = Inteiro (int)
:f = Número de ponto flutuante (flot)
:. (NUMERO)f = Quantidade de Casas Decimais (float) :.2f
:(CARACTERE)(>ou<ou^)(QUANTIDADE/TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
num1 = 1
print(f' {num1:0>10} = num1:0>10')

num2 = 888
print(f' {num2:0>10} = num2:0>10')

num3 = 777
print(f' {num3:0^10} = num3:0^10')

divisao = 10 / 3
print(f' divisao = 10/3 - {divisao}')
print(' divisao = 10/3 - {:.2f} - :.2f .format(divisao)'.format(divisao))
print(f' divisao = 10/3 - {divisao:.2f} - divisao:.2f')

nome = 'Gustavo Hammes'
nome_formatado = '{:=^60}'.format(nome)
print(nome_formatado)
print(len(nome_formatado))
print()
nome_formatado = '{n:=^20}{n:=^20}{n:=^20}'.format(n=nome)
print(nome_formatado)
print(len(nome_formatado))
print()
nome1 = 'Gustavo'
nome2 = 'Hammes'
junta = '{1}, {0}, {1}'.format(nome1, nome2)
print(junta)
print(len(junta))
nome3 = "Gustavo hAmmes"
print(nome3.lower())
print(nome3.upper())
print(nome3.title())
print(nome3.isalpha())
print(nome3.capitalize())
print(nome3.casefold())
print(nome3.center())
print(nome3.endswith())

