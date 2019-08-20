import numpy as np
import os
from random import shuffle
from tqdm import  tqdm
from PIL import Image

TRAIN_DIR = 'dogs-vs-cats/train'
TEST_DIR  = 'dogs-vs-cats/test'
IMG_SIZE  = 50

def label_img(img):
    word_label = img.split('.')[0]
    if word_label == 'cat':
        return 0
    elif word_label == 'dog':
        return 1

def create_train_data():
    X_list = []
    y_list = []

    #module tqdm sd de hien thi tien trinh hoan thanh chuong trinh.
    #label cho cat la ), dog la 1.
    for img in tqdm(os.listdir(TRAIN_DIR)):
        label = label_img(img)
        path = os.path.join(TRAIN_DIR, img)

        img = Image.open(path)
        img = img.resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS)
        img = np.asanyarray(img)

        X_list.append(img)
        y_list.append(label)

    X = np.array(X_list)
    y = np.array(y_list)

    #np.save() de luu lai tap training khi da xu ly xong
    np.save('dogs-vs-cats/X.npy', X)
    np.save('dogs-vs-cats/y.npy', y)

    return X, y

X, y = create_train_data()
print(X.shape)
print(y.shape)


#De kiem tra viec xu ly du lieu, chung ta luu vai anh tu ta; file X.npy:
indices = list(np.random.randint(25000, size=10))
X = np.load('dogs-vs-cats/X.npy')

for i in range(10):
    im = Image.fromarray(X[indices[i]].reshape(50, 50, 3))
    im.save("cats_dogs/image_" + str(i) + ".jpg")


