# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов. 
# 2*x² + 4*x + 5 3*x² +10*x + 6 Вывод: 5*x² + 14*x + 11

import sympy
x = sympy.Symbol('x')
with open('Ex4.1.txt','r') as a:
    firstpol=a.read()
    print(firstpol)
with open('Ex4.2.txt','r') as b:
    secondpol=b.read()
    print(secondpol)
summpol = sympy.simplify(firstpol+'+'+secondpol)
with open("Ex4summ.txt",'w') as summ:
  summ.write(f'{str(summpol)} = 0')
  print(str(summpol))
    