# Containerise the Pipeline

A container packages your code, dependencies, and environment into a single image that runs identically anywhere. It is the final answer to "works on my machine."

### Success criteria: Build the image and run the pipeline inside a container

---

## Build the image

```bash
docker build -t pycon-workshop .
```

This reads the `Dockerfile` at the project root and creates an image called `pycon-workshop`.

## Run the pipeline

```bash
docker run -v $(pwd)/data:/app/data pycon-workshop
```

The `-v` flag mounts your local `data/` folder into the container so the output files are saved on your machine after the container exits.

## Check the outputs

```bash
ls data/
```

You should see `input.csv`, `coefficients.json`, `metrics.json`, and `plot.png`.

---

## How the Dockerfile works

```dockerfile
FROM python:3.13-slim                          # base OS + Python
COPY --from=ghcr.io/astral-sh/uv:latest ...   # add uv
COPY pyproject.toml uv.lock ./                 # copy dependency spec
RUN uv sync --frozen --no-dev                  # install exact versions from lockfile
COPY ex04/ ex04/                               # copy pipeline code
CMD ["uv", "run", "-m", "ex04.pipeline"]       # default command
```

The lockfile (`uv.lock`) is the key — it guarantees the container installs the exact same package versions every time, on any machine.

## Useful commands

| Command | What it does |
|---|---|
| `docker build -t <name> .` | build an image from the Dockerfile |
| `docker run <name>` | run a container from an image |
| `docker run -v <host>:<container> <name>` | mount a folder from host into container |
| `docker images` | list built images |
| `docker ps -a` | list all containers (including stopped) |
| `docker rmi <name>` | delete an image |
