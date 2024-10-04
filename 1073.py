'''
Beecrowd: Problema 1073
21/04/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''
N = int(input())
for i in range(1, N+1):
  if i % 2 == 0:
    quadrado = i ** 2
    print(f'{i}^2 = {quadrado}')