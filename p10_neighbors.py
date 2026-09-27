"""
Problem 10: 4-, 8-, and diagonal neighbors of a pixel.
Usage: python p10_neighbors.py <image_path>
"""
import sys
import cv2

def neighbors(img, x, y):
    h, w = img.shape[:2]
    n4, nd = [], []
    for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < h and 0 <= nx < w:
            n4.append((nx, ny))
    for dy, dx in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < h and 0 <= nx < w:
            nd.append((nx, ny))
    n8 = n4 + [p for p in nd if p not in n4]
    return n4, nd, n8

def main(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    if img is None:
        print(f"Could not read {path}")
        return
    h, w = img.shape[:2]

    tests = {
        "Middle": (w // 2, h // 2),
        "Edge":   (w // 2, 0),
        "Corner": (0, 0),
    }
    for name, (x, y) in tests.items():
        n4, nd, n8 = neighbors(img, x, y)
        print(f"{name:7s} ({x:3d},{y:3d}) -> N4={n4}, ND={nd}, N8={n8}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python p10_neighbors.py <image_path>")
    else:
        main(sys.argv[1])
