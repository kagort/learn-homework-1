'''
for number in range(3):
    print(f'Номер{number}')

for letter in 'Python':
    print(letter.upper())

my_string = 'Привет , я учу Python !'
for word in my_string.split():
    print(f'Длина слова {word}: {len(word)}')

student_score = [3, 5, 4, 4, 2]
avg_score = 0
for score in student_score:
    avg_score = avg_score + score
class_avg = avg_score / len(student_score)
print(class_avg)
'''



stock = [
    {'name': 'iPhone 12', 'stock': 24, 'price': 65432,
     'discount': 25},
    {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000,
     'discount': 10},
    {'name': '', 'stock': 18, 'price': 10000,
     'discount': 10}
]
def discounted(price, discount,  max_discount = 30, phone_name = ''):
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
    phone['price_final'] = discounted(phone['price'], phone['discount'], phone_name = phone['name'])
print(stock)


classes = [
    {'name': '3А', 'scores': [3, 4, 4, 5, 2]},
    {'name': '3Б', 'scores': [5, 5, 3, 2, 2]},
    {'name': '3В', 'scores': [4, 5, 3, 5, 4]}
]

def count_class_avg(student_scores):
    scores_sum = 0
    for score in student_scores:
        scores_sum += score
    return scores_sum / (len(student_scores))

school_avg_sum = 0
for one_class in classes:
    class_avg = count_class_avg(one_class['scores'])
    print(f'Средняя оценка класса {one_class["name"]}: {class_avg}')
    school_avg_sum += class_avg
school_avg = round(school_avg_sum / len(classes), 2)
print(f'Средняя оценка по школе {school_avg}')

def total_sales(product_sold):
    # Функция для подсчёта суммарного количества продаж
    item_sold_sum = 0
    for sale in product_sold:
        item_sold_sum += sale
    return item_sold_sum

# Список данных
sales_data = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
]

# Подсчёт и вывод суммарного количества продаж для каждого товара
for item in sales_data:
    product = item['product']  # Название товара
    sales = item['items_sold']  # Список продаж
    total = total_sales(sales)  # Вызов функции с передачей списка продаж
    print(f"Суммарное количество продаж для {product}: {total}")
