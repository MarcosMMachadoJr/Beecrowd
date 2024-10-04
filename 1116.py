'''
Beecrowd: Problema 1116
21/04/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''

z = int(input())

for i in range(1, z + 1):
  x,y = map(int, input().split())
  if y == 0:
    print("divisao impossivel")
    
  if y != 0:
    divisor = x/y
    print("%.1f"%divisor)