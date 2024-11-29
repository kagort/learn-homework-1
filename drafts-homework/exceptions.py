
import random
def  cutcake (people):
    try:
        z = 1/people
        print(f'Каждый получит {z} пирога')
    except (ZeroDivisionError, TypeError):
        print('Не могу поделить')

while True:
    p = random.randint(1, 10)
    cutcake(p)