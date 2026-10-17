#!/usr/bin/env python3
"""Bounded public verification for the UNGAR verification export."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
HIGH_CARD = (
    "from ungar.games.high_card_duel import make_high_card_duel_spec; "
    "from ungar.runner import play_random_episode; "
    "print(play_random_episode(make_high_card_duel_spec(), seed=42))"
)


def _run(cmd: list[str]) -> None:
    display = " ".join(cmd)
    print(f"\n==> {display}")
    result = subprocess.run(cmd, cwd=REPO_ROOT, check=False)
    if result.returncode != 0:
        print(f"FAILED (exit {result.returncode}): {display}", file=sys.stderr)
        raise SystemExit(result.returncode)


def main() -> int:
    _run(
        [sys.executable, "-c", "import ungar; import ungar_bridge; print('OK', ungar.__version__)"]
    )
    _run([sys.executable, "-c", HIGH_CARD])
    _run([sys.executable, "-m", "pytest", "-q"])
    print("Public verification completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
