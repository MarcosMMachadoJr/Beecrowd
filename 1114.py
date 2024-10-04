'''
Beecrowd: Problema 1114
21/04/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''
SenhaFixa = 2002
while True:
  senha = int(input())
  if senha == SenhaFixa:
    print('Acesso Permitido')
    break
  else:
    print('Senha Invalida')