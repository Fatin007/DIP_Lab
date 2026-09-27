"""
Problem 14: AND / OR / NOT / XOR on two binary shapes.
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

def main(size=(300, 300)):
    a = np.zeros(size, dtype=np.uint8)
    b = np.zeros(size, dtype=np.uint8)
    cv2.circle(a, (120, 150), 80, 255, -1)
    cv2.rectangle(b, (150, 100), (260, 240), 255, -1)

    panels = [
        (a,                    "A (circle)"),
        (b,                    "B (square)"),
        (cv2.bitwise_and(a,b), "AND (intersection)"),
        (cv2.bitwise_or(a,b),  "OR (union)"),
        (cv2.bitwise_not(a),   "NOT (complement A)"),
        (cv2.bitwise_xor(a,b), "XOR (symmetric diff.)"),
    ]
    plt.figure(figsize=(10, 8))
    for i, (im, t) in enumerate(panels, 1):
        plt.subplot(2, 3, i)
        plt.imshow(im, cmap='gray')
        plt.title(t); plt.axis('off')
    plt.tight_layout(); plt.show()

    print("Interpretation:")
    print("  AND   -> only the overlap of circle and square is white (intersection).")
    print("  OR    -> both shapes are white (union).")
    print("  NOT A -> everything except the circle is white (complement).")
    print("  XOR   -> white where exactly one shape is present, not both.")

if __name__ == "__main__":
    main()
