#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="src",
    version="0.0.1",
    description="Describe Your Cool Project",
    author="",
    author_email="",
    url="https://github.com/user/project",
    python_requires=">=3.10",
    install_requires=[
        "torch==2.7.1+cu128",
        "torchvision==0.22.0+cu128",
        "lightning>=2.4.0",
        "torchmetrics>=1.3.1",
        "hydra-core>=1.3",
    ],
    packages=find_packages(),
    # use this to customize global commands available in the terminal after installing the package
    entry_points={
        "console_scripts": [
            "train_command = src.train:main",
            "eval_command = src.eval:main",
        ]
    },
)
