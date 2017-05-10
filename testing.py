# PyKinect

# Copyright(c) Microsoft Corporation

# All rights reserved.

#

# Licensed under the Apache License, Version 2.0 (the License); you may not use

# this file except in compliance with the License. You may obtain a copy of the

# License at http://www.apache.org/licenses/LICENSE-2.0

#

# THIS CODE IS PROVIDED ON AN  *AS IS* BASIS, WITHOUT WARRANTIES OR CONDITIONS

# OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION ANY

# IMPLIED WARRANTIES OR CONDITIONS OF TITLE, FITNESS FOR A PARTICULAR PURPOSE,

# MERCHANTABLITY OR NON-INFRINGEMENT.

#

# See the Apache Version 2.0 License for specific language governing

# permissions and limitations under the License.

import thread

import itertools

import ctypes

from pykinect import nui
from pykinect.nui import JointId
import pygame
from pygame.color import THECOLORS
from pygame.locals import *
import time
import functions,gui
import winsound
from PyQt4 import QtGui,QtCore


KINECTEVENT = pygame.USEREVENT

DEPTH_WINSIZE = 320, 240

VIDEO_WINSIZE = 640, 480

pygame.init()

SKELETON_COLORS = [THECOLORS["red"],
                   THECOLORS["blue"],
                   THECOLORS["green"],
                   THECOLORS["orange"],
                   THECOLORS["purple"],
                   THECOLORS["yellow"],
                   THECOLORS["violet"]]

LEFT_ARM = (JointId.ShoulderCenter,
            JointId.ShoulderLeft,
            JointId.ElbowLeft,
            JointId.WristLeft,
            JointId.HandLeft)

RIGHT_ARM = (JointId.ShoulderCenter,
             JointId.ShoulderRight,
             JointId.ElbowRight,
             JointId.WristRight,
             JointId.HandRight)

LEFT_LEG = (JointId.HipCenter,
            JointId.HipLeft,
            JointId.KneeLeft,
            JointId.AnkleLeft,
            JointId.FootLeft)

RIGHT_LEG = (JointId.HipCenter,
             JointId.HipRight,
             JointId.KneeRight,
             JointId.AnkleRight,
             JointId.FootRight)

SPINE = (JointId.HipCenter,
         JointId.HipRight,
         JointId.HipLeft,
         JointId.Spine,
         JointId.ShoulderCenter,
         JointId.Head)

skeleton_to_depth_image = nui.SkeletonEngine.skeleton_to_depth_image

#initialize X Y Z for each joint with public variable

#right hand-arm
HandRightX=HandRightY=HandRightZ=0
WristRightX=WristRightY=WristRightZ=0
ElbowRightX=ElbowRightY=ElbowRightZ=0
ShoulderRightX=ShoulderRightY=ShoulderRightZ=0

#right leg
HipRightX=HipRightY=HipRightZ=0
KneeRightX=KneeRightY=KneeRightZ=0
AnkleRightX=AnkleRightY=AnkleRightZ=0
FootRightX=FootRightY=FootRightZ=0

#left leg
HipLeftX=HipLeftY=HipLeftZ=0
KneeLeftX=KneeLeftY=KneeLeftZ=0
AnkleLeftX=AnkleLeftY=AnkleLeftZ=0
FootLeftX=FootLeftY=FootLeftZ=0

#left hand-arm
HandLeftX=HandLeftY=HandLeftZ=0
WristLeftX=WristLeftY=WristLeftZ=0
ElbowLeftX=ElbowLeftY=ElbowLeftZ=0
ShoulderLeftX=ShoulderLeftY=ShoulderLeftZ=0

#spine
HipCenterX=HipCenterY=HipCenterZ=0
SpineX=SpineY=SpineZ=0
ShoulderCenterX=ShoulderCenterY=ShoulderCenterZ=0
HeadX=HeadY=HeadZ=0

#initialize variables for instant measure for specific jointId
RightHandY=headY=RightShoulderY=LeftShoulderY=CenterShoulderY=CenterHipY=0
RightHandZ=headZ=RightShoulderZ=LeftShoulderZ=CenterShoulderZ=CenterHipZ=0


