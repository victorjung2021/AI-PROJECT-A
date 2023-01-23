import sys, os
sys.path.append(os.pardir)
import numpy as np

from dataset.mnist import load_mnist
from PIL import Image
exit() 

(train_images, train_labels), (test_images,test_labels) = datasets.mnist.load_data()

np.set_printoptions(linewidth=200,threshold=1000)
(x_train,t_train), (x_test, t_test) = load_mnist(flatten=False,normalize=False)

print(x_train[0])
