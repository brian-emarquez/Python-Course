############################################
# face Recognition
# Detencion de Rostros
############################################

import cv2
import os
import imutils

PersonalName = "Brian"
dataPath="Reconocimiento Facial/data"
personPath = dataPath +'/'+ PersonalName

if not os.path.exists(personPath):
    print('Carperta creda', personPath)
    os.makedirs(personPath)


