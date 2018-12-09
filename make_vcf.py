from pandas import read_excel
import numpy as np

data = read_excel('Orgies.xlsx')
data = np.array(data)

for i in range(len(data)):
    data[i][0] += ' LIT ORGIE'

f = open('orgies.vcf', 'w+')

for i in data:
    f.write('BEGIN:VCARD\n')
    f.write('VERSION:3.0\n')
    f.write('N:;' + i[0] + ';;;\n')
    f.write('FN:' + i[0] + '\n')
    f.write('TEL;TYPE=CELL:' + str(i[1]) + '\n')
    f.write('END:VCARD\n')

f.close()
