# TODO - create a Question class with and __init()__ method with two attributes: text and answer attribute
class Question:
    def __init__(self, q_text, q_answer):
        # Set the value of the text attribute to the value of q_text
        self.text = q_text
        # Set the value of the answer attribute to the value of q_answer
        self.answer = q_answer


new_q = Question("Question", "Answer") # These are passed into the Question class.
# print(new_q.text) # To access the text
# print(new_q.answer)
