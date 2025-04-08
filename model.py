import torch
from torch import nn

class AiModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.layer1 = nn.Linear(in_features=10, out_features=16)
        self.layer2 = nn.Linear(in_features=16, out_features=16)
        self.layer3 = nn.Linear(in_features=16, out_features=4)

    def forward(self, x:torch.Tensor) -> torch.Tensor:
        x = nn.ReLU(self.layer1(x))
        x = nn.ReLU(self.layer2(x))
        return self.layer3(x)

