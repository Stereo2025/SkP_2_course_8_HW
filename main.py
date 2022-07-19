from utils import *
from random import shuffle

if __name__ == '__main__':

    # переменная с ссылкой на URL страницу.
    URL = 'https://jsonkeeper.com/b/3LQP'

    # результат работы ф-ии get_url_json: -> list
    database = get_url_json(URL)

    # результат работы ф-ии load_questions: -> list
    load = load_questions(database)

    # перемешиваем вопросы
    shuffle(load)
    for i in load:
        print('-' * 45)

        user_response = input(f'Вопрос: {i.build_question()}\n'
                              f'Ваш ответ >: ')

        # перезаписываем ответ пользователя с дефолтного None на текущий ответ.
        i.user_response = user_response

        # получаем фитбэк из класса Question, метода get_feedback
        print(i.get_feedback())
    # выводим статистику из get_statistics.
    print(get_statistics(load))
#########################################################################################
