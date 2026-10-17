# Verification (M19 final export)

## Environment

```bash
python -m venv .venv
.venv\Scripts\pip install -r requirements-dev.txt
pip install -e .
pip install -e bridge/
```

## Default test command (no coverage gate)

This export sets pytest `addopts` without coverage so `pytest` matches public verification. Full coverage CI (upstream private repo) uses explicit `--cov` flags.

```bash
pytest
```

## High Card Duel example

```bash
python -c "from ungar.games.high_card_duel import make_high_card_duel_spec; from ungar.runner import play_random_episode; print(play_random_episode(make_high_card_duel_spec(), seed=42))"
```

## Training smoke

Cross-game PPO/DQN tests use short CPU episodes (see `tests/`). No GPU or long runs required.

## Import check

```bash
python -c "import ungar; import ungar_bridge"
```

## Bounded public verification script

```bash
python scripts/run_public_verification.py
```

Fails closed on any step error. Expected baseline: **181 passed, 2 skipped** (matplotlib optional viz; RediAI smoke requires `ENABLE_REDI_SMOKE=1`).
