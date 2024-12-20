import cv2
import numpy as np
import matplotlib.pyplot as plt

# Leer imagen
imagen = cv2.imread('C:/Users/drago/Downloads/triangulo.png')
gris = cv2.cvtColor(imagen,cv2.COLOR_BGR2GRAY)
bordes = cv2.Canny(imagen, 100, 200)
# Muestra imagen en una ventana 
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen color', gris)
cv2.imshow('Imagen gris bordes', bordes)
# Espera hasta que el usuario presione una tecla
cv2.waitKey(0)
# Cierra todas las ventanas
cv2.destroyAllWindows()