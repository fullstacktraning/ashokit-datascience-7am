# tensorflow - Deep Learning Library (Engine)
import tensorflow as tf

# keras - used to build Deep Learning Models (Steering)
from tensorflow import keras

import numpy as np

# create model
model = keras.Sequential([
    keras.layers.Dense(3,activation='relu'),
    keras.layers.Dense(1)
])

# compile the model
model.compile(
    optimizer='adam',
    loss='mean_squared_error'
)

X = np.array([[1],[2],[3],[4]], dtype=float)

y = np.array([[2],[4],[6],[8]], dtype=float) # y = 2x

model.fit(X,y, epochs=500)

print( model.predict(np.array([[5.0]])) )