def draw_skeleton_data(pSkelton, index, positions, width=4):
    start = pSkelton.SkeletonPositions[positions[0]]

    for position in itertools.islice(positions, 1, None):
        next = pSkelton.SkeletonPositions[position.value]

        curstart = skeleton_to_depth_image(start, dispInfo.current_w, dispInfo.current_h)

        curend = skeleton_to_depth_image(next, dispInfo.current_w, dispInfo.current_h)

        pygame.draw.line(screen, SKELETON_COLORS[index], curstart, curend, width)

        start = next


# recipe to get address of surface: http://archives.seul.org/pygame/users/Apr-2008/msg00218.html

if hasattr(ctypes.pythonapi, 'Py_InitModule4'):

    Py_ssize_t = ctypes.c_int

elif hasattr(ctypes.pythonapi, 'Py_InitModule4_64'):

    Py_ssize_t = ctypes.c_int64

else:

    raise TypeError("Cannot determine type of Py_ssize_t")

_PyObject_AsWriteBuffer = ctypes.pythonapi.PyObject_AsWriteBuffer

_PyObject_AsWriteBuffer.restype = ctypes.c_int

_PyObject_AsWriteBuffer.argtypes = [ctypes.py_object,

                                    ctypes.POINTER(ctypes.c_void_p),

                                    ctypes.POINTER(Py_ssize_t)]


def surface_to_array(surface):
    buffer_interface = surface.get_buffer()

    address = ctypes.c_void_p()

    size = Py_ssize_t()

    _PyObject_AsWriteBuffer(buffer_interface,

                            ctypes.byref(address), ctypes.byref(size))

    bytes = (ctypes.c_byte * size.value).from_address(address.value)

    bytes.object = buffer_interface

    return bytes


