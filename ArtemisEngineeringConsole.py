# Artemis Engineering Console by Stugo
# NOTE: This script requires the following Python modules:   
#  pygame   - http://www.pygame.org/  
# Win32 users may also need:  
#  pywin32  - http://sourceforge.net/projects/pywin32/ 
#
# This script is based on a screen resolution of 1366x768 or 1280x800
#
# This script is Beerware
# ----------------------------------------------------------------------------
# "THE BEER-WARE LICENSE":
# As long as you retain this notice you can do whatever you want with this
# stuff. If we meet some day, and you think this stuff is worth it, you can
# buy me a beer in return /Stugo
# ----------------------------------------------------------------------------

import pygame
import time
import serial
import sys
import win32api, win32con
from PIL import ImageGrab
from win32api import GetSystemMetrics
from pygame.locals import *

# Buttons
# 0-7 is Coolant Up
# 8-15 is Coolant Down
# 16-25 is Presets 1-0
# 26 is Shift
# 27 is Spacebar
# 28 is Enter

# Some numbers dependent on resolution 1366x768
# Slider location:
# Y: 525 - 725
# X: 50 + 168*n
# Coolant: 
# Y: 535, 745
# X: 94 + 168*n
# Heat:
# Y: 464, 503
# X: 84 + 168*n

# Some numbers dependent on resolution 1280x800
# Slider location:
# Y: 543 - 755
# X: 50 + 157*n
# Coolant: 
# Y: 555, 780
# X: 94 + 157*n
# Heat:
# Y: 485, 523
# X: 84 + 157*n

print("Artemis Engineering Console by Stugo")
print("You'll need to run Artemis in Full Screen Windowed")

pygame.init()

# Set the width and height of the screen [width,height]
#size = [300, 200]
#screen = pygame.display.set_mode(size)
#pygame.display.set_caption("Artemis Engineering Console by Stugo")

# Get the pixel width and height
width = GetSystemMetrics (0)
height = GetSystemMetrics (1)

#Sets the coordinates
if width == 1366 and height == 768:
    COOLX = 94          # X coordinate to the center of the first blue coolant arrow
    COOLXSPACE = 168    # Spacing in X between coolant systems
    COOLYUP = 535       # Y coordinate to the center of a blue coolant up-arrow
    COOLYDOWN = 745     # Y coordinate to the center of a blue coolant down-arrow
    SLIDETOP = 525.0    # Y coordinate to the top of a energy-slider
    SLIDEBOT = 725.0    # Y coordinate to the bottom of a energy-slider
    SLIDEX = 50         # X coordinate to the center of the first energy-slider
    SLIDESPACE = 168    # Spacing in X between energy-sliders
    HEATTOP = 464.0     # Y coordinate to the top of a heatbar
    HEATBOT = 503.0     # Y coordinate to the bottom of a heatbar
    HEATX = 84          # X coordinate to the center of the first beatbar
    HEATSPACCE = 168    # Spacing in X between heatbars
    print("1366x768 is selected")
elif width == 1280 and height == 800:
    COOLX = 94
    COOLXSPACE = 157
    COOLYUP = 555
    COOLYDOWN = 780
    SLIDETOP = 543.0
    SLIDEBOT = 755.0
    SLIDEX = 50
    SLIDESPACE = 157
    HEATTOP = 485.0
    HEATBOT = 523.0
    HEATX = 84
    HEATSPACCE = 157
    print("1280x800 is selected")
else:
    print("Sorry, your screen resolution",width,"x",height, "is not supported.")


# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Initialize the joysticks
pygame.joystick.init()

# Count the joysticks:
joystickCount = pygame.joystick.get_count()

if joystickCount == 0:
    print("Sorry, no joysticks were found!")

else:
    myJoy = pygame.joystick.Joystick(0)
    myJoy.init()
    print("Joystick name: ", myJoy.get_name())
    print("Joystick id: ", myJoy.get_id())
    print("Number of buttons: ", myJoy.get_numbuttons())


def click(x,y):         # Make the cursor move and click
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def press(VK_CODE):     # Press a key on the keyboard
    win32api.keybd_event(VK_CODE, 0,0,0)
    pygame.time.wait(5)
    win32api.keybd_event(VK_CODE,0 ,win32con.KEYEVENTF_KEYUP ,0)

def coolantup(nbr):     # Make the coolant go up
    x = COOLX + COOLXSPACE * nbr
    y = COOLYUP
    click(x,y)

def coolantdown(nbr):   # Make the coolant go down
    x = COOLX + COOLXSPACE * (nbr - 8)
    y = COOLYDOWN
    click(x,y)

def setslider(nbr, value):      # Move the slider
    x = SLIDEX + SLIDESPACE * nbr
    y = (SLIDEBOT - SLIDETOP) * ((value + 1) / 2) + SLIDETOP
    click(x,y)

def getHeat():      # This bit is written by Davr. It gets the overheat-level
        px=ImageGrab.grab().load() # capture an image of the screen
        color = 0
        for i in range(0,8): # loop over all 8 heat indicators
            x = HEATX + HEATSPACE*i # math to calculate the X position of the center of the heat indicator
            total = 0
            for y in range(HEATBOT, HEATTOP, -1): # loop over all the Y positions in the heat indicator
                if sum(px[x,y]) > 200: # if the sum of red, blue, and green channels is over 200
                    total+=1
            self.heat[i] = 100 * total/(HEATBOT - HEATTOP) # calculate total heat for this heat indicator
        print("Heat: " + str(self.heat))

#Loop until the user clicks the close button.
done = False

# -------- Main Program Loop -----------
while not done:
    pygame.time.wait(1)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button >= 0 and event.button <=7:
                coolantup(event.button)
                
            elif event.button >= 8 and event.button <= 15:
                coolantdown(event.button)
                
            elif event.button == 16:
                press (0x31)
                print("1")
            elif event.button == 17:
                press (0x32)
                print("2")
            elif event.button == 18:
                press (0x33)
                print("3")
            elif event.button == 19:
                press (0x34)
                print("4")
            elif event.button == 20:
                press (0x35)
                print("5")
            elif event.button == 21:
                press (0x36)
                print("6")
            elif event.button == 22:
                press (0x37)
                print("7")
            elif event.button == 23:
                press (0x38)
                print("8")
            elif event.button == 24:
                press (0x39)
                print("9")
            elif event.button == 25:
                press (0x30)
                print("0")
            elif event.button == 26:
                press (0xA0)
                print("Shift")
            elif event.button == 27:
                press (0x20)
                print("Spacebar")
            elif event.button == 28:
                press (0x0D)
                print("Enter")

        elif event.type == pygame.JOYAXISMOTION:
            if event.value > -1.0:
                setslider(event.axis, event.value)
           

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
