import numpy as np
from scipy.fft import fft2, fftshift
from skimage import io, color

def compute_fourier_transform(image_paths):
    transforms = {}
    for path in image_paths:
        image = io.imread(path)
        if image.ndim == 3:
            image = color.rgb2gray(image)
        f_transform = fft2(image)
        f_transform_shifted = fftshift(f_transform)
        magnitude_spectrum = np.abs(f_transform_shifted)
        transforms[path] = magnitude_spectrum
    return transforms