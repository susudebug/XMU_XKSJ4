from gpiozero import OutputDevice
from time import sleep
from signal import pause

A1 = OutputDevice(27)
A2 = OutputDevice(17)
stepPins = [A1,A2]
stepPins[0].on() # 0或1都可
sleep(2)
stepPins[0].off()
pause()