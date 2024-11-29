"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.

"""
stock = [
        {'name': 'iPhone 12', 'stock': 24, 'price': 65432,
         'discount': 25},
        {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000,
         'discount': 10},
        {'name': '', 'stock': 18, 'price': 10000,
         'discount': 10}
    ]

def discounted(price, discount, max_discount=20, phone_name=''):
    try:
        price = float(price)
        discount = float(discount)
        max_discount = int(max_discount)
    except(ValueError, TypeError):
        print('Ошибка в типе аргумента')
        return None


    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Максимальная скидка не должна быть больше 100')
    if discount >= max_discount:
        return price
    elif 'iphone' in phone_name.lower() or not phone_name:
        return price
    else:
        return price - (price * discount / 100)

    for phone in stock:
        price_final = discounted(phone['price'], phone['discount'], phone_name=phone('name'))
    if price_final is not None:
        phone['price_final'] = price_final
    else:
        print('Ошибка в расчетах')

print(discounted(100, 2))
print(discounted(100, "3"))
print(discounted("100", "4.5"))
print(discounted("five", 5))
print(discounted("сто", "десять"))
print(discounted(100.0, 5, "10"))



