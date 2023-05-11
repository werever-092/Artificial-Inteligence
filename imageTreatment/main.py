from __future__ import print_function
import cv2

#image path
image_path = "C:\\Users\\ISND89\\Documents\\Luisillo\\IA\\Imagenes\\vice_city.jpg"

#Read or load image from its path
image = cv2.imread(image_path)

#Image is a NumPy array
print("Dimensions of the image: ", image.ndim)
print("Image Height: ", format(image.shape[0]))
print("Image Width: ", format(image.shape[1]))
print("Image Channels: ", format(image.shape[2]))
print("Size of the image array: ", image.size)

#Display image
cv2.imshow("My image", image)
cv2.waitKey()

#Set start and end coordinates
start = (0, 0)
end = (image.shape[1], image.shape[0])

#Set the color bgr
color = (255, 0, 0)

#set thickness in pixel
thickness = 4
cv2.line(image, start, end, color, thickness)

#Display the modified image
cv2.imshow("Modified image", image)
cv2.waitKey()

#Set top-left and bottom-right corners of the rectangle
start = (100, 70)
end = (350, 380)

#Set color and thickness of the outline
color = (0, 255, 0)
thickness = 5

#Draw the rectangle
cv2.rectangle(image, start, end, color, thickness)

#save the modified image with the rectangle drwn on it
cv2.imshow("Rectangle", image)
cv2.waitKey()

