"""
Problem 6: Checkerboard effect - reduce spatial resolution.
Usage: python p6_spatial_resolution.py <image_path>
"""
import sys
import cv2
import matplotlib.pyplot as plt

SIZES = [128, 64, 32, 16]

def main(path):
    gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if gray is None:
        print(f"Could not read {path}")
        return

    plt.figure(figsize=(14, 3))
    n = len(SIZES)
    plt.subplot(1, n + 1, 1)
    plt.imshow(gray, cmap='gray')
    plt.title(f"Original\n{gray.shape[1]}x{gray.shape[0]}")
    plt.axis('off')

    for i, s in enumerate(SIZES, 2):
        small = cv2.resize(gray, (s, s), interpolation=cv2.INTER_AREA)
        plt.subplot(1, n + 1, i)
        plt.imshow(small, cmap='gray')
        plt.title(f"{s}x{s}")
        plt.axis('off')

    plt.tight_layout()
    plt.show()
    print("As spatial resolution decreases the pixels grow into visible blocks: "
          "fine details vanish and the image takes on a 'checkerboard' look where each "
          "square is one enlarged pixel.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python p6_spatial_resolution.py <image_path>")
    else:
        main(sys.argv[1])
