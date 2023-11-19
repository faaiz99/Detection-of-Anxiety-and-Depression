from typing import Union
from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
from typing import List
import numpy as np
import cv2
from keras.models import model_from_json
from keras.preprocessing import image
import keras.utils as image
app = FastAPI()

model = model_from_json(open("fer.json", "r").read())
#load weights
model.load_weights('fer.h5')
face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


@app.post("/process_image/")
async def process_image(files: List[UploadFile] = File(...)):
    if not files:
        raise HTTPException(status_code=400, detail="No file provided")

    # Process each uploaded file
    results = []
    for file in files:
        try:
            contents = await file.read()
            test_img = cv2.imdecode(np.frombuffer(contents, np.uint8), cv2.COLOR_BGR2GRAY)
            gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

            faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)

            for (x,y,w,h) in faces_detected:
                cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=3)
                roi_gray=gray_img[y:y+w,x:x+h]#cropping region of interest i.e. face area from  image
                roi_gray=cv2.resize(roi_gray,(48,48))
                img_pixels = image.img_to_array(roi_gray)
                img_pixels = np.expand_dims(img_pixels, axis = 0)
                
                img_pixels = img_pixels.astype('float64') / 255 #normalizing

                predictions = model.predict(img_pixels)

                #find max indexed array
                max_index = np.argmax(predictions[0])

                emotions = ('angry', 'disgust', 'Anxiety', 'happy', 'Depressed', 'surprise', 'neutral')
                predicted_emotion = emotions[max_index]

            return predicted_emotion
        except Exception as e:
            results.append(str(e))
            
    return results
    
@app.get('/test')
def here():
    return {"test": "workings"}
