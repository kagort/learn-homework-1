balance = 100
price = 50
in_stock = 0
print(bool(balance > price))
print(bool(in_stock))
if balance > price and in_stock:
    print('Одобряем оплату покупки')
elif not in_stock:
    print('Товара нет в наличии')
else:
    print('Пожалуйста, пополните баланс')

def check_weather(temperature):
    if temperature < 0:
        return 'На улице холодно'
    elif  0 <= temperature <= 15:
        return "На улице прохладно"
    elif 16 <= temperature <= 29:
        return 'На улице тепло'
    elif 30 <= temperature:
        return 'На улице жарко'
    else:
        return 'Не работает!'
print(check_weather(-10)) # На улице холодно
print(check_weather(15)) # На улице прохладно
print(check_weather(16)) # На улице тепло
print(check_weather(30)) # На улице жарко

def discounted(price, discount, max_discount = 20, phone_name = ''):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError('Максимальная скидка не должна быть больше 100')
    if discount >= max_discount:
       return  price
    elif 'iphone' in phone_name.lower() or not phone_name:
        return price
    else:
        return price - (price * discount / 100)
new_price = discounted(100000, 10, phone_name = 'iPhone 12')
print(new_price)
new_price = discounted(40000, 20, phone_name='Samsung Galaxy S21' )
print(new_price)
new_price = discounted(5000, 20) # Здесь возникает вопрос. Почему в выводе скидка не считается?
print(new_price)
