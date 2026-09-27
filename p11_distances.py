"""
Problem 11: Euclidean, D4 (city-block), D8 (chessboard) distances.
"""
import numpy as np

# Test cases with manually verifiable values
TESTS = [
    ((0, 0), (3, 4)),   # Euclidean = 5, D4 = 7, D8 = 4
    ((1, 1), (1, 5)),   # Euclidean = 4, D4 = 4, D8 = 4 (same column)
    ((2, 2), (6, 5)),   # Euclidean ~ 5, D4 = 7, D8 = 4
]

def distance(p1, p2):
    p1 = np.array(p1, dtype=float)
    p2 = np.array(p2, dtype=float)
    de = np.linalg.norm(p1 - p2)
    d4 = np.sum(np.abs(p1 - p2))
    d8 = np.max(np.abs(p1 - p2))
    return de, d4, d8

def main():
    for p1, p2 in TESTS:
        de, d4, d8 = distance(p1, p2)
        print(f"{p1} <-> {p2}: Euclidean={de:.2f}, D4={d4}, D8={d8}")

if __name__ == "__main__":
    main()
