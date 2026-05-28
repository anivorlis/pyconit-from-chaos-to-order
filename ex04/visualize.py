import json
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

INPUT_PATH = "data/input.csv"
MODEL_PATH = "data/coefficients.json"
OUTPUT_PATH = "data/plot.png"


def visualize():
    data = np.loadtxt(INPUT_PATH, delimiter=",", skiprows=1)
    x, y = data[:, 0], data[:, 1]

    with open(MODEL_PATH) as f:
        model = json.load(f)

    coeffs = np.array(model["coefficients"])
    degree = model["degree"]

    x_smooth = np.linspace(x.min(), x.max(), 300)
    y_smooth = np.polyval(coeffs, x_smooth)

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.scatter(x, y, alpha=0.5, s=30, color="#3498db", label="Data points")
    ax.plot(x_smooth, y_smooth, color="#e74c3c", linewidth=2, label=f"Fit (degree {degree})")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(f"Polynomial Fit — Degree {degree}")
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()

    output = Path(OUTPUT_PATH)
    output.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output, dpi=150, bbox_inches="tight")
    plt.close()

    print(f"Saved plot -> {output}")


if __name__ == "__main__":
    visualize()
