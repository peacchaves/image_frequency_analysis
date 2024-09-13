# Image Frequency Analysis

This package performs Fourier Transform on images and compares the resulting frequencies.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package_name

```bash
pip install image_frequency_analysis
```

## Usage

```python

from image_frequency_analysis import compute_fourier_transform, plot_frequency_comparison

# Paths to the images
image_paths = ['image1.jpg', 'image2.jpg']

# Compute the Fourier Transform
frequencies = compute_fourier_transform(image_paths)

# Plot the frequency comparison
plot_frequency_comparison(frequencies)

```

## Author
Pedro Augusto Costa Chaves

## License
MIT License

Copyright (c) 2024 Pedro Augusto Costa Chaves

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
