import keras
from PIL import Image, ImageOps
import numpy as np

def teachable_machine_classification(img):
   model = keras.models.load_model(r"C:\Users\prsin\OneDrive\Documents\python_files\Streamlit\converted_keras\P_choice.h5")
   data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
   image = img
   size = (224, 224)
   image = ImageOps.fit(image, size, Image.ANTIALIAS)
   image_array = np.asarray(image)
   normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
   data[0] = normalized_image_array
   prediction = model(data)
   #print(prediction)
   #print(np.argmax(prediction))
   label = np.argmax(prediction)
   return label