from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for line in question_data:
    question = Question(line['text'], line['answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score: {quiz.score}/{len(quiz.question_list)}")