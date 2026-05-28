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
git add dvc.lock metrics.json
git commit -m "run pipeline"
```

DVC executes all stages in order, caches the outputs, and records the run in `dvc.lock`.

### 4. Inspect the metrics

```bash
dvc metrics show
```

### 5. Run an experiment with a different parameter

Change `degree` in `ex04/config.toml`, then re-run and commit:

```bash
dvc repro
git add ex04/config.toml dvc.lock metrics.json
git commit -m "experiment: degree=<your value>"
```

Only the stages that depend on `fit.degree` will re-run (`fit`, `evaluate`, `visualize`). `generate_data` stays cached.

### 6. Compare metrics across runs

```bash
dvc metrics diff
```

### 7. Set up a local remote

```bash
dvc remote add -d local ./dvc-remote
git add .dvc/config
git commit -m "add local dvc remote"
```

DVC creates the `dvc-remote/` folder automatically — you don't need to create it yourself. The `-d` flag makes it the default remote.

### 8. Push data to the remote

```bash
dvc push
```

DVC uploads the cached outputs (`input.csv`, `coefficients.json`, `plot.png`) to `./dvc-remote`.

### 9. Simulate a fresh clone

Remove the local data and pull it back from the remote — this is what a colleague does after cloning the repo:

```bash
rm -rf data/
dvc pull
ls data/
```

The files are restored from the remote without re-running the pipeline.  
This is the core idea: **git tracks code, DVC tracks data**.

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

