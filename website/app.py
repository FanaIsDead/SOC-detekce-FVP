from flask import Flask, request, render_template
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import load_img, img_to_array
from io import BytesIO
import base64
from PIL import Image


app = Flask(__name__)

# load the model
model = load_model('model/bestKerasModel.keras')

# get image from stream, resize it 
def getImage(file, targetSize=(200, 200)):
    imgFile = BytesIO(file.read())
    img = load_img(imgFile, target_size=targetSize)
    imgArr = img_to_array(img)
    return img, imgArr   # returns the image and then image as array

# predict mask of current image (takes image array as a parameter)
# also highlights the area on the original image, where the mask coresponds
def getMask(imgArr):
    predictedMask = model.predict(np.expand_dims(imgArr, axis=0))[0]
    predMask = np.argmax(predictedMask, axis=-1)

    highlightColor = [0, 255, 0]

    output = imgArr.copy()
    if output.max() <= 1.0:     # convert to uint8
        output = (output * 255).astype(np.uint8)
    else:
        output = output.astype(np.uint8)

    output[predMask > 0] = (
        0.5 * output[predMask > 0] + 0.5 * np.array(highlightColor)
    ).astype(np.uint8)
    return Image.fromarray(output)  # returns original image with mask area highlighted
    
# encode the images, so flask can display it
def encodeImage(img):   
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    encoded = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return f"data:image/png;base64,{encoded}"

# main app loop
@app.route('/', methods=['GET', 'POST'])
def index():
    original_b64 = result_b64 = None

    if request.method == 'POST':    # file error handling
        if 'image' not in request.files:
            return "No file uploaded", 400
        file = request.files['image']
        if file.filename == '':
            return "No selected file", 400

        img, imgArr = getImage(file.stream)
        mask = getMask(imgArr)
        original_b64 = encodeImage(img)
        result_b64 = encodeImage(mask)

    return render_template('index.html', original=original_b64, result=result_b64)      # render the images onto the site

if __name__ == '__main__':
    app.run(debug=True)
