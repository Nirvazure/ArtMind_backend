import torch
import torchvision
from torchvision import transforms, utils
import matplotlib.pyplot as plt
import torch.nn as nn

from net.ArtNet import ArtNet
from net.inceptionV4 import InceptionV4
from config import num_epochs, num_classes, batch_size, learning_rate, train_path, saved_model_path, img_size

# Device configuration
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')


def show_batch(imgs):
    grid = utils.make_grid(imgs, nrow=5)
    plt.imshow(grid.numpy().transpose((1, 2, 0)))
    plt.title('Batch from dataloader')


# InceptionV4为229，Art为160
trainset = torchvision.datasets.ImageFolder(train_path, transform=transforms.Compose(
    [transforms.Scale(img_size), transforms.CenterCrop(img_size), transforms.ToTensor()]))

train_loader = torch.utils.data.DataLoader(
    trainset, batch_size=20, shuffle=True)

# 查看训练数据集样子的代码
for i, (batch_x, batch_y) in enumerate(train_loader):
    print(i, batch_x.size(), batch_y.size())
    # show_batch(batch_x)
    # plt.axis('off')
    # plt.show()

model = ArtNet(num_classes).to(device)
# model = InceptionV4(num_classes).to(device)
# Loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# Train the model
total_step = len(train_loader)
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        images = images.to(device)
        labels = labels.to(device)

        # Forward pass
        outputs = model(images)
        loss = criterion(outputs, labels)

        # Backward and optimize
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        # 之前是100，我改成10步一看
        if (i+1) % 100 == 0:
            print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}'
                  .format(epoch+1, num_epochs, i+1, total_step, loss.item()))

# Save the model checkpoint
torch.save(model.state_dict(), saved_model_path)
