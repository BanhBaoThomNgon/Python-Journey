class Car:
    def __init__(self, x = 0, y = 0, heading = 'n'):
        self.x = x
        self.y = y
        self.heading = heading

    def turn(self, direction: str):
        if (self.heading == 'n' and direction == 'r'):
            self.heading = 'e'
        elif (self.heading == 'n' and direction == 'l'):
            self.heading = 'w'
        elif (self.heading == 'e' and direction == 'r'):
            self.heading ='s'
        elif (self.heading == 'e' and direction == 'l'):
            self.heading = 'n'
        elif (self.heading == 'w' and direction == 'r'):
            self.heading ='n'
        elif (self.heading == 'w' and direction == 'l'):
            self.heading = 's'
        elif (self.heading =='s' and direction == 'r'):
            self.heading = 'w'
        elif (self.heading =='s' and direction == 'l'):
            self.heading = 'e'

    def drive(self, distance: int):
        if (self.heading == 'n'):
            self.x += distance
        elif (self.heading == 's'):
            self.x -= distance
        elif (self.heading == 'e'):
            self.y += distance
        elif (self.heading == 'w'):
            self.y -= distance

    def status(self):
        print(f"Coordinates: ({self.x}, {self.y})\nHeading: {self.heading}")