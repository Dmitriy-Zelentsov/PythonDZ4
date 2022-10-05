# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
import random
k = int(input('Введите натуральную степень k:'))
coeff=[random.randint(0,100) for i in range(k+1)]
print(coeff)
mnogoch='+'.join([f'{(i,"")[i==1]}x^{j}' for j, i in enumerate(coeff) if i][::-1])
mnogoch=mnogoch.replace('x^1+', 'x+')
mnogoch=mnogoch.replace('x^0', '')
mnogoch+=('','1')[mnogoch[-1] =='+']
mnogoch=(mnogoch, mnogoch[:-2])[mnogoch[-2:]=='^1']
with open('file.txt','w') as coeff:
    coeff.write(f'{mnogoch} = 0')
