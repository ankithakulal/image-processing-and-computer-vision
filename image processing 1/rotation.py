import cv2
import numpy as np 
import matplotlib.pyplot as plt
image=cv2.imread("C:/Users/ankit/Pictures/flower.jfif")
cv2.imshow('original',image)
cv2.waitKey(0) 
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('grayscale',gray_image)
center = (gray_image.shape[1] // 2, gray_image.shape[0] // 2)
angle = 60
scale = 2
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(gray_image, rotation_matrix, (image.shape[1], image.shape[0]))
fig, axs = plt.subplots(1, 2, figsize=(7, 4))


axs[0].imshow(gray_image)
axs[0].set_title('Original Image')
 

axs[1].imshow(rotated_image)
axs[1].set_title('Image Rotation')


for ax in axs:
    ax.set_xticks([])
    ax.set_yticks([])


plt.tight_layout()
plt.show()
cv2.waitKey(0) 
cv2.destroyAllWindows()