'''
Beecrowd: Problema 1080
21/04/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''

y = 0
z = 0
for i in range(100):
  x = int(input())
  if(x > z):
     z = x
     y = i

print(z)  
print(y+1)