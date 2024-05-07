# TODO: ask the question
# TODO: check if the answer was correct
# TODO: check to see if we're at the end of the quiz

class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
    def next_question(self):
        print(f"Q.{self.question_number}")

