# Requirements

Install the required dependencies by running the following command:
```bash
pip install -r requirements.txt
````
The environment requirements are as follows:

```
torch==1.7.1
torchvision==0.8.2
scipy==1.4.1
numpy==1.19.2
matplotlib==3.2.1
opencv_python==3.4.1.15
tqdm==4.62.3
Pillow==8.4.0
h5py==3.1.0
terminaltables==3.1.0
packaging==21.3
Model File Explanation
```

The model consists of the following components:

backbone: The backbone network for feature extraction.
neck: A component to adjust or combine feature maps.
head: The head of the model that performs the final classification or prediction.
head.loss: The loss function used to train the model.
Each component has a corresponding type, which defines the structure. After the type, you’ll find the necessary parameters to build that structure. These configuration files are already set up.

The type in the configuration is not a parameter used during construction; it is the class name.

# Modifications:
num_classes: This should be adjusted to match the number of classes in your dataset. For example, for a flower dataset with five classes, you would set num_classes=5.
Note: If the number of classes is less than 5, then the top-5 accuracy will default to 100%.
Example model configuration:

```python
model_cfg = dict(
    backbone=dict(
        type='ResNet',          # Type of backbone network
        depth=50,               # Depth of the ResNet backbone (18, 34, 50, 101, 152 are available)
        num_stages=4,           # Number of stages in the backbone (stages are used as inputs for the subsequent head)
        out_indices=(3,),       # Indices of the output feature maps. Larger index means closer to the output.
        frozen_stages=-1,       # The stage of the backbone to freeze during fine-tuning. -1 means no freezing.
        style='pytorch'),       # Backbone style ('pytorch' uses 3x3 convolutions for stride 2, 'caffe' uses 1x1)
    neck=dict(type='GlobalAveragePooling'),  # Type of neck network
    head=dict(
        type='LinearClsHead',     # Linear classification head
        num_classes=1000,         # Number of output classes (matches the number of classes in the dataset)
        in_channels=2048,         # Number of input channels (matches the output channels of the neck)
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0), # Loss function configuration
        topk=(1, 5),              # Evaluation metrics: Top-1 and Top-5 accuracy
    ))
```
# Quick Start
To start training the model, use the following command:
```bash
python tools/train.py models/vision_transformer/vit_base_p16_224.py
```
Arguments:

config: Path to the model configuration file.
--resume-from: Resume training from a checkpoint. Provide the path to the weight file, ensuring you use the correct resume file (e.g., --resume-from logs/SwinTransformer/2022-02-08-08-27-41/Last_Epoch15.pth).
--seed: Set the random seed (defaults to the environment setting).
--device: Specify whether to train on GPU or CPU.
--gpu-id: Specify the GPU device (default is 0, usually for single-GPU training).
--split-validation: Whether to split the training set into a validation set (default ratio is 0.2).
--ratio: Proportion of the training set to use for validation (default 0.2, randomly selected from training data).
--deterministic: Related to multi-GPU training; no need to configure it if not used.

# Model Evaluation
To evaluate the trained model, use the following command:
```bash
python tools/evaluation.py models/vision_transformer/vit_base_p16_224.py
```
