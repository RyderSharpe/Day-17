# TODO - Bring question data into main. as a list of question objects.
from question_model import Question
from data import question_data

# TODO - Write a FOR loop to iterate over the question_data.
# TODO - Create a Question object from each entry in question_data.
# TODO - Append each Question object to the question_bank.

# Initialize question_bank as an empty list
question_bank = []

for question in question_data:
    # Extract the question text and answer from each dictionary.
    question_text = question["text"]
    question_answer = question["answer"]

    # Create a Question object using the extracted question text and answer.
    new_question = Question(q_text=question_text, q_answer=question_answer)

    # Append each Question object to the question_bank list.
    question_bank.append(new_question)

# Print the answer attribute of the first Question object in the question_bank list.
print(question_bank[0].answer)
print(question_bank[0].text)

QuizBrain(question_bank)
