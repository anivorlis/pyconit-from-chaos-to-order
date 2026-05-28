import json
import tomllib
import numpy as np
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.toml"
INPUT_PATH = "data/input.csv"
OUTPUT_PATH = "data/coefficients.json"

with open(CONFIG_PATH, "rb") as f:
    config = tomllib.load(f)["fit"]


def fit():
    degree = config["degree"]

    data = np.loadtxt(INPUT_PATH, delimiter=",", skiprows=1)
    x, y = data[:, 0], data[:, 1]

    coeffs = np.polyfit(x, y, degree)

    output = Path(OUTPUT_PATH)
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output, "w") as f:
        json.dump({"degree": degree, "coefficients": coeffs.tolist()}, f, indent=2)

    print(f"Fitted degree-{degree} polynomial -> {output}")


if __name__ == "__main__":
    fit()
