# TODO: ask the question
# TODO: check if the answer was correct
# TODO: check to see if we're at the end of the quiz

# QuizBrain class to manage the quiz questions
class QuizBrain:
    # Initialize the QuizBrain object with a list of questions (q_list)
    def __init__(self, q_list):
        # Set the initial question number to 0
        self.question_number = 0
        # Store the list of questions
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        # Check if there are still questions left in the question list
        return self.question_number < len(self.question_list)
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     False

    # Method to ask the next question
    def next_question(self):
        # Get the current question from the question list
        current_question = self.question_list[self.question_number]
        # Increment the question number for the next iteration
        self.question_number += 1
        # Prompt the user with the current question text
        user_answer = input(f"\nQ.{self.question_number}: {current_question.text} (True/False)\n")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("CORRECT!")
            self.score += 1
            print(f"Your score is {self.score}/{self.question_number}")
        else:
            print("Thats WRONG!")
            print(f"Your score is {self.score}/{self.question_number}")
        print(f"The correct answer is {correct_answer}.")





