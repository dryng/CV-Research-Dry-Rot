import torch
import torch.nn
import torchvision.models as models

model = models.mobilenet_v3_small(pretrained=True)
num_ftrs = model.classifier[3].in_features
model.classifier[3] = nn.Linear(num_ftrs, 1)


'''
sys.path.append("../../")
from models import mobilenet_v3_small
model = mobilenet_v3_small.model
print(model)
'''
