import numpy as np
import tensorflow as tf
from PIL import Image

with open('plantvillage_model.json', 'r') as json_file:
    json_savedModel = json_file.read()

# load the model architecture
model = tf.keras.models.model_from_json(json_savedModel)
model.load_weights('plantvillage_weights.h5')
model.compile(optimizer="Adam",loss="sparse_categorical_crossentropy", metrics=["accuracy"])

labels = ['Corn_Blight',
 'Corn_Common_Rust',
 'Corn_Gray_Leaf_Spot',
 'Corn_Healthy',
 'Pepper__bell___Bacterial_spot',
 'Pepper__bell___healthy',
 'Potato___Early_blight',
 'Potato___Late_blight',
 'Potato___healthy',
 'Tomato_Bacterial_spot',
 'Tomato_Early_blight',
 'Tomato_Late_blight',
 'Tomato_Leaf_Mold',
 'Tomato_Septoria_leaf_spot',
 'Tomato_Spider_mites_Two_spotted_spider_mite',
 'Tomato__Target_Spot',
 'Tomato__Tomato_YellowLeaf__Curl_Virus',
 'Tomato__Tomato_mosaic_virus',
 'Tomato_healthy']


def classify_image(file_path):
    image = Image.open(file_path)
    img = np.asarray(image)

    img = np.expand_dims(img, 0)
    #shape = list(img.shape)
    #img = np.reshape(-1, img)

    predictions = model.predict(img)

    c = np.argmax(predictions[0])
    cls = labels[c]

    result = {
        'class': cls,
        'class_probability': round(predictions[0][c], 2),
    }

    return result
