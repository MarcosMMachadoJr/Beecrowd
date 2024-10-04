'''
Beecrowd: Problema 1075
21/04/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''
N = int(input())
for i in range(1, 10000):
  if i % N == 2:
    print(i)