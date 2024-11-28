"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

def hello_user():
    """
    Замените pass на ваш код
    """
    try:
        while True:
            user_say = input('Как дела?')
            if user_say == 'Хорошо':
                print('Ничего хорошего!')
                break
            else:
                print('Попробуем ещё раз?'.format(user_say))
    except KeyboardInterrupt:
        print("Исполнение программы остановлено пользователем")


if __name__ == "__main__":
    hello_user()
