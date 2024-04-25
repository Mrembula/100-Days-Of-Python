from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
answer_bank = []

for data in question_data:
    question_text = data['text']
    question_answer = data['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():  # if quiz still has questions remaining
    quiz.next_question()

score, number_of_questions = quiz.score, quiz.question_number
print("You've completed the quiz")
print(f"Your final score was: {score}/{number_of_questions}")