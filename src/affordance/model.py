import torch.nn as nn


class AffordancePredictor(nn.Module):
    def __init__(self, in_channels=6, hidden=128):
        super().__init__()
        self.backbone = nn.Sequential(
            nn.Conv2d(in_channels, hidden, 3, padding=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(hidden, hidden, 3, padding=1),
        )
        self.score = nn.Conv2d(hidden, 1, 1)

    def forward(self, rgbd):
        return self.score(self.backbone(rgbd))
