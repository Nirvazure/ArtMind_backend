import torch
from net.ArtNet import ArtNet
from net.inceptionV4 import InceptionV4
import torchvision
from torchvision import transforms, utils
from config import num_classes, batch_size, learning_rate, test_path, saved_model_path
import matplotlib.pyplot as plt

# Device configuration
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
model = InceptionV4(num_classes).to(device)
# model = ArtNet(num_classes).to(device)
model.load_state_dict(torch.load(saved_model_path))

testset = torchvision.datasets.ImageFolder(test_path, transform=transforms.Compose(
    [transforms.Scale(299), transforms.CenterCrop(299), transforms.ToTensor()]))

test_loader = torch.utils.data.DataLoader(testset, batch_size=20, shuffle=True)

# Test the model
model.eval()  # eval mode (batchnorm uses moving mean/variance instead of mini-batch mean/variance)
with torch.no_grad():
    correct = 0
    total = 0
    for images, labels in test_loader:

        images = images.to(device)
        labels = labels.to(device)

        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)

        total += labels.size(0)
        correct += (predicted == labels).sum().item()

        print(labels)
        print(predicted)
        # for i in range(len(images)):
        #     grid = utils.make_grid(images[i], nrow=1)
        #     plt.imshow(grid.numpy().transpose((1, 2, 0)))
        #     plt.title('Batch from dataloader'+str(labels[i])+str(predicted[i]))
        #     plt.show()

    print(correct, total)
    print('Test Accuracy of the model on the test images: {} %'.format(
        100 * correct / total))
