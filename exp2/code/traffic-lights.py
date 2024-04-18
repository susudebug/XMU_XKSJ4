from gpiozero import PWMLED, Button
from signal import pause
from threading import Thread
from time import sleep

# 创建PWMLED对象，代表红、绿、蓝LED
red_led = PWMLED(2)
green_led = PWMLED(3)
blue_led = PWMLED(4)

# 是否处于呼吸状态的标志
breathing = False

# 按钮按下时的处理函数
def button_pressed():
    global breathing, breathe_thread
    print(breathing)
    # 创建并启动一个新线程来监视breathing变量的状态
    if breathing==False:
        # 如果不处于呼吸状态，则开始呼吸灯效果
        breathing = True
        # 创建并启动一个新线程来执行呼吸灯效果
        breathe_thread = Thread(target=breathe)
        breathe_thread.start()
        
    else:
        # 否则停止呼吸灯效果
        breathing = False
        red_led.off()
        green_led.off()
        blue_led.off()
# 呼吸灯效果函数
def breathe():
    while breathing:

        red_led.on()
        red_led.pulse()
        for i in range(30):
            sleep(0.1)
            if not breathing:
                return
        red_led.off()

        green_led.on()
        green_led.pulse()
        for i in range(30):
            sleep(0.1)
            if not breathing:
                return
        green_led.off()


        blue_led.on()
        blue_led.pulse()
        for i in range(30):
            sleep(0.1)
            if not breathing:
                return
        blue_led.off()



# 创建按钮对象，代表控制按钮
button = Button(12,bounce_time=0.2)
while(True):
    # 当按键被按下时调用button_pressed函数
    button.when_pressed= button_pressed
    # 进入暂停模式，等待中断信号
    pause()


