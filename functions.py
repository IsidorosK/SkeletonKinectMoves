from testing import *
import math
from threshold import globalVariables

class functionsClass():

    def __init__(self):
        pass

    def recognize_sitting(totalY,totalZ):
        k = globalVariables()

        if totalY < k.newSitY and totalZ > k.newSitZ:
            print "EKATSE o paikths"
            print k.newSitY
        elif totalY > -0.02854367834 and totalZ > 1.8546612215:
            print "Player sit"
        elif totalY < 0.0407887405232 and totalZ < 1.8546612215 and totalZ > 1.2546612215:
            print totalY
            print "Kathetai"
        elif totalY < k.newLimitY and totalZ > k.newLimitZ:
            print "Paei na katsei or shkwnetai"
        elif totalY > k.newStandY and totalZ > k.newStandZ:
            print "Orthios"
        else:
            print "Den kathetai"
            print totalY



    def write_speed_Joints_To_Txt(HipCenterX, HipCenterY, HipCenterZ, HandRightX, HandRightY, HandRightZ, HandLeftX, HandLeftY, HandLeftZ, ElbowLeftX, ElbowLeftY, ElbowLeftZ,
                                  ElbowRightX, ElbowRightY, ElbowRightZ, WristLeftX, WristLeftY, WristLeftZ, WristRightX, WristRightY, WristRightZ, ShoulderLeftX, ShoulderLeftY,
                                  ShoulderLeftZ, ShoulderRightX, ShoulderRightY, ShoulderRightZ, ShoulderCenterX, ShoulderCenterY, ShoulderCenterZ, HeadX, HeadY, HeadZ, SpineX, SpineY, SpineZ,
                                  HipLeftX, HipLeftY, HipLeftZ, HipRightX, HipRightY, HipRightZ, KneeLeftX, KneeLeftY, KneeLeftZ, KneeRightX, KneeRightY, KneeRightZ,
                                  AnkleLeftX, AnkleLeftY, AnkleLeftZ, AnkleRightX, AnkleRightY, AnkleRightZ, FootRightX, FootRightY, FootRightZ, FootLeftX, FootLeftY, FootLeftZ):
        fo = open("logs.txt", 'a')
        #fo.truncate()
        paronomastis = 0.03333333333333333333333333333333
        fo.write("\n")

        fo.write("HipCenter speed xyz is: " + str(
            math.sqrt(HipCenterX ** 2 + HipCenterY ** 2 + HipCenterZ ** 2) / paronomastis) + "\n")

        fo.write("HandRight speed xyz is: " + str(
            math.sqrt(HandRightX ** 2 + HandRightY ** 2 + HandRightZ ** 2) / paronomastis) + "\n")

        fo.write("HandLeft speed xys is: " + str(
            math.sqrt(HandLeftX ** 2 + HandLeftY ** 2 + HandLeftZ ** 2) / paronomastis) + "\n")

        fo.write("ElbowLeft speed xys is: " + str(
            math.sqrt(ElbowLeftX ** 2 + ElbowLeftY ** 2 + ElbowLeftZ ** 2) / paronomastis) + "\n")

        fo.write("ElbowRight speed xys is: " + str(
            math.sqrt(ElbowRightX ** 2 + ElbowRightY ** 2 + ElbowRightZ ** 2) / paronomastis) + "\n")

        fo.write("WristLeft speed xys is: " + str(
            math.sqrt(WristLeftX ** 2 + WristLeftY ** 2 + WristLeftZ ** 2) / paronomastis) + "\n")

        fo.write("WristRight speed xys is: " + str(
            math.sqrt(WristRightX ** 2 + WristRightY ** 2 + WristRightZ ** 2) / paronomastis) + "\n")

        fo.write("ShoulderRight speed xyz is: " + str(
            math.sqrt(ShoulderRightX ** 2 + ShoulderRightY ** 2 + ShoulderRightZ ** 2) / paronomastis) + "\n")

        fo.write("ShoulderLeft speed xyz is: " + str(
            math.sqrt(ShoulderLeftX ** 2 + ShoulderLeftY ** 2 + ShoulderLeftZ ** 2) / paronomastis) + "\n")

        fo.write("ShoulderCenter speed xyz is: " + str(
            math.sqrt(ShoulderCenterX ** 2 + ShoulderCenterY ** 2 + ShoulderCenterZ ** 2) / paronomastis) + "\n")

        fo.write("Head speed xyz is: " + str(math.sqrt(HeadX ** 2 + HeadY ** 2 + HeadZ ** 2) / paronomastis) + "\n")

        fo.write("Spine speed xyz is: " + str(math.sqrt(SpineX ** 2 + SpineY ** 2 + SpineZ ** 2) / paronomastis) + "\n")

        fo.write(
            "HipLeft speed xyz is: " + str(math.sqrt(HipLeftX ** 2 + HipLeftY ** 2 + HipLeftZ ** 2) / paronomastis) + "\n")

        fo.write("HipRight speed xyz is: " + str(
            math.sqrt(HipRightX ** 2 + HipRightY ** 2 + HipRightZ ** 2) / paronomastis) + "\n")

        fo.write("KneeLeft speed xyz is: " + str(
            math.sqrt(KneeLeftX ** 2 + KneeLeftY ** 2 + KneeLeftZ ** 2) / paronomastis) + "\n")

        fo.write("KneeRight speed xyz is: " + str(
            math.sqrt(KneeRightX ** 2 + KneeRightY ** 2 + KneeRightZ ** 2) / paronomastis) + "\n")

        fo.write("AnkleLeft speed xyz is: " + str(
            math.sqrt(AnkleLeftX ** 2 + AnkleLeftY ** 2 + AnkleLeftZ ** 2) / paronomastis) + "\n")

        fo.write("AnkleRight speed xyz is: " + str(
            math.sqrt(AnkleRightX ** 2 + AnkleRightY ** 2 + AnkleRightZ ** 2) / paronomastis) + "\n")

        fo.write("FootRight speed xyz is: " + str(
            math.sqrt(FootRightX ** 2 + FootRightY ** 2 + FootRightZ ** 2) / paronomastis) + "\n")

        fo.write("FootLeft speed xyz is: " + str(
            math.sqrt(FootLeftX ** 2 + FootLeftY ** 2 + FootLeftZ ** 2) / paronomastis) + "\n")

        fo.write("---------------------------------------------------------------------")
        fo.close()