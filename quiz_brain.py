class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list  # question_list is the list of "Question" objects
        self.score = 0

    def next_question(self):
        q_number = self.question_number + 1
        q_text = self.question_list[self.question_number].text
        q_answer = (self.question_list[self.question_number].answer).lower()
        answer = input(f"Q.{q_number} {q_text} (True/False)??").lower()
        self.question_number += 1
        self.check_answer(answer, q_answer)     #note that self is already given as argument by "self." which is received
        # by self object


    def check_answer(self, answer, q_answer):
        if answer == q_answer:
            print("You are correct.")
            self.score += 1
            print(f"Your score is {self.score}/{self.question_number}.")
        else:
            print(f"Its not correct answer.\n Your score is {self.score}")
        print(f"The correct answer was {q_answer}")
        print("\n")



    def still_has_questions(self):
        return len(self.question_list) > self.question_number






