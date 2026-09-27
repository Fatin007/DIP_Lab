"""
Problem 8: Compare nearest-neighbor, bilinear, bicubic interpolation.
Usage: python p8_interpolation.py <image_path>
"""
import sys
import cv2
import matplotlib.pyplot as plt

SCALE = 4

def main(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Could not read {path}")
        return
    if img.shape[0] > 64 or img.shape[1] > 64:
        img = cv2.resize(img, (64, 64))
    new_size = (img.shape[1] * SCALE, img.shape[0] * SCALE)

    nn = cv2.resize(img, new_size, interpolation=cv2.INTER_NEAREST)
    bl = cv2.resize(img, new_size, interpolation=cv2.INTER_LINEAR)
    bc = cv2.resize(img, new_size, interpolation=cv2.INTER_CUBIC)

    plt.figure(figsize=(12, 4))
    plt.subplot(1, 3, 1); plt.imshow(nn, cmap='gray'); plt.title("Nearest-Neighbor"); plt.axis('off')
    plt.subplot(1, 3, 2); plt.imshow(bl, cmap='gray'); plt.title("Bilinear");        plt.axis('off')
    plt.subplot(1, 3, 3); plt.imshow(bc, cmap='gray'); plt.title("Bicubic");         plt.axis('off')
    plt.tight_layout()
    plt.show()
    print("Nearest-neighbor is blocky, bilinear is smoother but a bit blurry, "
          "bicubic is the smoothest with the least visible blockiness.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python p8_interpolation.py <image_path>")
    else:
        main(sys.argv[1])
