from testing import functionsObj

class globalVariables:

    #functionObj = functionsClass()
    def __init__(self):
        self.denominator = 0.03333333333333333333333333333333
        self.defaultSitY = -0.0336414869782
        self.defaultSitZ = 1.8546612215
        self.defaultLimitY = 0.105609899759
        self.defaultLimitZ = 1.8546612215
        self.defaultStandY = 0.35709164381
        self.defaultStandZ = 1.8246612215


    def addsitY(self):
        x = functionsObj.defaultSitY = functionsObj.defaultSitY + 0.0100000000000
        functionsObj.setSitY(x)
       # self.defaultSitY= self.defaultSitY + 0.0100000000000
        print self.defaultSitY
       # self.functionObj.setSitY(self.defaultSitY)


    def decSitY(self):
        self.defaultSitY = self.defaultSitY - 0.0100000000000
        print self.defaultSitY
        return self.defaultSitY

    def addSitZ(self):
        defaultSitZ = self.defaultSitZ + 0.0100000000000
        print self.defaultSitZ
        return defaultSitZ

    def decSitZ(self):
        self.defaultSitZ = self.defaultSitZ - 0.0100000000000
        print self.defaultSitZ
        return self.defaultSitZ




