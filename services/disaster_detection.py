import cv2
import tensorflow as tf
import numpy as np

model = tf.keras.models.load_model("models/disaster.h5")
categories = ["fire", "flood", "earthquake", "normal"]  # adjust based on your model

camera = cv2.VideoCapture(0)

def run_disaster_detection():
    ret, frame = camera.read()
    if not ret:
        return "No Input"

    img = cv2.resize(frame, (128, 128)) / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)
    return categories[np.argmax(prediction)]
