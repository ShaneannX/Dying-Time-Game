class Characters:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__countdown = 100

    def get_countdown(self):
        return self.__countdown
    
    def set_countdown(self,value):
        if value >= 0:
            self.__countdown = value

class Player(Characters):
    def __init__(self, name, age):
        super().__init__(name, age)

class Hunter(Characters):
    def __init__(self, name, age):
        super().__init__(name, age)

p1 = Player("Shaneann", 27)
print(p1.name)    # Shaneann
print(p1.age)     # 27
print(p1.get_countdown())  # 100
