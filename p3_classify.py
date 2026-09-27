"""
Problem 3: Classify an unknown image as binary, grayscale or color.
Usage: python p3_classify.py <image_path>
"""
import sys
import cv2
import numpy as np

def main(path):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    if img is None:
        print(f"Could not read {path}")
        return

    if img.ndim == 2:
        channels = 1
        uniq = np.unique(img)
        if len(uniq) <= 2:
            kind = "binary image"
            reason = f"single channel with {len(uniq)} unique pixel values"
        else:
            kind = "grayscale image"
            reason = f"single channel with {len(uniq)} unique intensity values"
    else:
        channels = img.shape[2]
        if channels == 1:
            kind = "grayscale image"
            reason = "1-channel image"
        elif channels == 3:
            kind = "color (BGR/RGB) image"
            reason = "3-channel image"
        elif channels == 4:
            kind = "color (BGRA/RGBA) image"
            reason = "4-channel image (with alpha)"
        else:
            kind = "multi-channel image"
            reason = f"{channels}-channel image"

    print(f"Image: {path}")
    print(f"Detected type : {kind}")
    print(f"Reasoning     : {reason}")
    print(f"Channels      : {channels}")
    print(f"Shape         : {img.shape}, dtype={img.dtype}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python p3_classify.py <image_path>")
    else:
        main(sys.argv[1])
