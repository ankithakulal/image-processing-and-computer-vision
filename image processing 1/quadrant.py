
import cv2
import matplotlib.pyplot as plt

def divide_image_into_quadrants(image):
    if image is None:
        raise ValueError("Error: Image not found. Check the file path.")

    height, width = image.shape[:2]

    mid_x, mid_y = width // 2, height // 2  # Floor division ensures integer values

    top_left = image[:mid_y, :mid_x]
    top_right = image[:mid_y, mid_x:]
    bottom_left = image[mid_y:, :mid_x]
    bottom_right = image[mid_y:, mid_x:]

    return top_left, top_right, bottom_left, bottom_right

# Load Image (Ensure the path is correct)
image_path = "C:/Users/ankit/Pictures/flower.jfif"  # Change this to your correct path
img = cv2.imread(image_path)

# Divide the image into quadrants
quadrants = divide_image_into_quadrants(img)

# Convert BGR to RGB for displaying with Matplotlib
quadrants_rgb = [cv2.cvtColor(q, cv2.COLOR_BGR2RGB) for q in quadrants]

# Display images using Matplotlib
plt.figure(figsize=(6, 6))

titles = ["Top Left", "Top Right", "Bottom Left", "Bottom Right"]

for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(quadrants_rgb[i])
    plt.title(titles[i])
    plt.axis('off')

plt.tight_layout()
plt.show()
