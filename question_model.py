# TODO - create a Question class with and __init()__ method with two attributes: text and answer attribute
# Create a Question class
class Question:
    # Initialize the Question object with two attributes: text and answer
    def __init__(self, q_text, q_answer):
        # Set the value of the text attribute to the value of q_text
        self.text = q_text
        # Set the value of the answer attribute to the value of q_answer
        self.answer = q_answer

# Create an instance of the Question class
new_q = Question("Question", "Answer")
# Print the text attribute of the new Question object
# print(new_q.text)
# Print the answer attribute of the new Question object
# print(new_q.answer)

