"""
Problem 1: Reading, Displaying, and Inspecting a Digital Image
Usage: python p1_inspect.py <image_path>
"""
import sys
import cv2
import matplotlib.pyplot as plt

def main(path):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if img is None:
        print(f"Could not read {path}")
        return
    h, w = img.shape[:2]
    channels = img.shape[2] if img.ndim == 3 else 1
    dtype = img.dtype
    size_bytes = img.nbytes

    print(f"Image         : {path}")
    print(f"Width x Height: {w} x {h}")
    print(f"Channels      : {channels}")
    print(f"Data type     : {dtype}")
    print(f"Size (bytes)  : {size_bytes}")

    if channels == 3:
        show = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cmap = None
    else:
        show = img
        cmap = 'gray'

    plt.imshow(show, cmap=cmap)
    plt.title("Loaded Image")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python p1_inspect.py <image_path>")
    else:
        main(sys.argv[1])
