from Queue_Implmentation import *

#from pythonds.basic.queue import Queue
from Doctor_Implmentation import *

from Patient_Implmentation import *

import random

def Simulation(numMins, number, breaktime):
    current = 0
    doctorMohamed = Doctor(number)
    clinicQueue = Queue()
    waitingTimes = []

    for currentMin in range (numMins):

        if random.randrange(1,7) == 6:
            current +=1
            patient = Patient(currentMin)
            clinicQueue.enqueue(patient)
        if currentMin >= (numMins // 2) and currentMin <= currentMin + breaktime:
            continue

        if (not doctorMohamed.isBusy() and (not clinicQueue.isEmpty())):
            nextPatient = clinicQueue.dequeue()
            waitingTimes.append(nextPatient.waitTime(currentMin))

            doctorMohamed.startNext(nextPatient)

        doctorMohamed.tickTock()

    averageWait = (sum(waitingTimes) / 60) / len(waitingTimes)
    #print(current)
    print("Average Wait", averageWait,"Mins", clinicQueue.size(),"patient remaining.")


for i in range (10):

    Simulation(14400,5,10)


