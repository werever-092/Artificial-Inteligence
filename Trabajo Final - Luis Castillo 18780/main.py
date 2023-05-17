import numpy as np
import cv2 as cv

#Image Path
image_path = "image\spiderman_sit.jpg"

#Read Image
image = cv.imread(image_path)

#Gray Scale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.namedWindow('Gray', cv.WINDOW_KEEPRATIO)
cv.imshow('Gray', gray)
cv.waitKey()

#Smoothing image
smooth = cv.blur(image, (10, 10))
cv.namedWindow('Smooth', cv.WINDOW_KEEPRATIO)
cv.imshow('Smooth', smooth)
cv.waitKey()

#Edge Detection
edges = cv.Canny(image, 100, 200)
cv.namedWindow('Edges', cv.WINDOW_KEEPRATIO)
cv.imshow('Edges', edges)
cv.waitKey()

#Find, Draw & Count Contours
contours, _ = cv.findContours(edges.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(image, contours, -1, (0, 0, 255), 2)
cv.imshow('Contours', image)
cv.waitKey()

#Count Countours
print("Se han encontrado {} objetos".format(len(contours)))