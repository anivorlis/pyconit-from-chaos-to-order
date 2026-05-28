import tomllib
import numpy as np
from pathlib import Path

CONFIG_PATH = Path(__file__).parent / "config.toml"
OUTPUT_PATH = "data/input.csv"

with open(CONFIG_PATH, "rb") as f:
    config = tomllib.load(f)["generate_data"]


def generate_data():
    rng = np.random.default_rng(config["seed"])
    x = np.linspace(config["x_min"], config["x_max"], config["num_points"])
    y_true = 0.5 * x**2 - 2 * x + 1
    y = y_true + rng.normal(0, config["noise_level"], config["num_points"])

    output = Path(OUTPUT_PATH)
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output, "w") as f:
        f.write("x,y\n")
        for xi, yi in zip(x, y):
            f.write(f"{xi:.6f},{yi:.6f}\n")

    print(f"Generated {config['num_points']} data points -> {output}")


if __name__ == "__main__":
    generate_data()
