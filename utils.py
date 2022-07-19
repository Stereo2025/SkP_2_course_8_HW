import requests
from class_question import Question


def get_url_json(url_source: str) -> list:
    """
    :param url_source: URL ссылка/адрес на json файл.
    :return: получаем "возвращаем" список согласно ТЗ.
    """
    response = requests.get(url_source)
    result = response.json()
    return result


def load_questions(database: list) -> list:
    """
    Создаём экземпляр класса, на каждой итерации цикла записываем его в список с ссылкой
    по ключам из обработанного Json файла.
    :param database: обработанный json
    :return: список вопросов.
    """

    questions = []
    for i in database:
        # присвоение данных инициализированным переменным по ключам из обработанного Json.
        question_text = i['q']
        # int, потому что difficulty_level это str, а при умножении строки на число
        # получается не int, а строка * на 10.
        difficulty_level = int(i['d'])
        correct_answer = i['a']

        # Экземпляр класса Question с "инициализированными" аргументами.
        question_1 = Question(question_text, difficulty_level, correct_answer)
        questions.append(question_1)

    return questions


def get_statistics(statistics: list) -> str:
    """
    Получает статистику.
    :param statistics: список с вопросами на которые уже пользователь ответил.
    :return: Вывод статистики
    """
    # текущий счет и кол-во правильных ответов.
    scores, count = 0, 0

    # цикл по вопросам
    for i in statistics:
        if i.is_correct():
            # увеличиваем на кол-во баллов, которые даются за текущий вопрос
            scores += i.scores
            count += 1

    return f'Вот и всё ! Отвечено {count} вопросов из 10.\n' \
           f'Набрано баллов: {scores}'
#########################################################################################
