'''
Beecrowd: Problema 1117
21/04/2024
Prof. Gregory --> Marcos Marçal Machado Junior
'''

nota = 0
N = 0
media = 0
while nota != 2:
    N = float(input())
    if N >= 0 and N <= 10:
        media += (N / 2)
        nota += 1
    else:
        print("nota invalida")
      
print('media = %.2f'%(media))