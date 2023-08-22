import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def adjust_grey_level_resolution(image, levels):

    max_value = image.max()
    min_value = image.min()
    normalized_image = (image - min_value) / (max_value - min_value)
    

    quantized_image = (normalized_image * (levels-1)).astype(np.int)
    adjusted_image = quantized_image / (levels-1)
    
    return adjusted_image


image_path = 'tenten.jpeg'
image = mpimg.imread(image_path)


if len(image.shape) == 3 and image.shape[2] > 1:
    image = np.mean(image, axis=-1)


fig, axs = plt.subplots(1, 11, figsize=(15, 5))


axs[10].imshow(image, cmap='gray')
axs[10].set_title("Original")
axs[10].axis('off')

for i in range(10, 1, -1): 
    adjusted_image = adjust_grey_level_resolution(image, i)
    axs[10-i].imshow(adjusted_image, cmap='gray')
    axs[10-i].set_title(f"{i} Levels")
    axs[10-i].axis('off')

plt.tight_layout()
plt.show()
