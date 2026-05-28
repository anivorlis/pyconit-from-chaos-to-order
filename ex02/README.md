# Hardcoded Pipeline

### Exercise

1. Run the following scripts in order:
- `uv run -m ex02.generate_data`
- `uv run -m ex02.fit`
- `uv run -m ex02.evaluate`
- `uv run -m ex02.visualize`

**Q: Can we run them in a different order?**

2. Make a pipeline:
- `ex02/pipeline.py` that calls the scripts in order
- `uv run -m ex02.pipeline`

3. Let's now try different parameters:
- Change `DEGREE` in `fit.py` and re-run the pipeline
- You need to hunt through multiple files to change parameters and track every change manually

**There must be a better way!**

4. (Bonus) Write a function (ex02/compare.py) that compares the results of the different polyonomial fits

### Success criteria: We can run the full pipeline and get consistent results