def draw_skeletons(skeletons):
    for index, data in enumerate(skeletons):
        # draw the Head

        HeadPos = skeleton_to_depth_image(data.SkeletonPositions[JointId.Head], dispInfo.current_w, dispInfo.current_h)

        draw_skeleton_data(data, index, SPINE, 10)

        pygame.draw.circle(screen, SKELETON_COLORS[index], (int(HeadPos[0]), int(HeadPos[1])), 20, 0)

        # drawing the limbs
        draw_skeleton_data(data, index, LEFT_ARM)
        draw_skeleton_data(data, index, RIGHT_ARM)
        draw_skeleton_data(data, index, LEFT_LEG)
        draw_skeleton_data(data, index, RIGHT_LEG)

        #subtract previous x,y,z position for each jointId to measure speed gesture

        if data.SkeletonPositions[JointId.HandRight].y != 0.0 and data.SkeletonPositions[JointId.HandRight].x != 0.0 and data.SkeletonPositions[JointId.HandRight].z != 0.0:
            global HandRightX, HandRightY, HandRightZ
            HandRightY = data.SkeletonPositions[JointId.HandRight].y - HandRightY
            HandRightX = data.SkeletonPositions[JointId.HandRight].x - HandRightX
            HandRightZ = data.SkeletonPositions[JointId.HandRight].z - HandRightZ

        if data.SkeletonPositions[JointId.HipCenter].x!=0.0 and data.SkeletonPositions[JointId.HipCenter].y!=0.0 and data.SkeletonPositions[JointId.HipCenter].z!=0.0:
            global HipCenterX,HipCenterY,HipCenterZ
            HipCenterX=data.SkeletonPositions[JointId.HipCenter].x - HipCenterX
            HipCenterY=data.SkeletonPositions[JointId.HipCenter].y - HipCenterY
            HipCenterZ=data.SkeletonPositions[JointId.HipCenter].z - HipCenterZ

        if data.SkeletonPositions[JointId.HandLeft].x!=0.0 and data.SkeletonPositions[JointId.HandLeft].y!=0.0 and data.SkeletonPositions[JointId.HandLeft].z!=0.0:
            global HandLeftX,HandLeftY,HandLeftZ
            HandLeftX=data.SkeletonPositions[JointId.HandLeft].x - HandLeftX
            HandLeftY=data.SkeletonPositions[JointId.HandLeft].y - HandLeftY
            HandLeftZ=data.SkeletonPositions[JointId.HandLeft].z - HandLeftZ

        if data.SkeletonPositions[JointId.AnkleLeft].x!=0.0 and data.SkeletonPositions[JointId.AnkleLeft].y!=0.0 and data.SkeletonPositions[JointId.AnkleLeft].z!=0.0:
            global AnkleLeftX,AnkleLeftY,AnkleLeftZ
            AnkleLeftX=data.SkeletonPositions[JointId.AnkleLeft].x-AnkleLeftX
            AnkleLeftY=data.SkeletonPositions[JointId.AnkleLeft].y-AnkleLeftY
            AnkleLeftZ=data.SkeletonPositions[JointId.AnkleLeft].z-AnkleLeftZ

        if data.SkeletonPositions[JointId.AnkleRight].x!=0.0 and data.SkeletonPositions[JointId.AnkleRight].y!=0.0 and data.SkeletonPositions[JointId.AnkleRight].z!=0.0:
            global AnkleRightX,AnkleRightY,AnkleRightZ
            AnkleRightX=data.SkeletonPositions[JointId.AnkleLeft].x-AnkleRightX
            AnkleRightY=data.SkeletonPositions[JointId.AnkleLeft].y-AnkleRightY
            AnkleRightZ=data.SkeletonPositions[JointId.AnkleLeft].z-AnkleRightZ

        if data.SkeletonPositions[JointId.HipLeft].x!=0.0 and data.SkeletonPositions[JointId.HipLeft].y!=0.0 and data.SkeletonPositions[JointId.HipLeft].z!=0.0:
            global HipLeftX,HipLeftY,HipLeftZ
            HipLeftX=data.SkeletonPositions[JointId.HipLeft].x-HipLeftX
            HipLeftY=data.SkeletonPositions[JointId.HipLeft].y-HipLeftY
            HipLeftZ=data.SkeletonPositions[JointId.HipLeft].z-HipLeftZ

        if data.SkeletonPositions[JointId.HipRight].x!=0.0 and data.SkeletonPositions[JointId.HipRight].y!=0.0 and data.SkeletonPositions[JointId.HipRight].z!=0.0:
            global HipRightX,HipRightY,HipRightZ
            HipRightX=data.SkeletonPositions[JointId.HipRight].x-HipRightX
            HipRightY=data.SkeletonPositions[JointId.HipRight].y-HipRightY
            HipRightZ=data.SkeletonPositions[JointId.HipRight].z-HipRightZ

        if data.SkeletonPositions[JointId.Spine].x!=0.0 and data.SkeletonPositions[JointId.Spine].y!=0.0 and data.SkeletonPositions[JointId.Spine].z!=0.0:
            global SpineX,SpineY,SpineZ
            SpineX=data.SkeletonPositions[JointId.Spine].x-SpineX
            SpineY=data.SkeletonPositions[JointId.Spine].y-SpineY
            SpineZ=data.SkeletonPositions[JointId.Spine].z-SpineZ

        if data.SkeletonPositions[JointId.Head].x!=0.0 and data.SkeletonPositions[JointId.Head].y!=0.0 and data.SkeletonPositions[JointId.Head].z!=0.0:
            global HeadX,HeadY,HeadZ
            HeadX=data.SkeletonPositions[JointId.Head].x-HeadX
            HeadY=data.SkeletonPositions[JointId.Head].y-HeadY
            HeadZ=data.SkeletonPositions[JointId.Head].z-HeadZ

        if data.SkeletonPositions[JointId.ShoulderCenter].x!=0.0 and data.SkeletonPositions[JointId.ShoulderCenter].y!=0.0 and data.SkeletonPositions[JointId.ShoulderCenter].z!=0.0:
            global ShoulderCenterX,ShoulderCenterY,ShoulderCenterZ
            ShoulderCenterX=data.SkeletonPositions[JointId.ShoulderCenter].x-ShoulderCenterX
            ShoulderCenterY=data.SkeletonPositions[JointId.ShoulderCenter].y-ShoulderCenterY
            ShoulderCenterZ=data.SkeletonPositions[JointId.ShoulderCenter].z-ShoulderCenterZ

        if data.SkeletonPositions[JointId.ShoulderLeft].x!=0.0 and data.SkeletonPositions[JointId.ShoulderLeft].y!=0.0 and data.SkeletonPositions[JointId.ShoulderLeft].z!=0.0:
            global ShoulderLeftX,ShoulderLeftY,ShoulderLeftZ
            ShoulderLeftX=data.SkeletonPositions[JointId.ShoulderLeft].x-ShoulderLeftY
            ShoulderLeftY=data.SkeletonPositions[JointId.ShoulderLeft].y-ShoulderLeftY
            ShoulderLeftZ=data.SkeletonPositions[JointId.ShoulderLeft].z-ShoulderLeftZ

        if data.SkeletonPositions[JointId.ShoulderRight].x!=0.0 and data.SkeletonPositions[JointId.ShoulderRight].y!=0.0 and data.SkeletonPositions[JointId.ShoulderRight].z!=0.0:
            global ShoulderRightX,ShoulderRightY,ShoulderRightZ
            ShoulderRightX=data.SkeletonPositions[JointId.ShoulderRight].x-ShoulderRightX
            ShoulderRightY=data.SkeletonPositions[JointId.ShoulderRight].y-ShoulderRightY
            ShoulderRightZ=data.SkeletonPositions[JointId.ShoulderRight].z-ShoulderRightZ

        if data.SkeletonPositions[JointId.WristLeft].x!=0.0 and data.SkeletonPositions[JointId.WristLeft].y!=0.0 and data.SkeletonPositions[JointId.WristLeft].z!=0.0:
            global WristLeftX,WristLeftY,WristLeftZ
            WristLeftX=data.SkeletonPositions[JointId.WristLeft].x-WristLeftX
            WristLeftY=data.SkeletonPositions[JointId.WristLeft].y-WristLeftY
            WristLeftZ=data.SkeletonPositions[JointId.WristLeft].z-WristLeftZ

        if data.SkeletonPositions[JointId.WristRight].x!=0.0 and data.SkeletonPositions[JointId.WristRight].y!=0.0 and data.SkeletonPositions[JointId.WristRight].z!=0.0:
            global WristRightX,WristRightY,WristRightZ
            WristRightX=data.SkeletonPositions[JointId.WristRight].x-WristRightX
            WristRightY=data.SkeletonPositions[JointId.WristRight].y-WristRightY
            WristRightZ=data.SkeletonPositions[JointId.WristRight].z-WristRightZ

        if data.SkeletonPositions[JointId.ElbowRight].x!=0.0 and data.SkeletonPositions[JointId.ElbowRight].y!=0.0 and data.SkeletonPositions[JointId.ElbowRight].z!=0.0:
            global ElbowRightX,ElbowRightY,ElbowRightZ
            ElbowRightX=data.SkeletonPositions[JointId.ElbowRight].x-ElbowRightX
            ElbowRightY=data.SkeletonPositions[JointId.ElbowRight].y-ElbowRightY
            ElbowRightZ=data.SkeletonPositions[JointId.ElbowRight].z-ElbowRightZ

        if data.SkeletonPositions[JointId.ElbowLeft].x!=0.0 and data.SkeletonPositions[JointId.ElbowLeft].y!=0.0 and data.SkeletonPositions[JointId.ElbowLeft].z!=0.0:
            global ElbowLeftX,ElbowLeftY,ElbowLeftZ
            ElbowLeftX=data.SkeletonPositions[JointId.ElbowLeft].x-ElbowLeftX
            ElbowLeftY=data.SkeletonPositions[JointId.ElbowLeft].y-ElbowLeftY
            ElbowLeftZ=data.SkeletonPositions[JointId.ElbowLeft].z-ElbowLeftZ

        if data.SkeletonPositions[JointId.KneeLeft].x!=0.0 and data.SkeletonPositions[JointId.KneeLeft].y!=0.0 and data.SkeletonPositions[JointId.KneeLeft].z!=0.0:
            global KneeLeftX,KneeLeftY,KneeLeftZ
            KneeLeftX=data.SkeletonPositions[JointId.KneeLeft].x-KneeLeftX
            KneeLeftY=data.SkeletonPositions[JointId.KneeLeft].y-KneeLeftY
            KneeLeftZ=data.SkeletonPositions[JointId.KneeLeft].z-KneeLeftZ

        if data.SkeletonPositions[JointId.KneeRight].x!=0.0 and data.SkeletonPositions[JointId.KneeRight].y!=0.0 and data.SkeletonPositions[JointId.KneeRight].z!=0.0:
            global KneeRightX,KneeRightY,KneeRightZ
            KneeRightX=data.SkeletonPositions[JointId.KneeRight].x-KneeRightX
            KneeRightY=data.SkeletonPositions[JointId.KneeRight].y-KneeRightY
            KneeRightZ=data.SkeletonPositions[JointId.KneeRight].z-KneeRightZ

        if data.SkeletonPositions[JointId.FootLeft].x!=0.0 and data.SkeletonPositions[JointId.FootLeft].y!=0.0 and data.SkeletonPositions[JointId.FootLeft].z!=0.0:
            global FootLeftX,FootLeftY,FootLeftZ
            FootLeftX=data.SkeletonPositions[JointId.FootLeft].x-FootLeftX
            FootLeftY=data.SkeletonPositions[JointId.FootLeft].y-FootLeftY
            FootLeftZ=data.SkeletonPositions[JointId.FootLeft].z-FootLeftZ

        if data.SkeletonPositions[JointId.FootRight].x!=0.0 and data.SkeletonPositions[JointId.FootRight].y!=0.0 and data.SkeletonPositions[JointId.FootRight].z!=0.0:
            global FootRightX,FootRightY,FootRightZ
            FootRightX=data.SkeletonPositions[JointId.FootRight].x-FootRightX
            FootRightY=data.SkeletonPositions[JointId.FootRight].y-FootRightY
            FootRightZ=data.SkeletonPositions[JointId.FootRight].z-FootRightZ

        #-----------------------------------------------------------------------------------------------------
        if data.SkeletonPositions[JointId.Head].y!=0.0 and data.SkeletonPositions[JointId.ShoulderCenter].y!=0.0 and data.SkeletonPositions[JointId.ShoulderLeft].y!=0.0 \
            and data.SkeletonPositions[JointId.ShoulderRight].y!=0.0 and data.SkeletonPositions[JointId.HipCenter].y!=0.0:
            global headY, RightShoulderY, LeftShoulderY, CenterShoulderY,CenterHipY
            headY=data.SkeletonPositions[JointId.Head].y
            CenterShoulderY=data.SkeletonPositions[JointId.ShoulderCenter].y
            LeftShoulderY=data.SkeletonPositions[JointId.ShoulderLeft].y
            RightShoulderY=data.SkeletonPositions[JointId.ShoulderRight].y
            CenterHipY=data.SkeletonPositions[JointId.HipCenter].y

        if data.SkeletonPositions[JointId.Head].z!=0.0 and data.SkeletonPositions[JointId.ShoulderCenter].z!=0.0 and data.SkeletonPositions[JointId.ShoulderLeft].z!=0 \
            and data.SkeletonPositions[JointId.ShoulderRight].z!=0.0 and data.SkeletonPositions[JointId.HipCenter].z!=0.0:
            global headZ,RightShoulderZ,LeftShoulderZ,RightShoulderZ,CenterShoulderZ,CenterHipZ
            headZ=data.SkeletonPositions[JointId.Head].z
            RightShoulderZ=data.SkeletonPositions[JointId.ShoulderRight].z
            LeftShoulderZ=data.SkeletonPositions[JointId.ShoulderLeft].z
            CenterShoulderZ=data.SkeletonPositions[JointId.ShoulderCenter].z
            CenterHipZ=data.SkeletonPositions[JointId.HipCenter].z


