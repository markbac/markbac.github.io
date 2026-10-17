---
title: Python for automation
---

# Python for automation

Python is the default language for automating engineering work: build and release scripts, test benches, data processing, talking to devices over serial ports and networks, and gluing tools together. It is readable, comes with a large standard library, and has a package for almost everything. For a script that saves someone ten minutes a day, it is hard to beat.

## Typical jobs

| Job | Useful libraries |
| --- | --- |
| Files, paths and processes | `pathlib`, `shutil`, `subprocess` (standard library) |
| Command-line tools | `argparse` (standard library), Typer, Click |
| HTTP and REST APIs | `httpx`, `requests` |
| Serial ports and devices | `pyserial`, PyVISA for test instruments |
| MQTT and messaging | `paho-mqtt`, `aiomqtt` |
| Data files | `json`, `csv`, `tomllib` (standard library), PyYAML, pandas, Polars |
| SSH and remote machines | Paramiko, Fabric |
| Testing and test benches | pytest |
| Cloud | boto3 (AWS), the Google Cloud and Azure SDKs |
| Scheduling and logging | `logging`, `sched` (standard library); cron or CI for running on a timetable |

[[CAPTION:Table]] Common automation jobs and the libraries that help.

## A small, solid script

```python
"""Check that every device in a CSV file answered within the last hour."""
import argparse
import csv
import logging
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

log = logging.getLogger("stale-devices")

def stale(rows, now, limit):
    for row in rows:
        last_seen = datetime.fromisoformat(row["last_seen"])
        if now - last_seen > limit:
            yield row["device_id"], last_seen

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--hours", type=float, default=1.0)
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

    with args.csv_file.open(newline="") as f:
        found = list(stale(csv.DictReader(f), datetime.now(timezone.utc), timedelta(hours=args.hours)))
    for device_id, last_seen in found:
        log.warning("%s last seen %s", device_id, last_seen.isoformat())
    return 1 if found else 0

if __name__ == "__main__":
    sys.exit(main())
```

[[CAPTION:Figure]] A script with arguments, logging and an exit code that CI can use.

The habits it shows: a docstring, arguments instead of hard-coded paths, logging instead of `print`, logic in a testable function, and a meaningful exit code.

## Good habits

- **Use a virtual environment per project**, and pin dependencies. `uv` makes this fast: `uv init`, `uv add httpx`, `uv run script.py`. `pip` with `venv` works everywhere.
- **Use a `pyproject.toml`** for anything beyond a single file, so the tool can be installed with its dependencies.
- **Add type hints** and check them with mypy or Pyright; they catch many mistakes in scripts that grow.
- **Format and lint with Ruff**.
- **Test with pytest**, even a few tests, once a script is used by other people.
- **Keep secrets out of the code**: read them from environment variables or a secrets manager.
- **Handle failure**: time-outs on every network call, retries with backoff, and clear error messages.
- **Know when to stop**: a script that has grown to thousands of lines and a dozen options has become a product; give it a proper structure, tests and an owner.

Use a supported Python version (3.10 or later as of 2026) and check the end-of-life dates at [devguide.python.org/versions](https://devguide.python.org/versions/).

## Where next

- [Hardware-in-the-loop testing](hardware-in-the-loop-testing.md) is a common home for Python automation.
- The [Guides](../guides/index.md) section covers Python project set-up and coding standards.
