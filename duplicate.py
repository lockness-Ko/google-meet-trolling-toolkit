import pyautogui
from time import sleep
import pyperclip

#15 tabs before x button

link = input('Meet URL?\n>')

unmute_button = None
mute_button = None
endcall_button = None

def getButtons():
    try:
        unmute_button = pyautogui.locateCenterOnScreen('UNMUTE.png')
        mute_button = pyautogui.locateCenterOnScreen('MUTE.png')
        endcall_button = pyautogui.locateCenterOnScreen('ENDCALL.png')
    except:
        print('deez nuts!')

def unMute():
    x, y = 0,0
    while True:
        try:
            try:
                mute_loc, __ = pyautogui.locateCenterOnScreen('MUTE.png')
                return
            except:
                print()
            x, y = pyautogui.locateCenterOnScreen('UNMUTE.png')
            break
        except:
            print("nound yet")
    pyautogui.click(x,y)

def muteVideo():
    x, y = 0,0
    while True:
        try:
            try:
                mute_loc, __ = pyautogui.locateCenterOnScreen('VIDEOON.png')
                return
            except:
                print()
            x, y = pyautogui.locateCenterOnScreen('VIDEOOFF.png')
            break
        except:
            print("nound yet")
    pyautogui.click(x,y)

def mute():
    try:
        mute_loc = pyautogui.click('MUTE.png')
    except:
        print('not found')

def join():
    x, y = 0,0
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen('JOIN.png')
            break
        except:
            print("Not found yet")
    pyautogui.click(x,y)

def newTab():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('t')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('t')

def paste(text):
    pyperclip.copy(text)
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('v')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('v')
    pyautogui.press('enter')
    

def newMeet():
    newTab()
    paste(link)
    # sleep(3.5)
    join()
    # sleep(2)
    unMute()
    muteVideo()

sleep(1)
for i in range(15):
    newMeet()