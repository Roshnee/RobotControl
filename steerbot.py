import RPi.GPIO as gpio 
import time 
import sys, tty, termios

#setting the pin mode which would be used
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)

#assign pin numbers to variables
E1=18
M1=17
E2=19
M2=20

#setting pins to output mode during runtime
gpio.setup(E1,gpio.OUT)
gpio.setup(M1,gpio.OUT)
gpio.setup(E2,gpio.OUT)
gpio.setup(M2,gpio.OUT)

#setting pwm
pwm_left=gpio.PWM(E2,50)
pwm_right=gpio.PWM(E1,50)

#setting dutycycle to 30%
pwm_left.start(0)
pwm_right.start(0)

#for input settings
#def getch():
#    fd = sys.stdin.fileno()
#    old_settings = termios.tcgetattr(fd)
#    try:
#        tty.setraw(sys.stdin.fileno())
#        ch = sys.stdin.read(1)
#    finally:
#        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#    return ch

#define robot motions
def forward():
  gpio.output(E1,gpio.HIGH)
  gpio.output(M1,gpio.HIGH)
  gpio.output(E2,gpio.HIGH)
  gpio.output(M2,gpio.LOW)
  time.sleep(2)

def backward():
  gpio.output(E1,gpio.HIGH)
  gpio.output(M1,gpio.LOW)
  gpio.output(E2,gpio.HIGH)
  gpio.output(M2,gpio.HIGH)
  time.sleep(2)

def left():
  gpio.output(E1,gpio.HIGH)
  gpio.output(M1,gpio.HIGH)
  gpio.output(E2,gpio.HIGH)
  gpio.output(M2,gpio.HIGH)
  time.sleep(2)

def right():
  gpio.output(E1,gpio.HIGH)
  gpio.output(M1,gpio.LOW)
  gpio.output(E2,gpio.HIGH)
  gpio.output(M2,gpio.LOW)
  time.sleep(2)

def duty_cycle():
  pwm_left.ChangeDutyCycle(30)
  pwm_right.ChangeDutyCycle(30)

print("Steer your bot")
while(True):
  char=raw_input()
  if(char == 'f'):
    print("Moving forward")
    duty_cycle()
    forward()

  if(char == 'b'):
    print("Moving backward")
    duty_cycle()
    backward()

  if(char == 'l'):
    print("going to turn left")
    duty_cycle()
    left()

  if(char == 'r'):
    print("going to turn right")
    duty_cycle()
    right()

  if(char == 's'):
    print("Stop")
    break;

pwm.ChangeDutyCycle(0)
char=""
gpio.cleanup()

 
