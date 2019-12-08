
import numpy as np
from openalpr import Alpr
import requests as req
import json
import cv2
import time
import os
import distance

plate_nums=[]
lastNum = "phony"
lot= "1b"
pi_name= "Pi-1"
alpr = Alpr("us", "/usr/share/openalpr/config/openalpr.defaults.conf", "/usr/share/openalpr/runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    #sys.exit(1)

##variable for the plate and frame
p= ""
c = ""

url="https://aj677mha43.execute-api.us-east-1.amazonaws.com/Beta/check_plate"

alpr.set_top_n(20)
alpr.set_default_region("md")

#cv2.destroyAllWindows()
def recognize(filename="test2.jpg"):



    
    results = alpr.recognize_file(filename)
    print(results)

    try:
        p= results['results'][0][u'plate']
        c= results['results'][0][u'confidence']
        print(p + " : " + str(c))
        if len(plate_nums)<5:
            plate_nums.append(p)
        elif len(plate_nums)==5:
            if plate_nums[0] == plate_nums[4] and lastNum != p:
                req.post(url,data=json.dumps({'plate': p,'conf': c, 'name': pi_name, 'lot':lot}))
                plate_nums=[]
                lastNum=p
            
                
            

        
        alpr.unload()
        
     
        
    except:
       req.post(url, data=json.dumps({'plate':'404','conf':'404'}))
       plate_nums.append('404')
       print('error')
def camera():
    cap = cv2.VideoCapture(-1) # video capture source camera (Here webcam of laptop) 
    ret,frame = cap.read() # return a single frame in variable `frame`


    
    #cv2.imshow('img1',frame) #display the captured image
    try:
        print("writing file")
        print(cv2.imwrite('test2.jpg',frame))
    except:
        print("file not written")
    cv2.destroyAllWindows()
        

    cap.release()
    
    time.sleep(5)
    recognize()          



               
                
            
    # Call when completely done to release memory
    
#get distnce
while(1):
    dist=distance.distancefunc();
    print(dist); 
    if(dist):
        camera()
        
        
        
    
   
    #print("counting started");
    #time.sleep(30);



 


#camera()
#recognize(filename)


