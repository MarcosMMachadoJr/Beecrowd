'''
Beecrowd: Problema 1071
21/04/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''
x = int(input())
y = int(input())
SomaImpar = 0

if x > y:
  x, y = y, x

for i in range(x + 1, y):
  if i % 2 != 0:
    SomaImpar += i

print(SomaImpar)