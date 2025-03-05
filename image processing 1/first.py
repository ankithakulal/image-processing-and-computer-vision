import cv2
image = cv2.imread("C:/Users/ankit/Pictures/flower.jfif")
px = image[50,50]

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
blue = image[100,100,0]
print(blue)
green=image[100,100,0]
print(green)

print(image.shape)

print(image.dtype)
