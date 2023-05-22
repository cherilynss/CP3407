import cv2
from flask import Flask

app = Flask(__name__)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

try:
    cap = cv2.VideoCapture(1)
except:
    cap = cv2.VideoCapture(0)
