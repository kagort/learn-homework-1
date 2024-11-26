"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные параметры
  и выводя на экран результаты

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
def check_lines(line1, line2):
    if not type(line1) == str or not type(line2) == str:
        return 0
    elif line1 == line2:
        return 1
    elif len(line1) > len(line2):
        return 2
    elif line1 != line2 and line2 == 'learn':
        return 3

print(check_lines("Bigwall", "Bigwall"))   # 1
print(check_lines("Bigwall", "wallBig"))   # None
print(check_lines("learn", "learn"))    # 1
print(check_lines("Python", "learn"))   # 3
print(check_lines("longerstring", "short"))  # 2
print(check_lines(123, "str"))      # 0
print(check_lines("str", 123))     # 0

if __name__ == "__main__":
    main()
