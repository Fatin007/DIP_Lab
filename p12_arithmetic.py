"""
Problem 12: Image arithmetic (add, sub, mul, div) and change detection.
Usage: python p12_arithmetic.py <image1_path> <image2_path>
"""
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

def main(p1, p2):
    a = cv2.imread(p1, cv2.IMREAD_GRAYSCALE).astype(np.float32)
    b = cv2.imread(p2, cv2.IMREAD_GRAYSCALE).astype(np.float32)
    if a is None or b is None:
        print("Could not read input images."); return
    if a.shape != b.shape:
        b = cv2.resize(b, (a.shape[1], a.shape[0]))

    add = np.clip(a + b, 0, 255)
    sub = np.clip(a - b, 0, 255)
    mul = np.clip((a * b) / 255.0, 0, 255)
    div = np.clip((a / (b + 1)) * 255, 0, 255)
    diff = np.abs(a - b).astype(np.uint8)
    _, diff_bin = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    plt.figure(figsize=(12, 8))
    panels = [(a.astype(np.uint8), "A"),
              (b.astype(np.uint8), "B"),
              (add.astype(np.uint8), "Add"),
              (sub.astype(np.uint8), "Sub"),
              (mul.astype(np.uint8), "Mul"),
              (div.astype(np.uint8), "Div"),
              (diff_bin, "Difference (binary)")]
    for i, (im, t) in enumerate(panels, 1):
        plt.subplot(3, 3, i)
        plt.imshow(im, cmap='gray')
        plt.title(t); plt.axis('off')
    plt.tight_layout(); plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python p12_arithmetic.py <image1> <image2>")
    else:
        main(sys.argv[1], sys.argv[2])
