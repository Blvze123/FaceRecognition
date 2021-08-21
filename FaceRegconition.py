import cv2
from simple_facerec import SimpleFacerec
import os.path
import time

def capture():
    sfr = SimpleFacerec()
    #Load Camera
    cap = cv2.VideoCapture(0)
    
    capture.Found = False
    sfr.load_encoding_images("Encodes/")
    
    while capture.Found != True:
        ret, frame = cap.read()
        
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            cv2.putText(frame, name, (x1, y1-10), cv2.FONT_HERSHEY_DUPLEX,1, (0,0,200), 2);
            cv2.rectangle(frame, (x1,y1), (x2,y2), (0,0,200), 2)
            if name == "Found":
                capture.Found = True
                cv2.destroyAllWindows()
                break
                
    
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()



if os.path.exists("Encodes/Found.jpg"):
    print("Setup Already Found")
    capture()
    print(capture.Found)
else:
    x = input("Do you wish to setup right now,(y/n) \n")
    
    if x== "n":
        quit()
    elif x== "y":
       print("Taking Picture in 5 Seconds, Save Picture by pressing Y") 
       time.sleep(5)
       cap = cv2.VideoCapture(0)  
       ret,frame = cap.read() 
       while(True):
           cv2.imshow('img1',frame) 
           if cv2.waitKey(1) & 0xFF == ord('y'): 
               cv2.imwrite('Encodes/Found.jpg',frame)
               cv2.destroyAllWindows()
               break
    
       cap.release()
       print("Picture taken. Now Exiting...")
       quit()






















    