import sys
import math
from threshold import globalVariables


class functionsClass():

    def __init__(self):
        self.k = globalVariables()

    def recognize_sitting(self,totalY,totalZ):

        if totalY < self.k.defaultSitY and totalZ > self.k.defaultSitZ:
            print "EKATSE o paikths"
            print self.k.defaultSitZ
        elif totalY < self.k.defaultLimitY and totalZ > self.k.defaultLimitZ:
            print "Paei na katsei or shkwnetai"
        elif totalY > self.k.defaultStandY and totalZ > self.k.defaultStandZ:
            print "Orthios"
        else:
            print "Den kathetai"
            print self.k.defaultSitZ

    def write_speed_Joints_To_Txt(self,HipCenterX, HipCenterY, HipCenterZ, HandRightX, HandRightY, HandRightZ, HandLeftX, HandLeftY, HandLeftZ, ElbowLeftX, ElbowLeftY, ElbowLeftZ,
                                  ElbowRightX, ElbowRightY, ElbowRightZ, WristLeftX, WristLeftY, WristLeftZ, WristRightX, WristRightY, WristRightZ, ShoulderLeftX, ShoulderLeftY,
                                  ShoulderLeftZ, ShoulderRightX, ShoulderRightY, ShoulderRightZ, ShoulderCenterX, ShoulderCenterY, ShoulderCenterZ, HeadX, HeadY, HeadZ, SpineX, SpineY, SpineZ,
                                  HipLeftX, HipLeftY, HipLeftZ, HipRightX, HipRightY, HipRightZ, KneeLeftX, KneeLeftY, KneeLeftZ, KneeRightX, KneeRightY, KneeRightZ,
                                  AnkleLeftX, AnkleLeftY, AnkleLeftZ, AnkleRightX, AnkleRightY, AnkleRightZ, FootRightX, FootRightY, FootRightZ, FootLeftX, FootLeftY, FootLeftZ):
        fo = open("logs.txt", 'a')
        #fo.truncate()
        k = globalVariables()

        fo.write("\n")
        fo.write("HipCenter speed xyz is: " + str(
            math.sqrt(HipCenterX ** 2 + HipCenterY ** 2 + HipCenterZ ** 2) / k.denominator) + "\n")

        fo.write("HandRight speed xyz is: " + str(
            math.sqrt(HandRightX ** 2 + HandRightY ** 2 + HandRightZ ** 2) / k.denominator) + "\n")

        fo.write("HandLeft speed xys is: " + str(
            math.sqrt(HandLeftX ** 2 + HandLeftY ** 2 + HandLeftZ ** 2) / k.denominator) + "\n")

        fo.write("ElbowLeft speed xys is: " + str(
            math.sqrt(ElbowLeftX ** 2 + ElbowLeftY ** 2 + ElbowLeftZ ** 2) / k.denominator) + "\n")

        fo.write("ElbowRight speed xys is: " + str(
            math.sqrt(ElbowRightX ** 2 + ElbowRightY ** 2 + ElbowRightZ ** 2) / k.denominator) + "\n")

        fo.write("WristLeft speed xys is: " + str(
            math.sqrt(WristLeftX ** 2 + WristLeftY ** 2 + WristLeftZ ** 2) / k.denominator) + "\n")

        fo.write("WristRight speed xys is: " + str(
            math.sqrt(WristRightX ** 2 + WristRightY ** 2 + WristRightZ ** 2) / k.denominator) + "\n")

        fo.write("ShoulderRight speed xyz is: " + str(
            math.sqrt(ShoulderRightX ** 2 + ShoulderRightY ** 2 + ShoulderRightZ ** 2) / k.denominator) + "\n")

        fo.write("ShoulderLeft speed xyz is: " + str(
            math.sqrt(ShoulderLeftX ** 2 + ShoulderLeftY ** 2 + ShoulderLeftZ ** 2) / k.denominator) + "\n")

        fo.write("ShoulderCenter speed xyz is: " + str(
            math.sqrt(ShoulderCenterX ** 2 + ShoulderCenterY ** 2 + ShoulderCenterZ ** 2) / k.denominator) + "\n")

        fo.write("Head speed xyz is: " + str(math.sqrt(HeadX ** 2 + HeadY ** 2 + HeadZ ** 2) / k.denominator) + "\n")

        fo.write("Spine speed xyz is: " + str(math.sqrt(SpineX ** 2 + SpineY ** 2 + SpineZ ** 2) / k.denominator) + "\n")

        fo.write(
            "HipLeft speed xyz is: " + str(math.sqrt(HipLeftX ** 2 + HipLeftY ** 2 + HipLeftZ ** 2) / k.denominator) + "\n")

        fo.write("HipRight speed xyz is: " + str(
            math.sqrt(HipRightX ** 2 + HipRightY ** 2 + HipRightZ ** 2) / k.denominator) + "\n")

        fo.write("KneeLeft speed xyz is: " + str(
            math.sqrt(KneeLeftX ** 2 + KneeLeftY ** 2 + KneeLeftZ ** 2) / k.denominator) + "\n")

        fo.write("KneeRight speed xyz is: " + str(
            math.sqrt(KneeRightX ** 2 + KneeRightY ** 2 + KneeRightZ ** 2) / k.denominator) + "\n")

        fo.write("AnkleLeft speed xyz is: " + str(
            math.sqrt(AnkleLeftX ** 2 + AnkleLeftY ** 2 + AnkleLeftZ ** 2) / k.denominator) + "\n")

        fo.write("AnkleRight speed xyz is: " + str(
            math.sqrt(AnkleRightX ** 2 + AnkleRightY ** 2 + AnkleRightZ ** 2) / k.denominator) + "\n")

        fo.write("FootRight speed xyz is: " + str(
            math.sqrt(FootRightX ** 2 + FootRightY ** 2 + FootRightZ ** 2) / k.denominator) + "\n")

        fo.write("FootLeft speed xyz is: " + str(
            math.sqrt(FootLeftX ** 2 + FootLeftY ** 2 + FootLeftZ ** 2) / k.denominator) + "\n")

        fo.write("---------------------------------------------------------------------")
        fo.close()