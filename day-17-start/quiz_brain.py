class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f'Q.{self.question_number + 1}: {current_question.text} (True/False): ')
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong")
            print(f"It was {correct_answer.lower()}!")
        print(f"Your current score is: {self.score}/{len(self.question_list)}")
        print("\n")
    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
