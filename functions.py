import sys
import math


class functionsClass():

    #variable = __import__('threshold').globalVariables.defaultSitY

    def __init__(self):
        self.denominator = 0.03333333333333333333333333333333
        self.defaultSitY = -0.0336414869782
        self.defaultSitZ = 1.8546612215
        self.defaultLimitY = 0.105609899759
        self.defaultLimitZ = 1.8546612215
        self.defaultStandY = 0.35709164381
        self.defaultStandZ = 1.8246612215


    def setSitY(self,defaultSitY):
        self.defaultSitY = defaultSitY

    def getSitY(self):
        return self.defaultSitY

    def recognize_sitting(self,totalY,totalZ):
        if totalY < self.defaultSitY and totalZ > self.defaultSitZ:
            print "EKATSE o paikths"

        elif totalY < self.defaultLimitY and totalZ > self.defaultLimitZ:
            print "Paei na katsei or shkwnetai"
        elif totalY > self.defaultStandY and totalZ > self.defaultStandZ:
            print "Orthios"
            print self.defaultSitY
        else:
            print "Den kathetai"
            print self.defaultSitY



    def recognize_hand_gesture(self,HandRightY):

        if HandRightY >= 0.201000000000:
            print "Right hand rised"
        print HandRightY


    def write_speed_Joints_To_Txt(self,HipCenterX, HipCenterY, HipCenterZ, HandRightX, HandRightY, HandRightZ, HandLeftX, HandLeftY, HandLeftZ, ElbowLeftX, ElbowLeftY, ElbowLeftZ,
                                  ElbowRightX, ElbowRightY, ElbowRightZ, WristLeftX, WristLeftY, WristLeftZ, WristRightX, WristRightY, WristRightZ, ShoulderLeftX, ShoulderLeftY,
                                  ShoulderLeftZ, ShoulderRightX, ShoulderRightY, ShoulderRightZ, ShoulderCenterX, ShoulderCenterY, ShoulderCenterZ, HeadX, HeadY, HeadZ, SpineX, SpineY, SpineZ,
                                  HipLeftX, HipLeftY, HipLeftZ, HipRightX, HipRightY, HipRightZ, KneeLeftX, KneeLeftY, KneeLeftZ, KneeRightX, KneeRightY, KneeRightZ,
                                  AnkleLeftX, AnkleLeftY, AnkleLeftZ, AnkleRightX, AnkleRightY, AnkleRightZ, FootRightX, FootRightY, FootRightZ, FootLeftX, FootLeftY, FootLeftZ):
        fo = open("logs.txt", 'a')
        #fo.truncate()

        fo.write("\n")
        fo.write("HipCenter speed xyz is: " + str(
            math.sqrt(HipCenterX ** 2 + HipCenterY ** 2 + HipCenterZ ** 2) / self.denominator) + "\n")

        fo.write("HandRight speed xyz is: " + str(
            math.sqrt(HandRightX ** 2 + HandRightY ** 2 + HandRightZ ** 2) / self.denominator) + "\n")

        fo.write("HandLeft speed xys is: " + str(
            math.sqrt(HandLeftX ** 2 + HandLeftY ** 2 + HandLeftZ ** 2) / self.denominator) + "\n")

        fo.write("ElbowLeft speed xys is: " + str(
            math.sqrt(ElbowLeftX ** 2 + ElbowLeftY ** 2 + ElbowLeftZ ** 2) /self.denominator) + "\n")

        fo.write("ElbowRight speed xys is: " + str(
            math.sqrt(ElbowRightX ** 2 + ElbowRightY ** 2 + ElbowRightZ ** 2) / self.denominator) + "\n")

        fo.write("WristLeft speed xys is: " + str(
            math.sqrt(WristLeftX ** 2 + WristLeftY ** 2 + WristLeftZ ** 2) / self.denominator) + "\n")

        fo.write("WristRight speed xys is: " + str(
            math.sqrt(WristRightX ** 2 + WristRightY ** 2 + WristRightZ ** 2) / self.denominator) + "\n")

        fo.write("ShoulderRight speed xyz is: " + str(
            math.sqrt(ShoulderRightX ** 2 + ShoulderRightY ** 2 + ShoulderRightZ ** 2) / self.denominator) + "\n")

        fo.write("ShoulderLeft speed xyz is: " + str(
            math.sqrt(ShoulderLeftX ** 2 + ShoulderLeftY ** 2 + ShoulderLeftZ ** 2) / self.denominator) + "\n")

        fo.write("ShoulderCenter speed xyz is: " + str(
            math.sqrt(ShoulderCenterX ** 2 + ShoulderCenterY ** 2 + ShoulderCenterZ ** 2) / self.denominator) + "\n")

        fo.write("Head speed xyz is: " + str(math.sqrt(HeadX ** 2 + HeadY ** 2 + HeadZ ** 2) / self.denominator) + "\n")

        fo.write("Spine speed xyz is: " + str(math.sqrt(SpineX ** 2 + SpineY ** 2 + SpineZ ** 2) / self.denominator) + "\n")

        fo.write(
            "HipLeft speed xyz is: " + str(math.sqrt(HipLeftX ** 2 + HipLeftY ** 2 + HipLeftZ ** 2) / self.denominator) + "\n")

        fo.write("HipRight speed xyz is: " + str(
            math.sqrt(HipRightX ** 2 + HipRightY ** 2 + HipRightZ ** 2) / self.denominator) + "\n")

        fo.write("KneeLeft speed xyz is: " + str(
            math.sqrt(KneeLeftX ** 2 + KneeLeftY ** 2 + KneeLeftZ ** 2) / self.denominator) + "\n")

        fo.write("KneeRight speed xyz is: " + str(
            math.sqrt(KneeRightX ** 2 + KneeRightY ** 2 + KneeRightZ ** 2) / self.denominator) + "\n")

        fo.write("AnkleLeft speed xyz is: " + str(
            math.sqrt(AnkleLeftX ** 2 + AnkleLeftY ** 2 + AnkleLeftZ ** 2) / self.denominator) + "\n")

        fo.write("AnkleRight speed xyz is: " + str(
            math.sqrt(AnkleRightX ** 2 + AnkleRightY ** 2 + AnkleRightZ ** 2) / self.denominator) + "\n")

        fo.write("FootRight speed xyz is: " + str(
            math.sqrt(FootRightX ** 2 + FootRightY ** 2 + FootRightZ ** 2) / self.denominator) + "\n")

        fo.write("FootLeft speed xyz is: " + str(
            math.sqrt(FootLeftX ** 2 + FootLeftY ** 2 + FootLeftZ ** 2) / self.denominator) + "\n")

        fo.write("---------------------------------------------------------------------")
        fo.close()