from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()
print("You've completed the quiz")
print(f"Your final score is {quiz_brain.score}/{len(question_bank)}")






# question_bank[index] = Question(question_data[index]["text"], question_data[index]["answer"] )
#
# print(question_bank[0].text)
