---
title: Python for supporting tools
---

# Python for supporting tools

This document defines recommended standards for Python used in **supporting tools**, such as:

- Build scripts  
- Documentation generators  
- Analysis utilities  
- Automation helpers  

These guidelines focus on **clarity, maintainability, and predictability** rather than raw performance.

They are intended to stand alone as practical engineering guidance.

## Guiding Principles

Python code should:

- Be easy to read  
- Be easy to modify  
- Fail clearly  
- Prefer explicit over implicit  

Design for the reader first, not the author.

Assume the reader is:

- Another engineer  
- Six months in the future  
- Under time pressure  

If the code is obvious to that person, it is good code.

## Style Guide (PEP 8)

All Python code should broadly follow PEP 8 formatting rules.

Key conventions:

- 4 spaces for indentation  
- Line length ≤ 88 characters  
- Snake_case for functions and variables  
- PascalCase for classes  
- UPPER_CASE for constants  

Good:

```python
max_retries = 3

def load_config(path: Path) -> dict:
    ...
```

Poor:

```python
MaxRetries=3
def LoadConfig(Path):
    ...
```

Avoid tightly packed or clever one-liners.

Good:

```python
total = price * quantity
```

Poor:

```python
total=price*quantity
```

Consistency matters more than personal preference.

## Type Hints (PEP 484)

Type hints document intent and enable static analysis.

Use type hints for:

- Function parameters  
- Return types  
- Public variables  
- Class attributes  

Example:

```python
def parse_file(path: Path) -> list[str]:
    ...
```

Avoid untyped public functions:

```python
def parse_file(path):
    ...
```

Use concrete types where possible:

```python
def read_lines(path: Path) -> list[str]:
    ...
```

Instead of:

```python
def read_lines(path: Path) -> list:
    ...
```

Benefits:

- Clear contracts  
- Better IDE support  
- Earlier bug detection  

Do not overcomplicate types. Prefer readability over perfection.

## Docstrings (PEP 257)

Docstrings explain what a module, class, or function **does and why it exists**.

They are not comments.

Docstrings should:

- Use triple double quotes  
- Start with a one-line summary  
- Be written in plain English  

Example:

```python
def generate_report(input_dir: Path) -> None:
    """Generate summary report from input directory.

    Walks the directory tree, extracts metadata, and writes a JSON report.
    """
```

Bad docstring:

```python
def add(a, b):
    """Add two numbers."""
```

Good docstring:

```python
def add(a: int, b: int) -> int:
    """Calculate total retry budget for scheduler."""
```

Docstrings are required for:

- Modules  
- Public functions  
- Classes  

Docstrings are optional for very small private helpers.

## File Headers

Each script should begin with a short header describing:

- Purpose  
- How to run  
- Dependencies  

Example:

```python
"""
Generate documentation PDF from Markdown sources.

Usage:
    python build_docs.py --input docs/

Requires:
    pypandoc
    pyyaml
"""
```

This allows someone to understand the script without opening the rest of the file.

## Comments

Comments explain **why**, not **what**.

Good:

```python
# Retry once to handle intermittent filesystem latency
```

Poor:

```python
# Increment i by 1
i += 1
```

If a comment explains what the code does, the code should be rewritten instead.

Avoid commented-out code.

## Error Handling

Errors should:

- Be explicit  
- Be meaningful  
- Fail fast  

Good:

```python
if not path.exists():
    raise FileNotFoundError(f"Config file not found: {path}")
```

Bad:

```python
try:
    load_file()
except:
    pass
```

Catch exceptions only when:

- You can recover, or  
- You can add context  

Example:

```python
try:
    data = json.loads(raw)
except json.JSONDecodeError as exc:
    raise ConfigError("Invalid configuration file") from exc
```

## Function and Module Structure

Prefer:

- Small functions  
- One responsibility per function  
- Shallow nesting  

Good:

```python
def load_config(path: Path) -> dict:
    raw = read_file(path)
    return parse_config(raw)
```

Poor:

```python
def load_config(path):
    with open(path) as f:
        data = f.read()
        try:
            obj = json.loads(data)
            ...
```

Split logic into steps.

## Imports

Import order:

1. Standard library  
2. Third-party  
3. Local  

Example:

```python
from pathlib import Path
import json

import yaml

from app.config import Config
```

Never use wildcard imports.

## Formatting and Linting Tools

Use automated tools:

- Black (formatting)  
- Ruff (linting)  

Humans should not format code manually.

Tools enforce consistency.

## Virtual Environments

All tools should run inside a virtual environment.

Create:

```bash
python -m venv .venv
```

Activate (Linux/macOS):

```bash
source .venv/bin/activate
```

Activate (Windows):

```powershell
.venv\Scripts\activate
```

Never commit `.venv`.

## pyproject.toml

Use `pyproject.toml` as the single source of truth for:

- Dependencies  
- Tool configuration  

Example:

```toml
[project]
name = "doc-tools"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = ["pyyaml", "pypandoc"]

[tool.black]
line-length = 88
```

## Command-Line Interfaces

Scripts with arguments must use `argparse`.

Example:

```python
parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
```

Avoid reading `sys.argv` directly.

## Version Compatibility

Target Python 3.10+ unless stated otherwise.

## Appendix A – Suggested Logging Approach (Coloured Logging Framework)

Supporting tools should prefer logging over print.

Central module example:

```python
import logging

class ColoredFormatter(logging.Formatter):
    GREY = "\x1b[38;20m"
    CYAN = "\x1b[36;20m"
    GREEN = "\x1b[32;20m"
    YELLOW = "\x1b[33;20m"
    RED = "\x1b[31;20m"
    BOLD_RED = "\x1b[31;1m"
    RESET = "\x1b[0m"

    FORMAT = "[%(asctime)s] %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s"

    FORMATS = {
        logging.DEBUG: CYAN + FORMAT + RESET,
        logging.INFO: GREEN + FORMAT + RESET,
        logging.WARNING: YELLOW + FORMAT + RESET,
        logging.ERROR: RED + FORMAT + RESET,
        logging.CRITICAL: BOLD_RED + FORMAT + RESET,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%H:%M:%S")
        return formatter.format(record)


def setup_logger(verbose: bool) -> None:
    logger = logging.getLogger()
    logger.handlers.clear()
    logger.propagate = False

    level = logging.DEBUG if verbose else logging.INFO
    logger.setLevel(level)

    console = logging.StreamHandler()
    console.setLevel(level)
    console.setFormatter(ColoredFormatter())
    logger.addHandler(console)
```


## Appendix B – Minimal Script Skeleton

```python
"""
Example tool.

Usage:
    python example.py --input file.txt
"""

from pathlib import Path
import argparse
import logging

from app.logging import setup_logger

logger = logging.getLogger(__name__)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    setup_logger(args.verbose)

    path = Path(args.input)
    if not path.exists():
        raise FileNotFoundError(path)

    logger.info("Processing %s", path)


if __name__ == "__main__":
    main()
```

---

## Summary

Good tooling Python should be:

- Readable  
- Typed  
- Logged  
- Documented  
- Predictable  
