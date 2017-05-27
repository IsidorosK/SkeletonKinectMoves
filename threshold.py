
class globalVariables:
    def __init__(self):
        self.denominator = 0.03333333333333333333333333333333
        self.defaultSitY = -0.0336414869782
        self.defaultSitZ = 1.8546612215
        self.defaultLimitY = 0.105609899759
        self.defaultLimitZ = 1.8546612215
        self.defaultStandY = 0.35709164381
        self.defaultStandZ = 1.8246612215

    def addsitY(self):
        self.defaultSitY = self.defaultSitY + 0.0000100000000
        return self.defaultSitY

    def decSitY(self):
        self.defaultSitY = self.defaultSitY - 0.0000100000000
        return self.defaultSitY

    def addSitZ(self):
        self.defaultSitZ = self.defaultSitZ + 0.0000100000000
        return self.defaultSitZ

    def decSitZ(self):
        self.defaultSitZ = self.defaultSitZ - 0.0000100000000
        return self.defaultSitZ




