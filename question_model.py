# TODO - create a Question class with and __init()__ method with two attributes: text and answer attribute
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text # attribute
        self.answer = q_answer # attribute


new_q = Question("Question", "answer") # These are passed into the Question class.
print(new_q.text) # To access the text
