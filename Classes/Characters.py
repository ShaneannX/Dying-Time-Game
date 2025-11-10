class Characters:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__countdown = 100

    def get_countdown(self):
        return self.__countdown
    
    def add_countdown(self,value):
        if value <= self.__countdown:
            self.__countdown += value

    def subtract_countdown(self, value):
        if value <= self.__countdown:
            self.__countdown -= value

class Player(Characters):
    def __init__(self, name, age):
        super().__init__(name, age)

    opened_door = False
    
    position = 5

    def get_player_pos(self):
        return self.position
    
    def advance_player(self):
        
        if self.opened_door:
            print("door has been opened")
            self.position += 5

    def open_door(self):
        if not self.opened_door:
            self.opened_door = True
        self.add_countdown(10)
    
    def failed_to_open_door(self):
        if self.opened_door:
            self.opened_door = False
        self.subtract_countdown(10)
    

class Hunter(Player):
    def __init__(self, name, age, position):
        super().__init__(name, age, position = 0)
    
    def advance_to_player(self):

        hunter_pos = self.position + 1

        return hunter_pos
    
    def pos_from_player(self):
        return self.position


p1 = Player("Shaneann", 27)
print(p1.name)    # Shaneann
print(p1.age)     # 27
print(p1.get_countdown())  # 100

print(p1.open_door())
print(p1.get_countdown())
print(p1.failed_to_open_door())

print(p1.get_countdown())

print(p1.open_door())

print(p1.get_player_pos())

p1.advance_player()

print(p1.get_player_pos())


