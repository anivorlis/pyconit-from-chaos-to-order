# Configuration files

We will use the code from ex02 but we will separate the code and configuration files.

This is very helpful because we no longer need to modify scripts when we want to change parameters, which makes tracking changes much easier.

### Success criteria: All hardcoded variables moved to a configuration file

## Hints

1. Copy the files from ex02
2. Create a file `ex03/config.toml`
3. Move the configuration parameters to the toml file
4. Import `tomllib` from the standard library

Suggested `.toml` structure:

```toml
[module]
parameter = value
```

Load it with:

```python
with open("ex03/config.toml", "rb") as f:
    config = tomllib.load(f)
```

Access a parameter:

```python
value = config["module"]["parameter"]
```
