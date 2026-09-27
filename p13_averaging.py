"""
Problem 13: Noise reduction by averaging N noisy copies.
Usage: python p13_averaging.py <image_path>
"""
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

N = 20       # number of noisy copies
SIGMA = 25   # Gaussian noise std-dev

def main(path):
    clean = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if clean is None:
        print(f"Could not read {path}"); return
    clean = clean.astype(np.float32)

    rng = np.random.default_rng(42)
    noisy = clean + rng.normal(0, SIGMA, clean.shape).astype(np.float32)
    avg = np.zeros_like(clean)
    for _ in range(N):
        avg += clean + rng.normal(0, SIGMA, clean.shape).astype(np.float32)
    avg /= N

    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(np.clip(noisy, 0, 255).astype(np.uint8), cmap='gray')
    plt.title("One Noisy Copy"); plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(np.clip(avg, 0, 255).astype(np.uint8), cmap='gray')
    plt.title(f"Average of {N}"); plt.axis('off')
    plt.tight_layout(); plt.show()

    print(f"Averaging N independent zero-mean noise samples reduces noise std "
          f"by sqrt(N) (~ factor {N**0.5:.2f}). Random fluctuations cancel; "
          f"the underlying signal is reinforced.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python p13_averaging.py <image_path>")
    else:
        main(sys.argv[1])
