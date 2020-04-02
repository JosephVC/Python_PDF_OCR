import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="JosephVC",
    version="0.0.1",
    author="Joseph Cardenas",
    author_email="josephvcardenas@gmail.com",
    description="A simple OCR project built using Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JosephVC/OCR_project",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)