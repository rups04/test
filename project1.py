
from keras.datasets import mnist

import numpy as np

from keras.layers import Convolution2D

from keras.layers import MaxPooling2D

from keras.layers import Flatten

from keras.layers import Dense

from keras.models import Sequential

from keras.utils import np_utils

model = Sequential()

(x_train, y_train), (x_test, y_test)  = mnist.load_data()

img_rows = x_train[0].shape[0]
img_cols = x_train[0].shape[0]

x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)


input_shape = (img_rows, img_cols, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)

y_train.shape


model = Sequential()

model.add(Convolution2D(filters=20, 
                        kernel_size=(5,5), 
                        activation='relu',
                   input_shape=input_shape
                       ))
model.add(MaxPooling2D(pool_size=(3,3)))


model.add(Flatten())
model.add(Dense(units=128, activation='relu'))


model.add(Dense(units=y_train.shape[1], activation='softmax'))
           
model.compile(loss = 'categorical_crossentropy',
              optimizer = 'adam',
              metrics = ['accuracy'])
    
print(model.summary())


epochs = 1
history = model.fit(x_train, y_train,
         
          epochs=epochs,
          validation_data=(x_test, y_test),
          )
model.save("mnist.h5")

scores = model.evaluate(x_test, y_test, verbose=1)
print('Test loss:', scores[0])
print('Test accuracy:', scores[1])




