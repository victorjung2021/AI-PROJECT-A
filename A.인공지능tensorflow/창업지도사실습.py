import os
import numpy as np
import matplotlib.pyplot as plt

os.environ['KERAS_BACKEND'] = 'theano' #디폴트는 tensorflow임.
from keras import backend, models, layers, utils


x=[0,1,2,3,4,5,6,7,8,9]
y=[1.,2.97,5.11,7.,9.05,10.79,13.12,15.,16.88,19.03]

print(x)
print(y)

model = models.Sequential([
    layers.Dense(1, input_shape=(1,)),
    layers.Activation('linear')
])

model.compile(optimizer='sgd', #stochastic gradient descent optimizer
loss='mean_squared_error')
model.fit( x,y, epochs=10)

X=[12,15]
Y = model.predict(X)

fig_size = plt.rcParams['figure.figsize'] = [16,8]
plt.title('Single perceptron learning (x1)')
plt.xlabel('x')
plt.xlabel('y')
plt.scatter(x,y, color='black')
plt.scatter(X,Y, color='gray')
plt.grid()
plt.show()

