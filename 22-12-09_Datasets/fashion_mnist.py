import cv2
import numpy as np
import torch
import os
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt

training_data = datasets.FashionMNIST(
    root = 'data',
    train = True,
    download=True,
    transform=ToTensor()
)

test_data = datasets.FashionMNIST(
    root='data',
    train=False,
    download=True,
    transform=ToTensor()
)

img_size = 28
num_images = 5
with open('./data/FashionMnist/raw/t10k-images-idx3-ubyte', 'rb') as f:
    a = f.read(16)
    buf = f.read(img_size*img_size*num_images)
    data = np.frombuffer(buf, dtype=np.uint8).astype(float)
    data = data.reshape(num_images, img_size, img_size, 1)
    import matplotlib.pyplot as plt
    image = np.asarray(data[1]).squeeze()
    plt.imshow(image)
    plt.show()

with open('./data/FashionMnist/raw/train-labels-idx1-ubyte', 'rb') as f:
    buf = f.read(num_images)
    labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
    print(labels[1])

labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}

figure = plt.figure(figsize=(8,8))
cols, rows = 3,3
for i in range(1, cols*rows +1):
    sample_idx = torch.randint(len(training_data), size=(1,)).item()
    img, label = training_data[sample_idx]
    figure.add_subplot(rows, cols, i)
    plt.title(labels_map[label])
    plt.axis('off')
    plt.imshow(img.squeeze(), cmap='gray')
plt.show()

imgf = open('./data/FashionMnist/raw/train-images-idx3-ubyte', 'rb')
imgd = imgf.read(16)
lblf = open('./data/FashionMNIST/raw/train-labels-idx1-ubyte', 'rb')
lbld = lblf.read(8)
df_dict = {
    'file_name':[],
    'label':[]
}
idx = 0
os.makedirs('./data/FashionMNIST/imgs', exist_ok=True)
while True:
    imgd = imgf.read(img_size*img_size)
    if not imgd:
        break
    data = np.frombuffer(imgd, dtype=np.uint8).astype(float)
    data = data.reshape(1, img_size, img_size, 1)
    image = np.asarray(data).squeeze()
    lbld = lblf.read(1)
    labels = np.frombuffer(lbld, dtype=np.uint8).astype(np.int64)
    file_name = f'{idx}.png'
    cv2.imwrite(f'./data/FashionMNIST/imgs/{file_name}', image)
    idx += 1
    df_dict['label'].append(labels[0])
    df_dict['file_name'].append(file_name)
import pandas as pd
df = pd.DataFrame(df_dict)
print(df)
df.to_csv('./data/FashionMNIST/annotations.csv')