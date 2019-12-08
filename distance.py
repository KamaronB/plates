
import RPi.GPIO as GPIO
import time

 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setwarnings(False) 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 
def distancefunc():
    i=0
    tmp=0
    result=False
    try:
        while True:
            dist = distance()
            if (tmp<dist+2 and tmp>dist-2 and dist<50 and dist>5):
                i=i+1
            else:
                i=0
            print("counter"+str(i));
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
            tmp=dist;
            if(i>10):
                print("car is stable")
                result=True
                break
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
    return result
        
                
            
        
            
     
        # Reset by pressing CTRL + C
    