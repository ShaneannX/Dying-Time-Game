
from abc import ABC, abstractmethod

# Interface for Questions so each subclass must have following methods. 
class QuestionInterface(ABC):
    @abstractmethod
    def get_question(self, question_number):
        pass

    @abstractmethod
    def set_question(self, question, answer):
        pass

    @abstractmethod
    def check_answer(self, question_number, answer):
        pass

# Abstract for Questions, to share attribute and logic. Has abstract methods to be overridden by different question classes. 
class AbstractQuestions(QuestionInterface):
    def __init__(self):
        self.questions = []
        self.answers = []
    
    def set_question(self, question, answer):
        self.questions.append(question)
        self.answers.append(answer)

    @abstractmethod
    def get_question(self, question_number):
        return super().get_question(question_number)
    
    @abstractmethod
    def check_answer(self, question_number, answer):
        return super().check_answer(question_number, answer)

# Class for holding TriviaQuestions, inherits the abstract class to overright the abstract methods and inherits set_question method. 
class TriviaQuestions(AbstractQuestions):
    def __init__(self):
        # An array of questions and answers
        self.questions = ["What planet is known as the Red Planet?", "What is the capital of Latvia?", "What is PI to 2 decimal places?", "Which ocean is the largest in the world?", "How many legs does a spider have?"]
        self.answers = ["Mars", "Riga", "3.14", "Pacific Ocean", "8"]
    # Method to retrieve the question
    def get_question(self, question_number):
        return self.questions[question_number]
    # Method to add question with answer. 
    def set_question(self, question, answer):
        self.questions.append(question)
        self.answers.append(answer)
    # Returns boolean after checking if answer is correct by the questions index. 
    def check_answer(self, question_number, answer):
        return answer == self.answers[question_number]
        