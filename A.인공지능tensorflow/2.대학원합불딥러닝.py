import pandas as pd
data = pd.read_csv('gpascore.csv')
data = data.dropna()

y데이타 = data['admit'].values
x데이타 = []

for i, rows in data.iterrows():
    x데이타.append([ rows['gre'],rows['gpa'],rows['rank'] ])

import numpy as np
import tensorflow as tf
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit( np.array(x데이타) , np.array(y데이타), epochs=800)

예측값 = model.predict( [ [560, 3.70, 2], [700, 2.2, 3], [900, 4.0, 2] ])
print(예측값)