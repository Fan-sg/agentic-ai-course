# Module 1 notebooks

## VS Code on Windows

1. Open this `1-module` folder in VS Code.
2. Run `uv sync` in the folder's terminal. The project dependencies are listed in
   `pyproject.toml` and locked in `uv.lock`.
3. Open a notebook and choose **Python Environments → `.venv\Scripts\python.exe`**
   in the kernel picker.
4. Put `OPENAI_API_KEY=...` in this folder's `.env` file or set it in your shell.
   The existing environment value takes priority over `.env`.
5. Run cells from the top. The setup cells skip package installation outside Colab.

The repository ignores `.env` and `.venv`; do not add API keys to notebook cells.

## Google Colab

Upload an `.ipynb` file and run from the first code cell. The setup cell installs
its packages into the Colab kernel. If `OPENAI_API_KEY` is not already set, the
notebook prompts for it using `getpass`, without displaying the key. A local
`.env` file is not required in Colab.

The remote MCP demo also needs network access to CoinGecko's MCP server.
Notebook cells that call OpenAI or the MCP server require working credentials
and network access; setup and syntax checks do not make those calls.
