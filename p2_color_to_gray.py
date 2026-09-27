"""
Problem 2: Convert a color image to grayscale; show side by side.
Usage: python p2_color_to_gray.py <image_path>
"""
import sys
import cv2
import matplotlib.pyplot as plt

def main(path):
    color = cv2.imread(path, cv2.IMREAD_COLOR)
    if color is None:
        print(f"Could not read {path}")
        return
    gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)

    size_color = color.nbytes
    size_gray = gray.nbytes
    print(f"Color image     : shape={color.shape}, channels=3, size={size_color} bytes")
    print(f"Grayscale image : shape={gray.shape},  channels=1, size={size_gray} bytes")
    print(f"Channel change  : 3 -> 1")
    print(f"Bytes saved     : {size_color - size_gray}")

    plt.figure(figsize=(8, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(color, cv2.COLOR_BGR2RGB))
    plt.title("Original (Color)")
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.imshow(gray, cmap='gray')
    plt.title("Grayscale")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python p2_color_to_gray.py <image_path>")
    else:
        main(sys.argv[1])
