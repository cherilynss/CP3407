import cv2
from flask import Flask

app = Flask(__name__)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

