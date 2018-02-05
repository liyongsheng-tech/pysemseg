import torch.nn as nn
import torch.nn.functional as F


class SimpleConvNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 10, kernel_size=5, padding=(2, 2))
        self.conv2 = nn.Conv2d(10, 20, kernel_size=5, padding=(2, 2))
        self.conv2_drop = nn.Dropout2d()
        self.fc1 = nn.Conv2d(20, 50, kernel_size=1)
        self.fc2 = nn.Conv2d(50, 1, kernel_size=1)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2_drop(self.conv2(x)))
        x = F.relu(self.fc1(x))
        x = F.dropout(x, training=self.training)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)
