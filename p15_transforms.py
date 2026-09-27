"""
Problem 15: Translation, rotation, scaling.
Usage: python p15_transforms.py <image_path>
"""
import sys
import cv2
import matplotlib.pyplot as plt

TX, TY = 50, 30      # translation pixels
ANGLE = 45           # degrees, about image center
SCALE = 0.6          # scaling factor

def main(path):
    img = cv2.imread(path, cv2.IMREAD_COLOR)
    if img is None:
        print(f"Could not read {path}"); return
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w = img.shape[:2]

    # (a) translation
    T = np.float32([[1, 0, TX], [0, 1, TY]])
    translated = cv2.warpAffine(img, T, (w, h))

    # (b) rotation about center
    M = cv2.getRotationMatrix2D((w // 2, h // 2), ANGLE, 1.0)
    rotated = cv2.warpAffine(img, M, (w, h))

    # (c) scaling
    new_size = (int(w * SCALE), int(h * SCALE))
    scaled = cv2.resize(img, new_size, interpolation=cv2.INTER_AREA)
    canvas = np.zeros_like(img)
    canvas[:scaled.shape[0], :scaled.shape[1]] = scaled

    plt.figure(figsize=(12, 10))
    plt.subplot(2, 2, 1); plt.imshow(img);        plt.title("Original");          plt.axis('off')
    plt.subplot(2, 2, 2); plt.imshow(translated); plt.title(f"Translate ({TX},{TY})"); plt.axis('off')
    plt.subplot(2, 2, 3); plt.imshow(rotated);    plt.title(f"Rotate {ANGLE} deg"); plt.axis('off')
    plt.subplot(2, 2, 4); plt.imshow(canvas);     plt.title(f"Scale x{SCALE}");    plt.axis('off')
    plt.tight_layout(); plt.show()

    print("Empty (black) regions appear where the transformation pushes pixels "
          "outside the original frame, or where the scaling factor shrinks the content.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python p15_transforms.py <image_path>")
    else:
        main(sys.argv[1])
