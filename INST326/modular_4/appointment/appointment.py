class Appointment:
    def __init__(self, name: str, start: tuple, end: tuple):
        self.name = name
        self.start = start
        self.end = end

    def overlaps(self, other):
        if self.start <= other.start < self.end or self.start <= other.end < self.end:
            return True
        else:
            return False

# appt1 = Appointment("dinner", (18, 00), (19, 00))
# print(appt1.name)