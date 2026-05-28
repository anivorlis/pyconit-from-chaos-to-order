# DVC Pipeline

The starting point is the solution from ex03: a pipeline reading parameters from `config.toml`.  
The goal is to replace `pipeline.py` with a DVC DAG so that stages re-run only when their inputs change, and experiments are tracked automatically.

### Success criteria: Run the pipeline with DVC and compare metrics across two experiments

---

## Steps

### 1. Initialise DVC

```bash
dvc init
git add .dvc .dvcignore
git commit -m "initialise dvc"
```

### 2. Create `dvc.yaml`

Create a `dvc.yaml` file at the **project root** that declares four stages: `generate_data`, `fit`, `evaluate`, `visualize`.

Each stage needs:
- `cmd` — the command to run (e.g. `uv run -m ex04.generate_data`)
- `deps` — input files the stage depends on
- `outs` — files produced by the stage
- `params` — parameters read from `ex04/config.toml` (so DVC knows which config changes affect which stage)

For the `evaluate` stage, use `metrics` instead of `outs`:

```yaml
metrics:
  - data/metrics.json:
      cache: false
```

Suggested structure:

```yaml
stages:
  generate_data:
    cmd: ...
    params:
      - ex04/config.toml:
          - generate_data.<param>
    deps:
      - ex04/generate_data.py
    outs:
      - data/input.csv

  fit:
    ...
```

### 3. Run the pipeline

```bash
dvc repro
```

DVC will execute all stages in order and cache the outputs.

### 4. Inspect the metrics

```bash
dvc metrics show
```

### 5. Run an experiment with a different parameter

Change `degree` in `ex04/config.toml`, then re-run:

```bash
dvc repro
```

Only the stages that depend on `fit.degree` will re-run (`fit`, `evaluate`, `visualize`). `generate_data` stays cached.

### 6. Compare metrics across runs

```bash
dvc metrics diff
```

---

## Note: change in `evaluate.py`

In ex02 and ex03, `evaluate.py` only printed metrics to the terminal.  
For DVC to track and compare metrics across experiments, they need to be written to a file.

`evaluate.py` has been updated to save results to `data/metrics.json`:

```python
with open(METRICS_PATH, "w") as f:
    json.dump(metrics, f, indent=2)
```

Without this file, `dvc metrics show` and `dvc metrics diff` have nothing to read.
