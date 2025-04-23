from PIL import Image
import os
import cv2
# import pygame
import torch
import requests
import numpy as np


Vech_weights={'ambulance': [50, 37.5],
 'army vehicle': [40, 24.2],
 'auto rickshaw': [30, 6.75],
 'bicycle': [15, 1.188],
 'bus': [40, 105.0],
 'car': [50, 12.15],
 'garbagevan': [30, 27.5],
 'human hauler': [25, 10.8],
 'minibus': [40, 25.0],
 'minivan': [45, 17.28],
 'motorbike': [40, 1.92],
 'pickup': [45, 18.0],
 'policecar': [50, 12.96],
 'rickshaw': [20, 5.4],
 'scooter': [35, 1.512],
 'suv': [55, 15.552],
 'taxi': [45, 12.15],
 'three wheelers (CNG)': [30, 6.75],
 'truck': [40, 45.0],
 'van': [45, 25.0],
 'wheelbarrow': [5, 0.576]}

capacity=100
density=0.0

path = os.getcwd()
dir_list = os.listdir(path+'//images//traffic//')

def calc_density(rounds,model):
    
    image_path ="images/traffic/"+dir_list[rounds-1]
    img = Image.open(image_path).convert('RGB')
    res = model(img)

    boxes = res.xyxy[0].detach().cpu().numpy()
    labels = res.names

    pred = res.pandas().xyxy[0].value_counts("name")
    vech = list(pred.index)

    image_np = np.array(img)
    
    for box in boxes:
        x1, y1, x2, y2, confidence, class_idx = box
        label = labels[int(class_idx)]
        # sum += (pred[i] * Vech_weights[i][1])/Vech_weights[i][0]
        cv2.rectangle(
            image_np, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2
        )
        cv2.putText(
            image_np,
            label,
            (int(x1), int(y1 - 10)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0, 255, 0),
            2,
        )
    # Resize the image to 30x30
    image_np = cv2.resize(image_np, (300, 300))
    if len(vech) != 0:
        sum=0
        for i in vech:
            # if(i=='person'):
            #     continue
            sum += (pred[i] * Vech_weights[i][1])/Vech_weights[i][0]
        # print("Density:",sum/capacity)
        density=sum/capacity
    else:
        density=0
    # density=
    # image_pil = Image.fromarray(image_np)
    # image_bytes = io.BytesIO()
    # image_pil.save(image_bytes, format="PNG")
    print("density",density)
    return  image_np,density*10       #round(density,3)

































# pygame.init()

# # Create a Pygame window
# screen = pygame.display.set_mode((1400,800))
# pygame.display.set_caption('YOLOv5 Detection')

# image_data=[[],[],[],[]]
# # # Load pre-trained YOLOv5 model
# model = torch.hub.load('ultralytics/yolov5:v6.0', 'yolov5s')
# image_data[0]=calc_density(1,1,model)

# image_data = pygame.surfarray.make_surface())
# print(np.transpose(image_data[0], (1, 0, 2)).shape)

# Convert the NumPy array to a Pygame surface


# # Run the Pygame event loop
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # Display the Pygame surface
#     screen.blit(image_data, (10,10))
#     pygame.display.flip()

# # Close Pygame
# pygame.quit()