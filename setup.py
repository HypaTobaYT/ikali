from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ikali",
    version="1.0.0",
    author="hyper",
    author_email="hypertobayt@gmail.com",
    description="This thing is cancer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HypaTobaYT/ikali",
    py_modules=["ikali"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "ikali=ikali:main",
        ],
    },
)
