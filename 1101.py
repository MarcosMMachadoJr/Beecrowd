'''
Beecrowd: Problema 1101
21/04/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''

while True:
  M, N =  input().split()
  M = int (M)
  N = int (N)
  if M <= 0 or N <= 0:
      break
  
  soma = 0
  
  if M > N:
      M, N = N, M
  
  for i in range(M, N + 1):
      print(i, end=" ")
      soma += i
  
  print(f"Sum={soma}")