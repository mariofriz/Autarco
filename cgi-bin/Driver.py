# coding=utf-8
class Driver:
    #gpio 0 et 1 liés (0 out, 1 in)
    #gpio 2 et 3 liés (2 out, 3 in)
    #gpio 2 : compteur d'eau
    gpioLights = [4,5]
    gpioSprinklers=[6,7]
    gpioPump=17

    def __init__(self):
        raise NotImplementedError

    def getGPIO(self,index):
        raise NotImplementedError

    def setGPIO(self,index,value):
        raise NotImplementedError

    #Lumières
    def setLight(self,index,value):
        self.setGPIO(self.gpioLights[index],int(value))

    def getLight(self,index):
        return self.getGPIO(self.gpioLights[index])

    #Jets d'eau
    def setSprinkler(self,index,value):
        self.setGPIO(self.gpioSprinklers[index],int(value))

    def getSprinkler(self,index):
        return self.getGPIO(self.gpioSprinklers[index])

    #Pompe
    def getPump(self):
        return self.getGPIO(self.gpioPump)

    def setPump(self,value):
        self.setGPIO(self.gpioPump,value)





