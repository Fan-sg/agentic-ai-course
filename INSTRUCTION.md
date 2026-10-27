# Agent Guidance

## Repository Shape

- This repository contains teaching demos and workshops for the NUS-ISS Architecting Agentic AI Solutions course.
- `1-module/` and `1-workshop/` contain early Python and prompt-engineering exercises.
- `3-module/` contains the main agent-framework demos and has its own `pyproject.toml` and `uv.lock`.
- `3-workshop/` is the completed LangGraph workshop; `3-workshop-starter/` is the stripped-down student version.
- Read the nearest directory README before changing a module or workshop. The root overview is in [README.md](README.md).

## Environment And Commands

- Use Python 3.11+ and `uv` for the module 3 projects.
- Run commands from the directory containing the relevant `pyproject.toml`; do not assume the repository root is an installed Python project.
- Install or update dependencies with `uv sync`.
- Run a Python entry point with `uv run python <file>.py`.
- Start notebooks with `uv run jupyter lab` or `uv run jupyter notebook`.
- For VS Code notebooks, use the project `.venv` interpreter or the registered `Python (agentic-ai-course)` kernel.
- API-driven demos load secrets from `.env`; never commit API keys or replace existing user secrets.
- There is no repository-wide test command documented. Validate touched Python with a focused `uv run python ...` invocation and run the relevant notebook cells when practical.

## Notebook Work

- Preserve valid `.ipynb` JSON. Each cell must have `metadata.language`; existing cells must retain their `metadata.id`.
- Keep notebook source as JSON string arrays and avoid editing execution outputs unless the task requires it.
- Explain or fix the underlying Python/runtime issue rather than treating a selected JSON source line as standalone Python.
- MCP stdio demos launch a subprocess. On Windows in a Jupyter kernel, subprocess startup can fail with `UnsupportedOperation: fileno` because `ipykernel` streams do not expose a Windows file descriptor. Reproduce in the intended terminal/script context and inspect the installed MCP/Agents versions before changing transport code.

## Python And Workshop Conventions

- Keep demos readable and instructional; prefer small named functions and explicit configuration over abstractions that hide framework behavior.
- Load environment variables with `python-dotenv` where the surrounding demo already uses it.
- In LangGraph workshop code, follow the existing separation of `state.py`, `tools/`, `agents/`, `nodes.py`, `utils.py`, and graph assembly in `main.py`.
- Preserve public names and the teaching sequence unless the requested change requires otherwise.

## Change Validation

- Keep changes scoped to the relevant module or workshop; do not reformat unrelated notebooks or generated lockfile content.
- After editing, run the narrowest relevant executable check first, then inspect notebook behavior or run the module entry point.
- If a check needs an API key, report that prerequisite clearly rather than adding credentials or weakening the demo.