from gpiozero import OutputDevice
from time import sleep
from signal import pause

A1 = OutputDevice(27)
A2 = OutputDevice(17)
B1 = OutputDevice(3)
B2 = OutputDevice(2)

# Define the sequence for clockwise rotation
seq = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
stepPins = [B2,A2,B1,A1]

stepCount = len(seq)
sleep(1)
flag = 0 

while True:
    for i in range(0, stepCount): # Loop in reverse for anti-clockwise
        for j in range(0, stepCount):
            if seq[i][j] == 1:
                stepPins[j].on()
                sleep(0.2)
                stepPins[j].off()
                flag = flag + 1
                print('The angle is', (flag % 20) * 18)
                if (flag % 5) == 0:
                    print('Because the angle is', (flag % 20) * 18, ' so stop.')
                    sleep(2)
                if (flag % 20) == 2:
                    print('Because the angle is about 45, so stop.')
                    sleep(2)

pause()
