class Questions:
    def __init__(self):
        self.questions = ["What is another word for 'Hello'?", "What is the capital of Latvia?", "What is PI to 2 decimal places?"]
        self.answers = ["Hey", "Riga", "3.14"]

    def get_question(self, question_number):
        return self.questions[question_number]
    
    def check_answer(self, question_number, answer):
        if answer == self.answers[question_number]:
            return True
        else:
            return False