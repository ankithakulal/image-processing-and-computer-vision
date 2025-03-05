import cv2
import matplotlib.pyplot as plt
image=cv2.imread("C:/Users/ankit/Pictures/flower.jfif")
# cv2.imshow("iamge",image)
half=cv2.resize(image,(0,0),fx=5,fy=5)
bigger=cv2.resize(image,(1024,1610))
stretch_near=cv2.resize(image,(780,540),interpolation=cv2.INTER_LINEAR)
Titles =["Oxriginal", "Half", "Bigger", "Interpolation Nearest"]
images =[image, half, bigger, stretch_near]
count = 4
for i in range(count):
    plt.subplot(3, 3, i + 1)
    plt.title(Titles[i])
    plt.imshow(images[i])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()