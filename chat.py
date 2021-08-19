import pyautogui
from time import sleep

print("THe j")

def selectChat():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('alt')
    pyautogui.keyDown('c')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('c')
    try:
        mbox_loc = pyautogui.click('MESSAGEBOX.png')
    except:
        print('not found')

def sendMessage(msg):
    pyautogui.write(msg)
    pyautogui.press('enter')

mg = input("Message?\n>")
sleep(1)
selectChat()
while True:
    sendMessage(mg)