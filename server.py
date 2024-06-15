import os
import torch
import argparse
from flask import Flask, request, render_template, jsonify
import imageio
import re
import base64
from PIL import Image
from model.eminist import EMNISTNet, predict_char


app = Flask(__name__)
def load_model(model_path):
    ''' Load PyTorch model from .pt file

        Arguments:
            model_path: The path of the model

        Returns:
            Loaded PyTorch model from file
    '''
    model = EMNISTNet(False)
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    model.eval()  # Set the model to evaluation mode
    return model
model = load_model('bin/parameters.pt')

@app.route("/")
def index():
    ''' Render index for user connecting to /
    '''
    return render_template('index.html')

@app.route('/predict/', methods=['GET','POST'])
def predict():
    ''' Called when user presses the predict button.
        Processes the canvas and handles the image.
        Passes the loaded image into the neural network and it makes
        class prediction.
    '''
    def parseImage(imgData):
        # parse canvas bytes and save as output/output.png
        imgstr = re.search(b'base64,(.*)', imgData).group(1)
        with open('output/output.png','wb') as output:
            output.write(base64.decodebytes(imgstr))

    # get data from drawing canvas and save as image
    parseImage(request.get_data())
    
    # read parsed image back in 8-bit, black and white mode (L)
    img = Image.open('output/output.png')
    
    # Convert to grayscale mode (L)
    grayscale_img = img.convert('L') 
    
    # Invert the image (optional)
    inverted_img = grayscale_img.point(lambda p: 255 - p)  # Invert pixel values
    
    # Resize the image to (28, 28) 
    img = inverted_img.resize((28, 28))
    imageio.imsave('output/resized.png', img)
    
    prediction_char, precent = predict_char(model, 'output/resized.png')
    response = {
        'prediction': prediction_char,
        'confidence': precent
    }

    return jsonify(response)

# if __name__ == '__main__':
#     # Parse optional arguments
#     parser = argparse.ArgumentParser(description='A webapp for testing models generated from training.py on the EMNIST dataset')
#     parser.add_argument('--bin', type=str, default='bin/parameters.pt', help='model pt file')
#     parser.add_argument('--host', type=str, default='0.0.0.0', help='The host to run the flask server on')
#     parser.add_argument('--port', type=int, default=5000, help='The port to run the flask server on')
#     args = parser.parse_args()

#     # Overhead
#     model = load_model(args.bin)
#     # # mapping = pickle.load(open(f'{args.bin}/mapping.p', 'rb'))
#     # model.eval()
#     # print(model)

#     app.run(host=args.host, port=args.port)
