import torch
from torch import nn

class AiModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.Layer1 = nn.Linear(in_features=4, out_features=10)
        nn.ReLU()
        self.Layer2 = nn.Linear(in_features=10, out_features=10)