from openalpr import Alpr
import cv2
import os
alpr = Alpr("us", "/usr/share/openalpr/config/openalpr.defaults.conf", "/usr/share/openalpr/runtime_data")
if not alpr.is_loaded():
    print("Error loading OpenALPR")
    #sys.exit(1)

##variable for the plate and frame
p= ""
c = ""
filename= "test1.jpg"

alpr.set_top_n(20)
alpr.set_default_region("md")

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

  
        
    if k%256 == 32:
        # SPACE pressed

        img_name = filename.format(img_counter)

        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1
        print("Escape hit, closing...")
        break

cam.release()

cv2.destroyAllWindows()
print("Reached here")


results = alpr.recognize_file(filename)




i = 0
for plate in results['results']:
    i += 1
    print("Plate #%d" % i)
    print("   %12s %12s" % ("Plate", "Confidence"))
    for candidate in plate['candidates']:
        prefix = "-"
        if candidate['matches_template']:
            prefix = "*"

        p=candidate['plate']
        c=candidate['confidence']
        break
print("I am " + str(c) + "% confident that it is plate number " + p)
        
# Call when completely done to release memory
alpr.unload()
os.remove("/home/pi/plates/" + filename)



