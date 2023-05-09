import numpy as np
import cv2

#Leer una imagen
img = cv2.imread('C:\\Users\\ISND89\\Documents\\Luisillo\\IA\\Imagenes\\certified_lover_boy.jpg',1)
#Mostrar imagen
cv2.imshow('Conalep', img)
cv2.waitKey()

#Imagen en escala de grises
img_gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Grises', img_gris)
cv2.waitKey()

#Filtro agrgar filtro suavizado
filtro_gauss = cv2.GaussianBlur(img, (5, 5), 0)
cv2.imshow('Blur', filtro_gauss)
cv2.waitKey()

#Deteccion de bordes
bordes_canny = cv2.Canny(img, 100, 200)
cv2.imshow('Bordes', bordes_canny)
cv2.waitKey()