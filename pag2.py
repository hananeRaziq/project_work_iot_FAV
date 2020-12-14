import streamlit as st
import plotly.figure_factory as ff
from PIL import Image
import pandas as pd
import numpy as np


import cv2 
import time
import numpy as np
import os
from pydub import AudioSegment
from pydub.playback import play
import csv
from datetime import datetime
from io import BytesIO
import base64
import warnings
warnings.filterwarnings('ignore')
import matplotlib.image as mpimg

RASPBERRY = False
if RASPBERRY:
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)


def get_time():
    # d = datetime.now().strftime("%m:%d:%Y-%H:%M:%S")
    d = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    return d

def write_data_on_csv(filename, listdata):
    with open(filename, mode='a') as f:
        fw = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        fw.writerow(listdata)

def findLargestBB(bbs):
    areas = [w*h for x,y,w,h in bbs]
    if not areas:
        return False, None
    else:
        i_biggest = np.argmax(areas) 
        biggest = bbs[i_biggest]
        return True, biggest

def main():
    
    st.title("Mask Detector")

    cap = cv2.VideoCapture(0)

    choice = st.radio(label="", options=["Start","Stop"], index=1)  #,"Analisi"
 
    if choice=="Start":
        
        st.subheader("Mask Detector: Started")

        cascade_masks = cv2.CascadeClassifier(os.path.join('models','mask_cascade.xml'))
        cascade_faces = cv2.CascadeClassifier(os.path.join('models','haarcascade_frontalface_default.xml'))
        
        text_placeholder = st.empty()
        image_placeholder = st.empty()

        speak_no = 0
        speak_yes = 0
        
        person_detected = 0

        while(True):
            # Capture frame-by-frame
            ret, im_color = cap.read()


            # Our operations on the frame come here
            im_gray = cv2.cvtColor(im_color, cv2.COLOR_BGR2GRAY)

            masks = cascade_masks.detectMultiScale(im_gray, 1.01,5,cv2.CASCADE_DO_ROUGH_SEARCH | cv2.CASCADE_SCALE_IMAGE)
            faces = cascade_faces.detectMultiScale(im_gray, 1.1,4,cv2.CASCADE_DO_ROUGH_SEARCH | cv2.CASCADE_SCALE_IMAGE)
            
            resMasks, biggestMask = findLargestBB(masks)
            resFaces, biggestFace = findLargestBB(faces)
            if resFaces:
                (x,y,w,h) = biggestFace
                roi = im_gray[y:y+h,x:x+w]
                cv2.rectangle(im_color,(x,y),(x+w,y+h),(255,255,0),2)

            if resMasks or resFaces:
                person_detected = person_detected + 1
            else:
                person_detected = 0
        
            if person_detected >=3:
                if resMasks:
                    (x,y,w,h) = biggestMask
                    roi = im_gray[y:y+h,x:x+w]
                    cv2.rectangle(im_color,(x,y),(x+w,y+h),(255,0,0),2)
        
                    text_placeholder.success("Mascherina indossata correttamente \U0001f600")
                    speak_yes = speak_yes + 1
                    if speak_yes > 5: 
                        song = AudioSegment.from_wav(os.path.join("audio","procedere.wav"))
                        play(song)
                        speak_yes=0
                        
                        time_print = get_time()
                        storage_url = os.path.join("storage/mask/", time_print+".png")
                        cv2.imwrite(storage_url, im_color)
                        write_data_on_csv(filename="data.csv",listdata=[time_print,"mask", storage_url])

                        if RASPBERRY:
                            GPIO.setup(2,GPIO.OUT)
                            GPIO.output(2,GPIO.HIGH)

                    speak_no=0
                else:
                    text_placeholder.error("Indossare la Mascherina")
                    speak_no = speak_no + 1
                    if speak_no > 3:
                        song = AudioSegment.from_wav(os.path.join("audio","indossare_mascherina.wav"))
                        play(song)
                        speak_no=0

                        time_print = get_time()
                        storage_url = os.path.join("storage/no-mask/", time_print+".png")
                        cv2.imwrite(storage_url, im_color)
                        write_data_on_csv(filename="data.csv",listdata=[time_print,"no-mask",storage_url])

                        if RASPBERRY:
                            GPIO.output(2,GPIO.LOW)
    
                    speak_yes = 0

            image_placeholder.image(im_color, channels="BGR", use_column_width=True)
            time.sleep(0.033) # 30 Hz
    
    else:
        st.subheader("Mask Detector: Stopped")
        cap.release()
    

    img=mpimg.imread('people_mask.jpg')
    st.image(img, caption='',use_column_width=True)

if __name__ == "__main__":
    face_cascade = cv2.CascadeClassifier(os.path.join('models','mask_cascade.xml'))

    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, im_color = cap.read()

        im_color = cv2.resize(im_color, (640,480))

        # Our operations on the frame come here
        im_gray = cv2.cvtColor(im_color, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(im_gray, 1.1,5)

        for (x,y,w,h) in faces:
            roi = im_gray[y:y+h,x:x+w]
            cv2.rectangle(im_color,(x,y),(x+w,y+h),(255,0,0),2)


        # Display the resulting frame
        cv2.imshow('frame',im_color)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()




