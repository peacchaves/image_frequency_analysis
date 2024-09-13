import matplotlib.pyplot as plt
import numpy as np

def plot_frequency_comparison(frequency_dict):
    num_images = len(frequency_dict)
    fig, axes = plt.subplots(1, num_images, figsize=(15, 5))
    if num_images == 1:
        axes = [axes]
    
    for ax, (path, magnitude_spectrum) in zip(axes, frequency_dict.items()):
        ax.imshow(np.log(1 + magnitude_spectrum), cmap='gray')
        ax.set_title(f'Imagem: {path}')
        ax.axis('off')

    plt.tight_layout()
    plt.show()
