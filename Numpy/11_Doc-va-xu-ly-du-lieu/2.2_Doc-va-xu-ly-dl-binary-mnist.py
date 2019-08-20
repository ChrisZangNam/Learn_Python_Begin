#xu ly du lieu mnist

import os
import gzip
import numpy as np
import matplotlib.pyplot as plt

def load_fashion_mnist(path, kind='train'):
    #Load fashion_MNIST data from 'path'
    labels_path = os.path.join(path, "%s-labels-idx1-ubyte.gz" % kind)
    images_path = os.path.join(path, "%s-images-idx3-ubyte.gz" % kind)

    with gzip.open(labels_path, 'rb') as lbpath:
        labels = np.frombuffer(lbpath.read(), dtype=np.uint8, offset=8)
        #Bo qua 8 byte dau file mo ta thong tin ve file.

    with gzip.open(images_path, 'rb') as imgpath:
        images = np.frombuffer(imgpath.read(), dtype=np.uint8, offset=16).reshape(len(labels), 784)
        #Bo qua 16 byte dau khi doc file cho tap training.
        #du lieu duoc luu duoi dang vecto cho do dai 784 thay do dang matrix 2D 28x28


    return images, labels

X_train, y_train = load_fashion_mnist('data_fashion_mnist/')
print(X_train.shape)
print(y_train.shape)

#Kiem tra ngau nhien cac mau trainning trong tong so 60000 mau

#Tao danh sach 100 phan tu ngau nhien tu X_train co 6000 phan tu
indices = list(np.random.randint(X_train.shape[0], size=100))

fig = plt.figure(figsize=(9,9))
columns = 10
rows = 10
for i in range(1, columns*rows + 1):
    img = X_train[indices[i-1]].reshape(28,28)
    fig.add_subplot(rows, columns, i)
    plt.axis('off')
    plt.imshow(img, cmap='gray', vmin=0, vmax=255)

plt.show()
