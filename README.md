EMNIST
=====

![](https://raw.githubusercontent.com/hung-manh/eminist/main/static/preview.gif)

##### Description

This project was intended to explore the properties of convolution neural networks (CNN) and see how they compare to recurrent convolution neural networks (RCNN). This was inspired by a [paper](http://www.cv-foundation.org/openaccess/content_cvpr_2015/app/2B_004.pdf "Recurrent Convolutional Neural Network for Object Recognition") I read that details the effectiveness of RCNNs in object recognition as they perform or even out perform their CNN counterparts with fewer parameters. Aside from exploring CNN/RCNN effectiveness, I built a simple interface to test the more challenging [EMNIST dataset](https://arxiv.org/abs/1702.05373 "EMNIST: an extension of MNIST to handwritten letters") dataset (as opposed to the [MNIST dataset](http://yann.lecun.com/exdb/mnist/ "THE MNIST DATABASE of handwritten digits"))

##### Current Implementation
  * Multistack CNN
  * Web-applet testing environment
    * Touch screen compatible
    * Works best when letter takes up a good portion of the canvas
    * See [paper](https://arxiv.org/abs/1702.05373 "EMNIST: an extension of MNIST to handwritten letters") for more info

##### Todo
  * Update gif with new webapp
  * Train more models
    * RCNN
    * Optimize hyperparameters
    * Add a noise (gaussian or likewise) layer to input in an attempt to boost accuracy
  * Move webapp to a host service like PythonAnywhere
<!-- 
## Environment

#### Anaconda:  -->

## Usage
#### [training.ipynb](https://github.com/hung-manh/eminist/blob/38ac17c03b0ffcc7876524639a2a45139e7200e0/training/emnist-pytorch.ipynb)
A training program for classifying the EMNIST dataset


#### [server.py](https://github.com/hung-manh/eminist/blob/38ac17c03b0ffcc7876524639a2a45139e7200e0/server.py)
A webapp for testing models generated from [training.ipynb](https://github.com/hung-manh/eminist/blob/38ac17c03b0ffcc7876524639a2a45139e7200e0/training/emnist-pytorch.ipynb) on the EMNIST dataset

    usage: server.py [-h] [--bin BIN] [--host HOST] [--port PORT]

##### Optional Arguments:

    -h, --help   show this help message and exit
    --bin BIN    Model path pt or pth
    --host HOST  The host to run the flask server on
    --port PORT  The port to run the flask server on