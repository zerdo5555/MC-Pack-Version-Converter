"""
Setup script for MC-Pack Version Converter
"""

from setuptools import setup, find_packages
import os

# Read README for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="minecraft-pack-updater",
    version="1.0.0",
    author="MC-Pack Version Converter Team",
    author_email="your-email@example.com",
    description="A GUI tool for updating Minecraft resource packs and mods between versions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/YOUR_USERNAME/minecraft-pack-updater",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: X11 Applications :: Qt",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pyinstaller>=4.10",
            "pytest>=6.0.0",
            "black>=21.0.0",
            "flake8>=3.9.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "minecraft-pack-updater=minecraft_pack_updater:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.png", "*.jpg", "*.ico"],
    },
    keywords="minecraft, resource-pack, mod, converter, gui, version-update",
    project_urls={
        "Bug Reports": "https://github.com/YOUR_USERNAME/minecraft-pack-updater/issues",
        "Source": "https://github.com/YOUR_USERNAME/minecraft-pack-updater",
        "Documentation": "https://github.com/YOUR_USERNAME/minecraft-pack-updater/wiki",
    },
)
