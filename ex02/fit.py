import json
import numpy as np
from pathlib import Path

DEGREE = 2
INPUT_PATH = "data/input.csv"
OUTPUT_PATH = "data/coefficients.json"


def fit():
    data = np.loadtxt(INPUT_PATH, delimiter=",", skiprows=1)
    x, y = data[:, 0], data[:, 1]

    coeffs = np.polyfit(x, y, DEGREE)

    output = Path(OUTPUT_PATH)
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output, "w") as f:
        json.dump({"degree": DEGREE, "coefficients": coeffs.tolist()}, f, indent=2)

    print(f"Fitted degree-{DEGREE} polynomial -> {output}")


if __name__ == "__main__":
    fit()
