import cv2
import numpy as np
import torch
import os
from torchvision import datasets, transforms
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
from torchvision.io import read_image
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import pandas as pd


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
    #plt.imshow(image)
    #plt.show()

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
#plt.show()

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


df = pd.DataFrame(df_dict)
#print(df)
df.to_csv('./data/FashionMNIST/annotations.csv')

class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file, names=['file_name', 'label'], skiprows=[0])
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx,0])
        try:
            image = read_image(img_path)
        except:
            print(self.img_labels.iloc[idx, 0])
            exit()
        label = int(self.img_labels.iloc[idx,1]) # sting?????? ??????.
        if self.transform:
            image = self.tranform(image) # totensor??????
        if self.target_transform:
            label = self.target_transform(label)
        return image, label

class Net(nn.Module):
    def __int__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(784, 512)
        self.fc2 = nn.Linear(512, 256)
        self.fc3 = nn.Linear(256, 128)
        self.fc4 = nn.Linear(128, 64)
        self.fc5 = nn.Linear(64, 32)
        self.fc6 = nn.Linear(32, 10)

    def forward(self, x):
        x = x.float()
        h1 = F.relu(self.fc1(x.view(-1, 784)))
        h2 = F.relu(self.fc2(h1))
        h3 = F.relu(self.fc3(h2))
        h4 = F.relu(self.fc4(h3))
        h5 = F.relu(self.fc5(h4))
        h6 = self.fc6(h5)
        return F.log_softmax(h6, dim=1)

transform = transforms.Compose([
                 transforms.ToTensor(),
                 transforms.Normalize((0.1307,), (0.3081,))])

print("init model done")

epochs = 10 # ????????? 10??? ??????.
lr = 0.01
momentum = 0.5 # ????????? ??? ????????? ???????????? ?????? ????????????. optimizer??? ?????????.
no_cuda = True
seed = 1
log_interval = 200

use_cuda = not no_cuda and torch.cuda.is_available()
torch.manual_seed(seed)
device = torch.device('cuda' if use_cuda else 'cpu')
kwargs = {'num_workers':1, 'pin_memory':True} if use_cuda else{}
print('set vars and device done')

batch_size = 64
test_batch_size = 1000
dataset = CustomImageDataset(
    annotations_file='./data/FashionMNIST/annotations.csv',
    img_dir = './data/FashionMNIST/imgs'
)

train_loader = torch.utils.data.DataLoader(dataset, batch_size=64, shuffle=True )
test_loader =  torch.utils.data.DataLoader(dataset, batch_size=test_batch_size, shuffle=True, **kwargs)

model = Net().to(device)
optimizer = optim.SGD(model.parameters(), lr=lr, momentum=momentum)

def train(log_interval, model, device, train_loader, optimizer, epoch):
    model.train()
    for batch_idx, (data, target), in enumerate(train_loader):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad() #
        output = model(data)
        loss = F.nll_loss(output, target)
        loss.backward()
        optimizer.step()
        if batch_idx % log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                100. * batch_idx / len(train_loader), loss.item()))
for epch in range(1,11):
    train(log_interval, model, device, train_loader, optimizer, epochs)
torch.save(model, './model.pt')

# def test(log_interval, model, device, test_loader):
#     model.eval()
#     test_loss = 0
#     correct = 0
#     with torch.no_grad():
#         for data, target in test_loader:
#             data, target = data.to(device), target.to(device)
#             output = model(data)
#             test_loss += F.nll_loss(output, target, reduction='sum').item()
#             pred = output.argmax(dim=1, keepdim=True)
#             correct += pred.eq(target.view_as(pred)).sum().item()
#
#     test_loss /= len(test_loader.dataset)
#
#     print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format
#           (test_loss, correct, len(test_loader.dataset),
#         100. * correct / len(test_loader.dataset)))
#
# for epoch in range(1, 11):
#     train(log_interval, model, device, train_loader, optimizer, epoch)
#     test(log_interval, model, device, test_loader)
# torch.save(model, './model.pt')