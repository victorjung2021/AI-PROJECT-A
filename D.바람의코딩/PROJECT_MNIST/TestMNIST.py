import sys, os
sys.path.append(os.pardir)
import numpy as np
import pickle
from data_mnist.mnist import load_mnist
from common.function import sigmoid, softmax
from PIL import Image
