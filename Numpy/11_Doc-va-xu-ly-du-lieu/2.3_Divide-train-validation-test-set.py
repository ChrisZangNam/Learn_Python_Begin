#Divide data in to Training set, Validation set and Test set

import os
import gzip
import numpy as np
from PIL import Image


#Ham load tuong tuong bai 2.2
def load_fashion_mnist(path, kind='train'):
    labels_path = os.path.join(path, '%s-labels-idx1-ubyte.gz' % kind)
    images_path = os.path.join(path, '%s-images-idx3-ubyte.gz' % kind)

    with gzip.open(labels_path, 'rb') as lbpath:
        labels = np.frombuffer(lbpath.read(), dtype=np.uint8, offset=8)
    with gzip.open(images_path, 'rb') as imgpath:
        images = np.frombuffer(imgpath.read(), dtype=np.uint8, offset=16).reshape(len(labels), 784)

    return images, labels

X_train, y_train = load_fashion_mnist('data_fashion_mnist/')
X_test, y_test = load_fashion_mnist('data_fashion_mnist/', kind='t10k')
#Lay so hang cua X_train va X_test
m_train = 50000
m_test  = 10000
m_validation = 10000

#Validation set: Tao list gom 10000 phan tu tu 50000->59999
mask = list(range(m_train, m_train + m_validation))

#Tap con X_val gom 10000 tu X_train
X_val = X_train[mask]

#Lay 10000 nhan tu tap nhan y_train
y_val = y_train[mask]


#Training set: Tao list gom 50000 phan tu tu 0->49999
mask = list(range(m_train))

X_train = X_train[mask]
y_train = y_train[mask]


#Reshape data to row
X_train  = X_train.reshape(m_train, -1)
X_val    = X_val.reshape(m_validation, -1)
X_test   = X_test.reshape(m_test, -1)

print("X_train shape: ", X_train.shape)
print("y_train shape: ", y_train.shape)
print("X_val shape: ", X_val.shape)
print("y_val shape: ", y_val.shape)
print("X_test shape: ", X_test.shape)
print("y_test shape: ", y_test.shape)

#De dam bao du lieu hinh duoc xu li dung. ta se luu vai mau du lieu tu tap training
indices = list(np.random.randint(50000, size=5))
for i in range(5):
    img = Image.fromarray(X_train[indices[i]].reshape(28,28))
    img.save("data_fashion_mnist/image_" + str(i) + ".png")
