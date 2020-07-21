from pynput.keyboard import KeyCode, Listener, Controller 
from pynput.mouse import Controller as mController, Button
import time
import threading

class Macro(threading.Thread):
    def __init__(self, delay, button):
        super(Macro, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.programRunning = True

    def startMacro(self):
        self.running = True
    
    def stopMacro(self):
        self.running = False
    
    def exit(self):
        self.stopMacro()
        self.programRunning = False

    def run(self):
        while self.programRunning == True:
            while self.running == True:
                Keyboard.press('w')
                mouse.press(button)
            time.sleep(1)

def on_press(key):
    if key == startStopKey:
        if macroThread.running:
            macroThread.stopMacro()
        else:
            macroThread.startMacro()
    elif key == exitKey:
        macroThread.exit()
        listener.stop()

if __name__ == "__main__":
    delay = .01
    button = Button.right
    startStopKey = KeyCode(char='b')
    exitKey = KeyCode(char='n')
    Keyboard = Controller()
    mouse = mController()
    macroThread = Macro(delay, button)
    macroThread.start()

    with Listener(on_press=on_press) as listener:
        listener.join()




