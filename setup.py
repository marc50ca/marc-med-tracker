"""Setup configuration for Marc Med Tracker."""

from pathlib import Path
from setuptools import setup, find_packages

# Read the long description from README
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="marc-med-tracker",
    version="2.0.0",
    description="Home Assistant integration for comprehensive medication tracking",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Marc Med Tracker Contributors",
    url="https://github.com/yourusername/marc-med-tracker",
    license="MIT",
    packages=find_packages(exclude=["tests", "docs", "examples"]),
    python_requires=">=3.11",
    install_requires=[
        "homeassistant>=2024.1.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Home Automation",
    ],
    keywords="homeassistant medication tracking health",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/marc-med-tracker/issues",
        "Documentation": "https://github.com/yourusername/marc-med-tracker/tree/main/docs",
        "Source": "https://github.com/yourusername/marc-med-tracker",
    },
)
