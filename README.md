# CT Wavelet Transform Library
[![Build Status](https://travis-ci.org/tahtaciburak/ctwavelet.svg?branch=master)](https://travis-ci.org/tahtaciburak/ctwavelet)  

A utility library for generating wavelet coefficients by using Haar Lifting Scheme.

## Installation
From PyPi:
```
pip install ctwavelet
```
From Source Code:
```
git clone https://github.com/tahtaciburak/ctwavelet
cd ctwavelet
pip install .
```

## Usage:
```python
from ctwavelet import LiftingScheme
ls = LiftingScheme.LiftingScheme()
ls.apply([0,1,2,3,4,5,6,7])

coeffs = ls.get_wavelet_coeffs()
print(coeffs)

inverse_coeffs = ls.inverse(coeffs)
print(inverse_coeffs)
```
