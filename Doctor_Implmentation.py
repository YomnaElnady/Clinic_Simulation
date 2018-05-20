class Doctor:
    def __init__(self, number):
        self.patientAge = number
        self.currentPatient = None
        self.timeRemaning = 0

    def tickTock(self):
        if self.currentPatient != None:
            self.timeRemaning = self.timeRemaning - 1
            if self.timeRemaning == 0 :
                self.currentPatient = None

    def isBusy(self):
        if self.currentPatient != None:
            return True
        else:
            return False

    def startNext(self,newpatient):
        self.currentPatient = newpatient
        self.timeRemaning = ( (newpatient.getAge()) // (self.patientAge) ) * 60



