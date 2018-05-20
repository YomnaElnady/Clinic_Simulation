import random
class Patient:

    def __init__(self, time):
        self.timeStart = time
        self.age = random.randrange(20, 61)

    def getAge(self):
        return  self.age

    def getTime(self):
        return self.timeStart

    def waitTime(self, currenttime):
        return currenttime - self.timeStart