def depth_frame_ready(frame):
    if video_display:
        return

    with screen_lock:

        address = surface_to_array(screen)

        frame.image.copy_bits(address)

        del address

        if skeletons is not None and draw_skeleton:
            draw_skeletons(skeletons)

        pygame.display.update()


def video_frame_ready(frame):
    if not video_display:
        return

    with screen_lock:

        address = surface_to_array(screen)

        frame.image.copy_bits(address)

        del address

        if skeletons is not None and draw_skeleton:
            draw_skeletons(skeletons)

        pygame.display.update()

if __name__=='__main__':


    full_screen = False

    draw_skeleton = True

    video_display = False

    screen_lock = thread.allocate()

    screen = pygame.display.set_mode(DEPTH_WINSIZE, 0, 16)

    pygame.display.set_caption('Python Kinect Demo')

    skeletons = None

    screen.fill(THECOLORS["black"])

    kinect = nui.Runtime()

    kinect.skeleton_engine.enabled = True


    def post_frame(frame):

        try:

            pygame.event.post(pygame.event.Event(KINECTEVENT, skeletons=frame.SkeletonData))

        except:

            # event queue full

            pass


    kinect.skeleton_frame_ready += post_frame

    kinect.depth_frame_ready += depth_frame_ready

    kinect.video_frame_ready += video_frame_ready

    kinect.video_stream.open(nui.ImageStreamType.Video, 2, nui.ImageResolution.Resolution640x480, nui.ImageType.Color)

    kinect.depth_stream.open(nui.ImageStreamType.Depth, 2, nui.ImageResolution.Resolution320x240, nui.ImageType.Depth)

    print

    print('Controls: ')

    print('     d - Switch to depth view')

    print('     v - Switch to video view')

    print('     s - Toggle displaing of the skeleton')

    print('     u - Increase elevation angle')

    print('     j - Decrease elevation angle')

    # main game loop

    done = False
    raised=False
    start_time = time.time()
    k=0
    while not done:
        e = pygame.event.wait()

        dispInfo = pygame.display.Info()
        frame= kinect.skeleton_engine.get_next_frame()
        #sec2 = time.time() - start_time
        #print ("%.2f" % sec2)
        if e.type == pygame.QUIT:

            done = True
            break

        elif e.type == KINECTEVENT:

            skeletons = e.skeletons
            if (k == 0):
                winsound.Beep(2500, 1000)
                k += 1
            if draw_skeleton:
                draw_skeletons(skeletons)

                pygame.display.update()
                totalY = (headY + CenterShoulderY + LeftShoulderY + RightShoulderY + CenterHipY) / 5
                totalZ = (headZ + CenterShoulderZ + LeftShoulderZ + RightShoulderZ + CenterHipZ) / 5


                functions.recognize_sitting(totalY, totalZ)

                functions.write_speed_Joints_To_Txt(HipCenterX, HipCenterY, HipCenterZ, HandRightX, HandRightY, HandRightZ,
                                              HandLeftX, HandLeftY, HandLeftZ, ElbowLeftX, ElbowLeftY, ElbowLeftZ
                                              , ElbowRightX, ElbowRightY, ElbowRightZ, WristLeftX, WristLeftY,
                                              WristLeftZ, WristRightX, WristRightY, WristRightZ, ShoulderLeftX,
                                              ShoulderLeftY,
                                              ShoulderLeftZ, ShoulderRightX, ShoulderRightY, ShoulderRightZ,
                                              ShoulderCenterX, ShoulderCenterY, ShoulderCenterZ, HeadX, HeadY, HeadZ,
                                              SpineX, SpineY, SpineZ,
                                              HipLeftX, HipLeftY, HipLeftZ, HipRightX, HipRightY, HipRightZ, KneeLeftX,
                                              KneeLeftY, KneeLeftZ, KneeRightX, KneeRightY, KneeRightZ,
                                              AnkleLeftX, AnkleLeftY, AnkleLeftZ, AnkleRightX, AnkleRightY, AnkleRightZ,
                                              FootRightX, FootRightY, FootRightZ, FootLeftX, FootLeftY, FootLeftZ)

        elif e.type == KEYDOWN:

            if e.key == K_ESCAPE:

                done = True
                fo=open("logs.txt",'a')
                fo.write("--------------------------------------- End\n ")
                fo.close()
                break

            elif e.key == K_d:

                with screen_lock:

                    screen = pygame.display.set_mode(DEPTH_WINSIZE, 0, 16)

                    video_display = False

            elif e.key == K_v:

                with screen_lock:

                    screen = pygame.display.set_mode(VIDEO_WINSIZE, 0, 32)

                    video_display = True

            elif e.key == K_s:

                draw_skeleton = not draw_skeleton

            elif e.key == K_u:

                kinect.camera.elevation_angle = kinect.camera.elevation_angle + 2

            elif e.key == K_j:

                kinect.camera.elevation_angle = kinect.camera.elevation_angle - 2

            elif e.key == K_x:

                kinect.camera.elevation_angle = 2
