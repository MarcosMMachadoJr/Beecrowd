'''
Beecrowd: Problema 1072
21/04/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''

N = int(input())

x = 0
y = 0 

for i in range(N):
  z = int(input())

  if z >= 10 and z <= 20:
    x += 1
  else:
    y += 1

print(f"{x} in")
print(f"{y} out")