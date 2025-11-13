
from abc import ABC, abstractmethod

# Interface for Questions so each subclass must have following methods. 
class QuestionInterface(ABC):
    @abstractmethod
    def get_question(self, question_number):
        pass

    @abstractmethod
    def set_new_question(self, question, answer):
        pass

    @abstractmethod
    def check_answer(self, question_number, answer):
        pass

# Abstract for Questions, to share attribute and logic. Has abstract methods to be overridden by different question classes. 
class AbstractQuestions(QuestionInterface):
    def __init__(self):
        self.__questions = []
        self.__answers = []
    
    def set_new_question(self, question, answer):
        self.__questions.append(question)
        self.__answers.append(answer)

    def get_question(self, question_number):
        return self.__questions[question_number]
    
    def get_answer(self, question_number):
        return self.__answers[question_number]
    @abstractmethod
    def check_answer(self, question_number, answer):
        pass

# Class for holding TriviaQuestions, inherits the abstract class to overright the abstract methods and inherits set_question method. 
class TriviaQuestions(AbstractQuestions):
    def __init__(self):
        super().__init__()
        # An array of questions and answers
        self.questions = ["What planet is known as the Red Planet?", "What is the capital of Latvia?", "What is PI to 2 decimal places?", "Which ocean is the largest in the world?", "How many legs does a spider have?"]
        self.answers = ["Mars", "Riga", "3.14", "Pacific Ocean", "8"]
        for idx in range(len(self.questions)):
            self.set_new_question(self.questions[idx],self.answers[idx])

    def set_new_question(self, question, answer):
        return super().set_new_question(question, answer)
    # Returns boolean after checking if answer is correct by the questions index. 
    def check_answer(self, question_number, answer):
        correct_answer = self.get_answer(question_number)
        return answer == correct_answer
        