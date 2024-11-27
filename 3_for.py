"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по количеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    sales_data_base = [
        {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]
    def total_sales(product_sold): #Функция суммирует продажи по продукту
        item_sold_sum = 0
        for sale in product_sold:
            item_sold_sum += sale
        return item_sold_sum
    def sales_avg(product_sold):      #Функция суммирует средние продажи по продукту
        total = 0
        for sale in product_sold:
            total += sale
        return total / len(product_sold)

    def total_sales_all (all_products): #Функция суммирует суммы продаж по продукту
        total_sum = 0
        for item in all_products:
            total_sum += total_sales(item['items_sold'])
        return total_sum
    def total_sales_avg (all_products): #Функция считает средние продажи по базе
        total_sum = 0
        total_items = 0
        for item in all_products:
            total_sum += sum(item['items_sold'])
            total_items += len(item['items_sold'])
        return total_sum / total_items



    # Cуммарноe количества продаж для каждого продукта
    for item in sales_data_base:
        product = item['product']  # Название товара
        sales = item['items_sold']  # Список продаж
        total = total_sales(sales)  # Вызов функции с передачей списка продаж
        print(f"Суммарное количество продаж для {product}: {total}")


    #Cреднее количество продаж для каждого продукта
    for item in sales_data_base:
        product = item['product']
        sales = item['items_sold']
        avg = round(sales_avg(sales), 2)
        print(f"Среднее количество продаж для {product}: {avg}")

    #Cуммарное количество продаж всех товаров
    total_sales = total_sales_all(sales_data_base)
    print(f'Общие продажи составляют {total_sales}')

    #Среднее количество продаж всех товаров
    total_sales_average = total_sales_avg(sales_data_base)
    print(f'Средние продажи по всей базе товаров составляют {total_sales_average}')


if __name__ == "__main__":
    main()
