import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ctwavelet",
    version="1.0.5",
    author="Burak Tahtacı",
    author_email="buraktahtaci@crypttech.com",
    description="A wavelet transform library based on Haar Lifting Scheme",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://crypttech.com/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
