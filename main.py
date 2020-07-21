from pynput.keyboard import Key, KeyCode, Listener, Controller as keyController
from pynput.mouse import Button, Controller as mouseController
import macroClass

myKeyboard = keyController()
myMouse =  mouseController()
start_stop_key = KeyCode(char = 'n')
exit_key = KeyCode( char = 'b')

 
macro = macroClass.Macro()
macro.start()

def on_press(key):
    if key == start_stop_key:
        print("macroObject is either running or stopping")
        if macro.running == True:
            macro.stopMacro()
        else:
            macro.startMacro()
        macro.runProgram()
    elif key == exit_key:
        print("ExitKey")
        macro.exit()
        listener.stop()
    else:
        print(f"TF why is {key} here?!? LMAOOO stoopid")

with Listener(on_press = on_press) as listener:
    listener.join()
