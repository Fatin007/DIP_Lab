"""
Problem 4: Survey of imaging modalities.
Edit IMAGES list below to your 5 sample image paths + modality + application.
"""
import cv2
import matplotlib.pyplot as plt

# Each tuple: (image_path, modality_name, real_world_application)
IMAGES = [
    ("xray.jpg",       "X-ray",        "Medical diagnostics"),
    ("satellite.jpg",  "Satellite",    "Land-cover mapping"),
    ("microscopy.png", "Microscopy",   "Cell biology"),
    ("ultrasound.png", "Ultrasound",   "Prenatal imaging"),
    ("infrared.jpg",   "Infrared",     "Night-vision / thermal imaging"),
]

def main():
    plt.figure(figsize=(15, 6))
    plotted = 0
    for i, (path, modality, app) in enumerate(IMAGES, 1):
        img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
        if img is None:
            print(f"Skipping (missing): {path}")
            continue

        if img.ndim == 2 or (img.ndim == 3 and img.shape[2] == 1):
            show, cmap = img, 'gray'
        else:
            show, cmap = cv2.cvtColor(img, cv2.COLOR_BGR2RGB), None

        plt.subplot(1, 5, i)
        plt.imshow(show, cmap=cmap)
        plt.title(f"{modality}\n{app}", fontsize=9)
        plt.axis('off')
        plotted += 1

    if plotted == 0:
        print("No images loaded. Add real image paths to IMAGES in the script.")
    else:
        plt.tight_layout()
        plt.show()

    print("\nModality applications:")
    for p, m, app in IMAGES:
        print(f"  {m:10s} -> {app}")

if __name__ == "__main__":
    main()
