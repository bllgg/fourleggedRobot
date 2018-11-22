import RPi.GPIO as GPIO
import time

#setting Input output pins for the servo motors.
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

#naming the servo motors
L1 = GPIO.PWM(2, 50)
S1 = GPIO.PWM(3, 50)
L2 = GPIO.PWM(17, 50)
S2 = GPIO.PWM(27, 50)
L3 = GPIO.PWM(5, 50)
S3 = GPIO.PWM(6, 50)
L4 = GPIO.PWM(10, 50)
S4 = GPIO.PWM(9, 50)

S4.start(0)
S1.start(0)
S2.start(0)
S3.start(0)
L1.start(0)
L2.start(0)
L3.start(0)
L4.start(0)

try:
    while 1:
        
        for i in range(0,31):
            L2.ChangeDutyCycle(9-i/10.0)
            time.sleep(0.008)
            L4.ChangeDutyCycle(9-i/10.0)
            time.sleep(0.008)
            
        time.sleep(0.025)
        
        L1.ChangeDutyCycle(4.5)
        time.sleep(0.003)
        L3.ChangeDutyCycle(4.5)
        time.sleep(0.003) 
        
        for i in range(0,41):
            S1.ChangeDutyCycle(9-(i/10.0))
            time.sleep(0.003)
            S2.ChangeDutyCycle(9-(i/10.0))
            time.sleep(0.003)
            S3.ChangeDutyCycle(4+(i/10.0))
            time.sleep(0.003)
            S4.ChangeDutyCycle(6.5+(i/10.0))
            time.sleep(0.003)
            
        L1.ChangeDutyCycle(0)
        time.sleep(0.003)
        L3.ChangeDutyCycle(0)
        time.sleep(0.003)
        
        for i in range(0,31):
            L1.ChangeDutyCycle(4.5+i/10.0)
            time.sleep(0.008)
            L3.ChangeDutyCycle(4.5+i/10.0)
            time.sleep(0.008)
            
        time.sleep(0.025)
            
        L2.ChangeDutyCycle(9)
        time.sleep(0.008)
        L4.ChangeDutyCycle(9)
        time.sleep(0.008)
        
        for i in range(0,41):
            S1.ChangeDutyCycle(5+(i/10.0))
            time.sleep(0.003)
            S2.ChangeDutyCycle(5+(i/10.0))
            time.sleep(0.003)
            S3.ChangeDutyCycle(8-(i/10.0))
            time.sleep(0.003)
            S4.ChangeDutyCycle(10.5-(i/10.0))
            time.sleep(0.003)
            
        
        
        
    S1.ChangeDutyCycle(0)
    time.sleep(0.015)
    S2.ChangeDutyCycle(0)
    time.sleep(0.015)
    S3.ChangeDutyCycle(0)
    time.sleep(0.015)
    S4.ChangeDutyCycle(0)
    time.sleep(0.015)
    L1.ChangeDutyCycle(0)
    time.sleep(0.015)
    L2.ChangeDutyCycle(0)
    time.sleep(0.015)
    L3.ChangeDutyCycle(0)
    time.sleep(0.015)
    L4.ChangeDutyCycle(0)
    time.sleep(0.015)
    
#Operation can be stopped by keyboard interrupt
except KeyboardInterrupt:
    S1.stop()
    S2.stop()
    S3.stop()
    S4.stop()
    L1.stop()
    L2.stop()
    L3.stop()
    L4.stop()
    GPIO.cleanup()
