
class Questions:
    def __init__(self):
        # An array of questions and answers
        self.questions = ["What is another word for 'Hello'?", "What is the capital of Latvia?", "What is PI to 2 decimal places?"]
        self.answers = ["Hey", "Riga", "3.14"]
    # Method to retrieve the question
    def get_question(self, question_number):
        return self.questions[question_number]
    # Returns boolean after checking if answer is correct by the questions index. 
    def check_answer(self, question_number, answer):
        if answer == self.answers[question_number]:
            return True
        else:
            return False