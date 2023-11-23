from getPicture import capturePicture
from keras.models import load_model
import keras.utils as image
import numpy as np
import sys
from termcolor import colored, cprint
from dataGyro import dataGyro
import matplotlib.pyplot as plt

# Load the model
model = load_model('models/PKM-KC_1.h5')

IMG_SIZE = 300


def loadImage(img_path, show=False):
    img = image.load_img(img_path, target_size=(IMG_SIZE, IMG_SIZE))
    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.
    if show:
        plt.imshow(img_tensor[0])
        plt.axis('off')
        plt.show()
    return img_tensor


path = 'img/Positive/1699373249868.jpg'
img = loadImage(path, False)

output = model.predict(img)
color_txt = 'green'
if output < 0.5:
    color_txt = 'red'

cprint(f'Probability: {output[0][0]*100:.2f}%', color_txt)
print("="*26)
print("Tingkat Nafsu Makan Tinggi" if output >=
      0.5 else "Tingkat Nafsu Makan Rendah")

# if output >= 0.5:
#   dataGyro()
