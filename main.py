# Import the Question class and question data from question_model and data modules
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Initialize an empty list to store Question objects
question_bank = []

# Iterate over the question_data list
for question in question_data:
    # Extract the question text and answer from each dictionary
    question_text = question["question"]
    question_answer = question["correct_answer"]

    # Create a Question object using the extracted question text and answer
    new_question = Question(q_text=question_text, q_answer=question_answer)

    # Append each Question object to the question_bank list
    question_bank.append(new_question)

# Create a QuizBrain object and pass the question_bank list to it
quiz = QuizBrain(question_bank)

# Loop until there are no questions left
while quiz.still_has_questions():
    # Start the quiz by calling the next_question method of the QuizBrain object
    to_stop = input("Type exit to end program. Or press any key to continue\n")
    if to_stop.lower() == "exit":
        break
    else:
        quiz.next_question()
print(f" The quiz is over. Your final score was {quiz.score}")
