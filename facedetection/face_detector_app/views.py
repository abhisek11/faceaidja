from django.shortcuts import render

#initializing the imports
import numpy as np
import urllib
import json
import cv2
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

face_detector = "/home/abhisek/Desktop/haarcascade_frontalface_default.xml"
