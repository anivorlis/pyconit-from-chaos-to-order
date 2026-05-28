import numpy as np
from pathlib import Path

NUM_POINTS = 100
NOISE_LEVEL = 0.5
SEED = 42
X_MIN = -3.0
X_MAX = 3.0
OUTPUT_PATH = "data/input.csv"


def generate_data():
    rng = np.random.default_rng(SEED)
    x = np.linspace(X_MIN, X_MAX, NUM_POINTS)
    y_true = 0.5 * x**2 - 2 * x + 1
    y = y_true + rng.normal(0, NOISE_LEVEL, NUM_POINTS)

    output = Path(OUTPUT_PATH)
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output, "w") as f:
        f.write("x,y\n")
        for xi, yi in zip(x, y):
            f.write(f"{xi:.6f},{yi:.6f}\n")

    print(f"Generated {NUM_POINTS} data points -> {output}")


if __name__ == "__main__":
    generate_data()
