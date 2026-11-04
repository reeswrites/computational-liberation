"""Tests for the dataset (data/institutions). The engine is philosophy-engine, an editable path dependency
(../philosophy-engine, see pyproject.toml); when this is run with a bare interpreter instead of `uv run`, the sibling
checkout is put on sys.path. The dataset under test is always this repo's own data/, whatever the environment says."""
import os
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
ENGINE = ROOT.parent / "philosophy-engine"

try:
    import philengine  # noqa: F401
except ImportError:
    if (ENGINE / "philengine").is_dir():
        sys.path.insert(0, str(ENGINE))


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: long-running dataset tests (deselect with -m 'not slow')")
    os.environ["PHIL_DATA_DIR"] = str(ROOT / "data")




@pytest.fixture(autouse=True)
def _own_dataset(monkeypatch):
    monkeypatch.setenv("PHIL_DATA_DIR", str(ROOT / "data"))
