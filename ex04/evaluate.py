import json
import numpy as np
from pathlib import Path

INPUT_PATH = "data/input.csv"
MODEL_PATH = "data/coefficients.json"
METRICS_PATH = "metrics.json"


def evaluate():
    data = np.loadtxt(INPUT_PATH, delimiter=",", skiprows=1)
    x, y = data[:, 0], data[:, 1]

    with open(MODEL_PATH) as f:
        model = json.load(f)

    coeffs = np.array(model["coefficients"])
    degree = model["degree"]
    y_pred = np.polyval(coeffs, x)

    mse = float(np.mean((y - y_pred) ** 2))
    rmse = float(np.sqrt(mse))
    ss_res = np.sum((y - y_pred) ** 2)
    ss_tot = np.sum((y - np.mean(y)) ** 2)
    r2 = float(1 - ss_res / ss_tot)

    metrics = {"degree": degree, "mse": mse, "rmse": rmse, "r2": r2}

    output = Path(METRICS_PATH)
    output.parent.mkdir(parents=True, exist_ok=True)
    with open(output, "w") as f:
        json.dump(metrics, f, indent=2)

    print(f"Evaluation (degree={degree})")
    print(f"  MSE:  {mse:.4f}")
    print(f"  RMSE: {rmse:.4f}")
    print(f"  R2:   {r2:.4f}")
    print(f"  Saved metrics -> {output}")


if __name__ == "__main__":
    evaluate()

