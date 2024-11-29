'''
from collections import Counter

phones = ['iPhone XS', 'Samsung Galaxy S10', 'Xiaomi S18', 'iPhone XS', 'iPhone XS']
count = Counter(phones)
print(count['iPhone XS'], count['Hello'])

text = 'Ехал Грека через реку, видит ГРека в реке рак.'.lower().replace(' ', '')

count = Counter(text)
print(count)
'''

import ephem
mars = ephem.Mars('2000/01/01')
const = ephem.constellation(mars)
print(const)

