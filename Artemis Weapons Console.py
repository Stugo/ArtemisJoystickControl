# Artemis Weapons Console by Stugo
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
import win32api, win32con
from win32api import GetSystemMetrics
from pygame.locals import *

print("Artemis Weapons Console by Stugo")
print("You'll need to run Artemis in Full Screen Windowed")

pygame.init()

# Set the width and height of the screen [width,height]
size = [300, 200]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Artemis Weapons Console by Stugo")

# Get the pixel width and height
width = GetSystemMetrics (0)
height = GetSystemMetrics (1)

#Sets the coordinates for Load/unload
if width == 1366 and height == 768:
    ODDX=50             # X coordinate for the center of the odd tubes
    EVENX=25            # X coordinate for the center of the even tubes
    TUBE1Y=750          # Y coordinate for the center of tube 1
    TUBE2Y=700          # Y coordinate for the center of tube 2
    TUBE3Y=650          # Y coordinate for the center of tube 3
    TUBE4Y=600          # Y coordinate for the center of tube 4
    print("1366x768 is selected")
elif width == 1280 and height == 800:
    ODDX=55
    EVENX=30
    TUBE1Y=775
    TUBE2Y=725
    TUBE3Y=675
    TUBE4Y=630
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


def click(x,y):         #Make the cursor move and click
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def press(VK_CODE):     #Press a key on the keyboard
    win32api.keybd_event(VK_CODE, 0,0,0)
    pygame.time.wait(5)
    win32api.keybd_event(VK_CODE,0 ,win32con.KEYEVENTF_KEYUP ,0)

def press_s(VK_CODE):   #Press shift + a key on the keyboard
    win32api.keybd_event(0xA0, 0,0,0)
    pygame.time.wait(5)
    press(VK_CODE)
    pygame.time.wait(10)
    win32api.keybd_event(0xA0,0 ,win32con.KEYEVENTF_KEYUP ,0)

#Loop until the user clicks the close button.
done = False

# -------- Main Program Loop -----------
while not done:
    pygame.time.wait(1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                press(0x71)
                print("Viewscreen Commands: Front")
            elif event.button == 1:
                press(0x72)
                print("Viewscreen Commands: Left")
            elif event.button == 2:
                press(0x73)
                print("Viewscreen Commands: Right")
            elif event.button == 3:
                press(0x74)
                print("Viewscreen Commands: Rear")
            elif event.button == 4:
                press(0x75)
                print("Viewscreen Commands: Tactical")
            elif event.button == 5:
                press(0x76)
                print("Viewscreen Commands: Long Range")
            elif event.button == 6:
                press(0x77)
                print("Viewscreen Commands: Long Range")
            elif event.button == 7:
                press (0x34)
                print("Select Weapons: EMP")
            elif event.button == 8:
                press (0x33)
                print("Select Weapons: Mine")
            elif event.button == 9:
                press (0x32)
                print("Select Weapons: Nuke")
            elif event.button == 10:
                press(0x31)
                print("Select Weapons: Homing")
            elif event.button == 11:
                press (0x42)
                print("Toggle Auto Beam")
            elif event.button == 12:
                press_s (0x55)
                print("Torp-Energy")
            elif event.button == 13:
                press (0x27)
                print("Weap Freq. Right")
            elif event.button == 14:
                press (0x25)
                print("Weap Freq. Left")
            elif event.button == 15:
                press (0x51)
                print("Toggle Shield")
            elif event.button == 16:
                press_s (0x49)
                print("Energy-Torp")
            elif event.button == 17:
                press (0x59)
                print("Zoom Out")
            elif event.button == 18:
                press (0x54)
                print("Zoom In")
            elif event.button == 19:
                press_s (0x34)
                print("Fire Tubes: 4")
            elif event.button == 20:
                press_s (0x33)
                print("Fire Tubes: 3")
            elif event.button == 21:
                press_s (0x32)
                print("Fire Tubes: 2")
            elif event.button == 22:
                press_s (0x31)
                print("Fire Tubes: 1")
            elif event.button == 23:
                click (EVENX,TUBE4Y)
                print("Load / Unload Tubes: 4")
            elif event.button == 24:
                click (ODDX,TUBE3Y)
                print("Load / Unload Tubes: 3")
            elif event.button == 25:
                click (EVENX,TUBE2Y)
                print("Load / Unload Tubes: 2")
            elif event.button == 26:
                click (ODDX,TUBE1Y)
                print("Load / Unload Tubes: 1")
           

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()
