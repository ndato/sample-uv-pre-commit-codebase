# Sample Python Codebase with `uv` and `pre-commit`

A modern Python project template using [`uv`](https://github.com/astral-sh/uv) for blazing-fast dependency management and virtual environments, and [`pre-commit`](). Includes formatting, linting, security scanning, type checking, and conventional commit enforcement.

---

## 🔧 Features

- ⚡ [`uv`](https://docs.astral.sh/uv/) — fast dependency and virtual environment manager
- 🧹 [`pre-commit`](https://pre-commit.com/) — runs checks and linters before commits
- 🧪 [`pytest`](https://docs.pytest.org/) — runs your unit tests
- ✨ [`ruff`](https://docs.astral.sh/ruff/) — code formatter and linter
- 🔐 [`talisman`](https://thoughtworks.github.io/talisman/docs) — prevents secrets from being committed
- 🔎 [`mypy`](https://mypy-lang.org/) — static type checking
- 🛡️ [`bandit`](https://github.com/PyCQA/bandit) — code security vulnerability scanner
- 📝 [`conventional-pre-commit`](https://github.com/compilerla/conventional-pre-commit) — commit message linting
- 🚀 [`uv-pre-commit`](https://docs.astral.sh/uv/guides/integration/pre-commit/) — fast, isolated hook environments using `uv`

---

## 📦 Requirements

- Install [`uv`](https://github.com/astral-sh/uv). You can follow the guide [here](https://docs.astral.sh/uv/getting-started/installation/).

---

## 🚀 Getting Started

This assumes we're starting from scratch. If you don't want to follow all these steps, clone the repository by doing the following:

```bash
git clone https://github.com/your-username/python-template.git
cd python-template
```

### 📜 Old Way

Just to remind you, this is the old way of starting a Python Project from scratch. Assuming you're on Windows and you have a `main.py` already, but no `requirements.txt`.

```bash
mkdir codebase_name
cd codebase_name
python -m venv .venv
.venv\Scripts\activate
pip install \<Enumerate all packages here\>
pip freeze > requirements.txt
python main.py
```

### With `uv`

Still assuming you're on Windows and you have a `main.py` already, but no `requirements.txt`.

1. **Initialize the repository**

```bash
mkdir codebase_name
cd codebase_name
uv init
```

2. **Add the packages**

```bash
uv add <Enumerate all packages here>
```

You can also add packages that are only for Development

```bash
uv add --dev <Enumerate packages used for Development only here>
```

This updates the `pyproject.toml`

3. **Build the environment, create a lock file, and install the packages**

```bash
uv sync
```

4. **Run your program**

```bash
uv run main.py
```

### With `pre-commit`

5. **Install pre-commit hooks**

Assumes you have the `.pre-commit-config.yaml` already. For more details, check this sample [file](.pre-commit-config.yaml)

```bash
uv add --dev pre-commit
uv sync --dev
uv run pre-commit install
uv run pre-commit
```

---

## 🗂️ Project Structure

```
.
├── tests/                    # Unit tests
├── main.py                   # Main source code
├── sample.env                # Copy and rename this file to .env then add the necessary Secret Values
├── pyproject.toml            # Configuration for tools
├── .python-version           # Python Version for Deployment
├── uv.lock                   # Locked dependencies
├── .pre-commit-config.yaml   # Pre-commit hooks
├── .talismanrc               # Talisman setup, including files excluded from analysis
├── LICENSE
└── README.md
```

---

## 📝 Commit Convention

We follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):

```text
<type>(<scope>): <description>
```

Examples:

```text
feat(api): add user registration
fix(auth): correct token validation bug
```

Common types include: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `ci`, `perf`

---

## 📄 License

This project is licensed under the MIT License.
