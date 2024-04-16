from setuptools import setup, find_packages

setup(
    name="sheeet",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    author="Koen van Eijk",
    author_email="koen@magifind.com",
    description="Sheeet client",
    url="https://github.com/magifind/sheeet",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
