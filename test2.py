import torch
from net.ArtNet import ArtNet
from config import num_classes, batch_size, learning_rate, test_path, saved_model_path, img_size

# Device configuration
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
# model = InceptionV4(num_classes).to(device)
model = ArtNet(num_classes).to(device)
model.load_state_dict(torch.load(saved_model_path))
