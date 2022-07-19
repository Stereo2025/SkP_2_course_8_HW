class Question:

    def __init__(self, question_text, difficulty_level, correct_answer):
        """
        :param question_text: текст вопроса
        :param difficulty_level: сложность вопроса
        :param correct_answer: верный вариант ответа
        """
        self.question_text = question_text
        self.difficulty_level = difficulty_level
        self.correct_answer = correct_answer

        # Параметры заданные по умолчанию.
        self.asked_question = False
        self.user_response = None
        self.scores = self.difficulty_level * 10

    def get_points(self) -> int:
        """
        :return: Количество баллов. Баллы зависят от сложности.
        """
        return self.scores

    def is_correct(self) -> bool:
        """
        :return: True если ответ пользователя совпадает с верным ответом иначе False
        """
        return self.correct_answer == self.user_response

    def build_question(self):
        """
        :return: Вопрос для пользователя
        """
        return f'{self.question_text}\n' \
               f'Сложность: {self.difficulty_level}/5'

    def get_feedback(self):
        """
        :return: Ответ верный, получено ___ баллов или Ответ не верный, верный ответ ___
        """
        if self.is_correct():
            return f'Ответ верный, получено {self.scores} баллов'
        return f'Ответ не верный, верный ответ {self.correct_answer}'
#########################################################################################
