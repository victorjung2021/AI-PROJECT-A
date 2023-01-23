import pandas as pd
data = pd.read_csv('pricedata.csv')

# #print(data.isnull().sum())
data = data.dropna()
#data = data.fillna(100)
# #print(data['gpa'].count())

y데이타 = data['avgPrice'].values
x데이타 = []

for i, rows in data.iterrows():
    x데이타.append([ rows['avgTemp'],rows['minTemp'],rows['maxTemp'],rows['rainFall'] ])

#print(x데이타)
#print(y데이타)

#exit()

import numpy as np
import tensorflow as tf
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(1, activation='linear'),
     tf.keras.layers.Dense(1, activation='linear'),
   ])

model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit( np.array(x데이타) , np.array(y데이타), epochs=10)

예측값 = model.predict([[8,4.9,11.3,10.8]])
print(예측값)