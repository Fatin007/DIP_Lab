"""
Problem 7: False contouring - reduce intensity resolution.
Usage: python p7_intensity_resolution.py <image_path>
"""
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

LEVELS = [128, 64, 32, 16, 8, 4, 2]

def main(path):
    gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if gray is None:
        print(f"Could not read {path}")
        return

    plt.figure(figsize=(16, 3))
    n = len(LEVELS)
    plt.subplot(1, n + 1, 1)
    plt.imshow(gray, cmap='gray')
    plt.title("256 levels")
    plt.axis('off')

    for i, L in enumerate(LEVELS, 2):
        step = 256 // L
        quant = (gray // step) * step
        plt.subplot(1, n + 1, i)
        plt.imshow(quant, cmap='gray')
        plt.title(f"{L} levels")
        plt.axis('off')

    plt.tight_layout()
    plt.show()
    print("When the number of gray levels drops, smooth gradients break into visible bands. "
          "This 'false contouring' is most obvious in smoothly shaded regions like sky or skin.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python p7_intensity_resolution.py <image_path>")
    else:
        main(sys.argv[1])
