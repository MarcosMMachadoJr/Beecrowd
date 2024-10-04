'''
Beecrowd: Problema 1074
21/04/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''
N = int(input())

for X in range(1, N+1):
  X = int(input())
  if(X % 2 == 0) and (X > 0):
    print ("EVEN POSITIVE")
  elif (X % 2 != 0 ) and (X > 0):
    print ("ODD POSITIVE")
  elif (X == 0): 
    print ("NULL")
  elif (X % 2 == 0) and (X < 0):
    print ("EVEN NEGATIVE")
  elif (X % 2 != 0) and (X < 0):
    print ("ODD NEGATIVE")