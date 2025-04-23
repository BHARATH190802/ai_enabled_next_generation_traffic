from typing import Any
from django.shortcuts import render

from .serializers import *
# from .apps import model
from rest_framework import generics, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import os
import torch
import base64
from PIL import Image
import io
import cv2
import numpy as np


class predict(APIView):

    def get(self, request):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            cv2.imshow("Webcam feed for traffic", frame)

            if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
                break

        cap.release()
        cv2.destroyAllWindows()

    def post(self, request):
        # print("The Model is Loading......")
        # model = self.load_model()
                
        print("The Model is Loading......")
        path_hubconfig = "yolov5"
        path_weightfile = "predict//best.pt"  # or any custom trained model

        model = torch.hub.load(
            path_hubconfig, "custom", path=path_weightfile, source="local"
        )
        

        width=80
        time=[]
        
        im = Image.open(io.BytesIO(request.data["j1"].read()))
        res = model(im)

        
        pred = res.pandas().xyxy[0].value_counts("name")
        vech = list(pred.index)
        if len(vech) != 0:
            Vech_weights = {
                "ambulance": 10,
                "army vehicle": 8,
                "auto rickshaw": 4,
                "bicycle": 1,
                "bus": 5,
                "car": 3,
                "garbagevan": 7,
                "human hauler": 5,
                "minibus": 6,
                "minivan": 5,
                "motorbike": 2,
                "pickup": 4,
                "policecar": 4,
                "rickshaw": 3,
                "scooter": 2,
                "suv": 7,
                "taxi": 5,
                "three wheelers (CNG)": 3,
                "truck": 7,
                "van": 3,
                "wheelbarrow": 3,
            }

            sum = 0
            for i in vech:
                sum += pred[i] * Vech_weights[i]


            density = sum / (width*20)
            print(density)
        # for i in ["j1","j2","j3","j4"]:

        #     im = Image.open(io.BytesIO(request.data[i].read()))
        #     # im = Image.open(i)

        # res = model(im)


        #     boxes = res.xyxy[0].detach().cpu().numpy()
        #     labels = res.names

        #     image_np = np.array(im)

        #     for box in boxes:
        #         x1, y1, x2, y2, confidence, class_idx = box
        #         label = labels[int(class_idx)]
        #         cv2.rectangle(
        #             image_np, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2
        #         )
        #         cv2.putText(
        #             image_np,
        #             label,
        #             (int(x1), int(y1 - 10)),
        #             cv2.FONT_HERSHEY_SIMPLEX,
        #             0.9,
        #             (0, 255, 0),
        #             2,
        #         )

        #     # image_pil = Image.fromarray(image_np)
        #     # image_bytes = io.BytesIO()
        #     # image_pil.save(image_bytes, format="PNG")
           
        #     # img = base64.b64encode(image_bytes.getvalue()).decode()

        # #     # Code to calculate Traffic density

        #     pred = res.pandas().xyxy[0].value_counts("name")
        #     vech = list(pred.index)
        #     if len(vech) != 0:
        #         Vech_weights = {
        #             "ambulance": 10,
        #             "army vehicle": 8,
        #             "auto rickshaw": 4,
        #             "bicycle": 1,
        #             "bus": 5,
        #             "car": 3,
        #             "garbagevan": 7,
        #             "human hauler": 5,
        #             "minibus": 6,
        #             "minivan": 5,
        #             "motorbike": 2,
        #             "pickup": 4,
        #             "policecar": 4,
        #             "rickshaw": 3,
        #             "scooter": 2,
        #             "suv": 7,
        #             "taxi": 5,
        #             "three wheelers (CNG)": 3,
        #             "truck": 7,
        #             "van": 3,
        #             "wheelbarrow": 3,
        #         }

        #         sum = 0
        #         for i in vech:
        #             sum += pred[i] * Vech_weights[i]


        #         density = sum / (width*20)
                
        #         if(density==0):
        #             time.append(20)

        #         elif(density<5):
        #             time.append(density*20)
        #         else:
        #             time.append(120)

    
        return Response({"density":density})

