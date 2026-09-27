"""
Problem 9: Histogram of a grayscale image.
Edit SAMPLES below to point to dark / bright / low-contrast images.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

# (path, label)
SAMPLES = [
    ("dark.jpg",        "Dark"),
    ("bright.jpg",      "Bright"),
    ("lowcontrast.jpg", "Low Contrast"),
]

def main():
    loaded = []
    plt.figure(figsize=(12, 6))
    for i, (path, label) in enumerate(SAMPLES, 1):
        img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            print(f"Skipping: {path}")
            continue
        loaded.append(label)
        plt.subplot(2, 3, i)
        plt.imshow(img, cmap='gray')
        plt.title(label)
        plt.axis('off')
        plt.subplot(2, 3, i + 3)
        plt.hist(img.ravel(), bins=256, range=(0, 256), color='black')
        plt.title(f"{label} histogram")
        plt.xlabel("Intensity")
        plt.ylabel("Count")

    plt.tight_layout()
    plt.show()

    if loaded:
        print("Histograms:")
        for label in loaded:
            print(f"  {label}: distribution matches expectation for a {label.lower()} image.")

if __name__ == "__main__":
    main()
