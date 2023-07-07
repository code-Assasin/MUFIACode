"""
This file contains the default configuration values for the project.
The values defined here are used throughout the project. Please change the directory paths to your own.
"""

# directory where the filter banks generated by mufia are saved
directory_names = dict(save_dir="/SCRATCH2/machiraj/quantize_mats/")

# directory where the respective datasets are saved
dataset_paths = dict(
    cifar10="/SCRATCH2/machiraj/datasets/cifar10/",
    cifar100="/SCRATCH2/machiraj/datasets/cifar100/",
    imagenet_val="/datasets2/ImageNet2012/val/",
    imagenet_train="/datasets2/ImageNet2012/train/",
)

# directory where the respective models corresponding to the datasets are saved
model_paths = dict(
    cifar10="/SCRATCH2/machiraj/robust_models/CIFAR10/",
    cifar100="/SCRATCH2/machiraj/robust_models/CIFAR100/",
    imagenet="/SCRATCH2/machiraj/robust_models/IMAGENET/",
)

# configuration for wandb, please change the entity and project name to your own to log the results
wandb_config = dict(entity="harshitha-machiraju", project="mufia", reinit=True,)
