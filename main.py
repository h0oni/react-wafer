from fastapi import FastAPI
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from tensorflow.keras import preprocessing
import PIL
import base64
from io import BytesIO
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    img: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

new_model = tf.keras.models.load_model('best.h5',custom_objects={'KerasLayer':hub.KerasLayer})

@app.get('/')
async def hello():
    return {'hello':'world'}

@app.post('/predict/')
async def test(item: Post):
    # im_b64 = item.img
    # if not(im_b64):
    #     return {'hello':'oops'}

    #b64 -> pil
    image = PIL.Image.open(BytesIO(base64.b64decode(item.img[22:])))
    image.save('test.png')

    img = preprocessing.image.load_img('test.png', target_size = (224, 224))
    np_image = np.array(img).astype('float32')/255
    np_image = np.expand_dims(np_image, axis=0)
    del image, img
    
    proba = new_model.predict(np_image)
    pred = np.argmax(proba)

    return {'hello':f'{pred} ({(100*tf.reduce_max(proba)) : .2f}%)'}
