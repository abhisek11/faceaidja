from django.shortcuts import render

#initializing the imports
import numpy as np
import urllib
import json
import cv2
import os
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

face_detector = "/home/abhisek/Desktop/faceai/haarcascade_frontalface_default.xml"

@csrf_exempt
#default value to be set false 
def requested_url(request):
    default = {"safely executed":False} #because no detection yet 

    #betweene GET and POST we go for post request and check for https 
    if request.method =="POST":
        if request.FILEs.get("image",None) is not None:
            image_to_read = read_image(stream=request.FILES["image"])

        else:#url is provided by user 
            url_provided = request.POST.get()

            if url_provided is None:
                default["error value"]= "There is no url provided"
                return JsonResponse(default)