# Digital Image Processing 

## Requirements

```bash
pip install opencv-python numpy matplotlib
```

## Files

| # | Script | What it does |
|---|--------|--------------|
| 1 | [p1_inspect.py](p1_inspect.py) | Read image, print width / height / channels / data type |
| 2 | [p2_color_to_gray.py](p2_color_to_gray.py) | Convert color image to grayscale, show side by side |
| 3 | [p3_classify.py](p3_classify.py) | Auto-classify image as binary / grayscale / color |
| 4 | [p4_modalities.py](p4_modalities.py) | Display 5 imaging-modality samples (X-ray, satellite, microscopy, ultrasound, IR) |
| 5 | [p5_threshold.py](p5_threshold.py) | Threshold a grayscale image at T = 80, 128, 200 |
| 6 | [p6_spatial_resolution.py](p6_spatial_resolution.py) | Resample to 128×128, 64×64, 32×32, 16×16 → checkerboard effect |
| 7 | [p7_intensity_resolution.py](p7_intensity_resolution.py) | Quantize gray levels from 256 down to 2 → false contouring |
| 8 | [p8_interpolation.py](p8_interpolation.py) | 4× upscale with nearest-neighbor / bilinear / bicubic |
| 9 | [p9_histogram.py](p9_histogram.py) | Histogram of dark / bright / low-contrast images |
| 10 | [p10_neighbors.py](p10_neighbors.py) | N4, ND, N8 of a pixel (middle, edge, corner) |
| 11 | [p11_distances.py](p11_distances.py) | Euclidean, D4, D8 distances between two pixels |
| 12 | [p12_arithmetic.py](p12_arithmetic.py) | Image add / sub / mul / div + change detection |
| 13 | [p13_averaging.py](p13_averaging.py) | Average 20 noisy copies → noise reduction |
| 14 | [p14_logic.py](p14_logic.py) | AND / OR / NOT / XOR on binary shapes |
| 15 | [p15_transforms.py](p15_transforms.py) | Translation, rotation, scaling |

## Usage

Most scripts take an image path as an argument:

```bash
python p1_inspect.py photo.jpg
python p2_color_to_gray.py photo.jpg
python p5_threshold.py lena.png
```

A few scripts have sample lists at the top of the file — edit the paths and re-run:

- **p4_modalities.py** — `IMAGES = [(path, modality, application), ...]`
- **p9_histogram.py** — `SAMPLES = [(path, label), ...]`

Scripts with multiple inputs:

```bash
python p12_arithmetic.py image1.jpg image2.jpg
```

Scripts that need no inputs:

```bash
python p11_distances.py
python p14_logic.py
```

## Notes

- All scripts use `cv2.imread(..., IMREAD_UNCHANGED)` so the original bit-depth and channel count are preserved.
- Grayscale display uses `cmap='gray'`.
- Color display converts BGR → RGB for accurate rendering in Matplotlib.
- Sample image paths are placeholders — supply your own files (`.jpg`, `.png`, `.bmp`, ...).

## Credits - Test Images

The images used for testing the scripts in this repo (e.g. `images/additional/classic/boats.bmp`) are from the Kaggle dataset:

**"Standard Test Images"** by *saeedehkamjoo* —
[https://www.kaggle.com/datasets/saeedehkamjoo/standard-test-images](https://www.kaggle.com/datasets/saeedehkamjoo/standard-test-images)

This collection is itself a redistribution of the classic grayscale / color test images widely used in image-processing textbooks and benchmarks (Lena, Cameraman, Peppers, Boats, etc.).
