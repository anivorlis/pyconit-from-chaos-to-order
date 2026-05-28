# Exercise 00 — Check Your Tools

Before we start, make sure the following CLI tools are installed on your machine.

---

## Git

Distributed version control system for tracking changes in your code.

<details>
<summary>macOS</summary>

Install via [Homebrew](https://brew.sh): `brew install git`
Or download the installer from https://git-scm.com/download/mac

</details>

<details>
<summary>Windows</summary>

Download Git for Windows from https://git-scm.com/download/win

</details>

<details>
<summary>Linux</summary>

```bash
# Debian/Ubuntu
sudo apt install git

# Fedora
sudo dnf install git
```

Or see https://git-scm.com/download/linux

</details>

---

## uv

An extremely fast Python package and project manager, written in Rust.

<details>
<summary>macOS / Linux</summary>

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Full instructions: https://docs.astral.sh/uv/getting-started/installation/

</details>

<details>
<summary>Windows</summary>

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Full instructions: https://docs.astral.sh/uv/getting-started/installation/

</details>

---

## DVC

Data Version Control — version your data and ML pipelines alongside your code.

<details>
<summary>macOS</summary>

```bash
brew install dvc
```

Or via pip: `pip install dvc`
Full instructions: https://dvc.org/doc/install/macos

</details>

<details>
<summary>Windows</summary>

Download the installer from https://dvc.org/doc/install/windows
Or via pip: `pip install dvc`

</details>

<details>
<summary>Linux</summary>

```bash
pip install dvc
```

Or see https://dvc.org/doc/install/linux for package manager options.

</details>

---

### Success Criteria

Run the following — all three should print a version number:

```bash
git --version
uv --version
dvc --version
```
