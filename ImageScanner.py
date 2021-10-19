import cv2 as cv
import numpy as np
#import imutils
import pyautogui

def takeScreenshot():
    screen = pyautogui.screenshot()
    return cv.cvtColor(np.array(screen), cv.COLOR_RGB2BGR)
    #cv.imwrite("in_memory_to_disk.png", screen)

screen = cv.imread('quizlol/Screenshot_4.png')
respuestas = ['quizlol/a/respuesta2.png','quizlol/a/respuesta3.png','quizlol/a/respuesta4.png',
              'quizlol/a/respuesta5.png','quizlol/a/respuesta6.png']
#for image in respuestas:
image = cv.imread('quizlol/a/respuesta4.png')
result = cv.matchTemplate(screen, image, cv.TM_SQDIFF)
mn,_,mnLoc,_ = cv.minMaxLoc(result)
MPx, MPy = mnLoc

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = image.shape[:2]

# Step 3: Draw the rectangle on large_image
cv.rectangle(screen, (MPx,MPy),(MPx+tcols,MPy+trows),(0,255,0),2)

# Display the original image with the rectangle around the match.
cv.imshow('output',screen)

# Perform a click 
pyautogui.click(x=MPx+140, y=MPy+120)
# The image is only displayed if we call this
cv.waitKey(0)

# Notas al pie:
# Esto encuentra la posición que más se asemeje, pero no es EXACTO, es por aproximación.
# Ideas para corregirlo:
# Que compare todas las respuestas con la pregunta y que elija la que MAS COINCIDENCIA tuvo, para ello es necesario
# entender qué significan los valores que devuelve la variable result. Si esos valores son la aproximación por pixeles
# el promedio de aproximación por pixeles más bajo debería ser el que tenga mayor coincidencia por ende la imagen que más
# se parece a la buscada.