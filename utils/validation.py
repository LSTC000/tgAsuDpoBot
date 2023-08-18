class Validator:
    def __init__(self):
        pass

    def alert_validation(self, alert: str) -> bool:
        """
        :param alert: Text for the alert.
        :return: True if alert is valid, else - False
        """

        return True if alert else False

    def question_validation(self, question: str) -> bool:
        """
        :param question: Text for the question.
        :return: True if question is valid, else - False
        """

        return True if len(question) <= 128 else False

    def answer_validation(self, answer: str) -> bool:
        """
        :param answer: Text for the answer.
        :return: True if answer is valid, else - False
        """

        return True if answer else False
