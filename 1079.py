'''
Beecrowd: Problema 1079
21/04/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''

X = int(input())
cont = 0
while(cont < X):
  a, b, c = input().split()
  a = float(a)
  b = float(b)
  c = float (c)
  mp = (a*2 + b*3 + c*5)/10
  print("%.1f"%mp)
  cont += 1