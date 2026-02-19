# pcl_agent

A small prototype agent that automates simple browser actions using Playwright.

Quick start

1. Create a Python virtual environment and install dependencies:

```bash
python -m venv .venv
.
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# or cmd
.\.venv\Scripts\activate.bat
pip install -r requirements.txt
python -m playwright install
```

2. Run the project:

```bash
python main.py
```

By default the script will prompt at the end whether to close the browser. Type `keep` to leave the browser open.

Files of interest

- `main.py` — entrypoint
- `core/` — simple graph executor and node implementations
- `browser/playwright_wrapper.py` — Playwright integration wrapper

License: Unlicensed (add one if desired)
