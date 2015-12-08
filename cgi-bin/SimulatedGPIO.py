# coding=utf-8
class SimulatedGPIO:
    #state 0 ==> in
    #state 1 ==> out

    state = 0
    value = 0

    def getState(self):
        return self.state

    def setState(self,state):
        if state == 0 or state == 1:
            self.state = state

    def getValue(self):
        return self.value

    def setValue(self,value):
        self.value = value
