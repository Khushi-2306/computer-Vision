import cv2
import matplotlib.pyplot as plt

# Step 1: Read the image
image = cv2.imread(r"C:\Users\Student\Desktop\khushi shetty\Cancerous-Cell.jpg")
T=231
# Step 2: Convert to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Convert Grayscale to RGB
rgb = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

# Step 4: Display all images
plt.figure(figsize=(15, 5))

# Original Image
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Step 1: Original Image")
plt.axis("off")

# Grayscale Image
plt.subplot(1, 3, 2)
plt.imshow(gray, cmap="gray")
plt.title("Step 2: Grayscale Image")
plt.axis("off")

# RGB Image
plt.subplot(1, 3, 3)
plt.imshow(rgb)
plt.title("Step 3: RGB Image")
plt.axis("off")

plt.tight_layout()
plt.show()

