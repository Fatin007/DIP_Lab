"""
Problem 5: Threshold a grayscale image into binary at a given threshold.
Usage: python p5_threshold.py <image_path>
"""
import sys
import cv2
import matplotlib.pyplot as plt

THRESHOLDS = [80, 128, 200]

def main(path):
    gray = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if gray is None:
        print(f"Could not read {path}")
        return

    plt.figure(figsize=(12, 3))
    n = len(THRESHOLDS)
    plt.subplot(1, n + 1, 1)
    plt.imshow(gray, cmap='gray')
    plt.title("Original")
    plt.axis('off')

    for i, t in enumerate(THRESHOLDS, 2):
        _, binary = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)
        plt.subplot(1, n + 1, i)
        plt.imshow(binary, cmap='gray')
        plt.title(f"T={t}")
        plt.axis('off')

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python p5_threshold.py <image_path>")
    else:
        main(sys.argv[1])
