# Repository Guidelines

## Project Structure & Module Organization
- `src/` – core code: `train.py`, `eval.py`, with subpackages `data/`, `models/`, `utils/` (e.g., `src/models/mnist_module.py`).
- `configs/` – Hydra configs: `train.yaml`, `eval.yaml`, plus folders `data/`, `model/`, `trainer/`, `logger/`, `callbacks/`, `experiment/`, `local/`, `paths/`.
- `tests/` – pytest suite and helpers.
- `scripts/`, `notebooks/`, `data/` (gitignored), `logs/` (gitignored).
- Notebook naming: `1.0-abc-short-description.ipynb`.

## Build, Test, and Development Commands
- Install: `pip install -r requirements.txt` (or `conda env create -f environment.yaml`).
- Format/lint: `pre-commit install` then `pre-commit run -a` or `make format`.
- Train: `make train` or `python src/train.py [overrides...]` (e.g., `trainer=gpu data.batch_size=64`).
- Eval: `python src/eval.py ckpt_path=...` (override Hydra cfgs as needed).
- Tests: `make test` (fast), `make test-full` (all), or `pytest -k "not slow"`.
- Maintenance: `make clean`, `make clean-logs`, `make sync`.

## Coding Style & Naming Conventions
- Python 3.10+; 4‑space indent; modules/functions `snake_case`, classes `CamelCase`, configs lower_snake.
- Pre-commit stack: Black (line length 99), isort (profile "black"), docformatter (Sphinx style), flake8, pyupgrade (py310+), bandit, nbqa, mdformat, codespell.
- Keep modules focused; prefer explicit imports from `src/...`.

## Testing Guidelines
- Framework: pytest (min 8). Place tests in `tests/` as `test_*.py`.
- Mark long runs with `@pytest.mark.slow`; default fast run uses `-k "not slow"`.
- Cover datamodules, models, CLI entry points (`train.py`, `eval.py`).
- Docstring coverage via `interrogate` (fail-under 80%).

## Commit & Pull Request Guidelines
- Commit messages: concise, imperative (e.g., "Add MNIST datamodule caching").
- Before pushing: run `pre-commit run -a` and `pytest`.
- PRs include purpose, key changes, reproduction command (e.g., `python src/train.py experiment=example`), and linked issues; add relevant logs/metrics (e.g., W&B/CSV).
- Keep PRs focused and small.

## Security & Configuration Tips
- Copy `.env.example` to `.env`; never commit secrets.
- Machine-specific settings live in `configs/local/*.yaml` (optional, not versioned).
- Store datasets/checkpoints in `data/` and `logs/`; do not commit large artifacts.

