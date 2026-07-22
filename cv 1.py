import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread(r"C:\Users\Student\Desktop\khushi shetty\Cancerous-Cell.jpg")
image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

# 1. BRIGHTNESS 
bright=cv2.add(image,np.ones(image.shape,dtype="uint8")*50)
dark=cv2.subtract(image,np.ones(image.shape,dtype="uint8")*50)

# 2 flip 
h_flip=cv2.flip(image,1)
v_flip=cv2.flip(image,0)

#3  color channels
red=image[:,:,0]
green=image[:,:,1]
blue=image[:,:,2]

#4  gray scales
gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

#5 negative
negative=255-image

# display all images
plt.figure(figsize=(18,12))

plt.subplot(3,4,1)
plt.imshow(image);   plt.title('original'); plt.axis('off')
plt.subplot(3,4,2)
plt.imshow(bright);  plt.title('brighter +50'); plt.axis('off')
plt.subplot(3,4,3)
plt.imshow(dark);  plt.title('darker -50'); plt.axis('off')

plt.subplot(3,4,5)
plt.imshow(h_flip);  plt.title('h-flip');  plt.axis('off')
plt.subplot(3,4,6)
plt.imshow(v_flip);  plt.title('v-flip');  plt.axis('off')

plt.subplot(3,4,7)
plt.imshow(red);  plt.title('red ');  plt.axis('off')
plt.subplot(3,4,8)
plt.imshow(green);  plt.title('green ');  plt.axis('off')
plt.subplot(3,4,9)
plt.imshow(blue);  plt.title('blue');  plt.axis('off')

plt.subplot(3,4,10)
plt.imshow(gray);  plt.title('gray');  plt.axis('off')
plt.subplot(3,4,11)
plt.imshow(negative);  plt.title('negative');  plt.axis('off')

plt.tight_layout()
plt.show()
plt.subplot(1,3,2)
plt.imshow(bright); 
plt.title('brighter +50'); 
plt.axis('off')

plt.subplot(1,3,3)
plt.imshow(dark)
plt.title('darker -50')
plt.axis('off')

plt.show()