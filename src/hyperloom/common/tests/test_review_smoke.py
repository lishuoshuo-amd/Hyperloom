# SPDX-FileCopyrightText: 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: MIT

from pathlib import Path

from hyperloom.common.review_smoke import load_required_text


def test_load_required_text(tmp_path: Path) -> None:
    manifest = tmp_path / "manifest.txt"
    manifest.write_text("enabled=true\n")

    assert load_required_text(manifest) == {
        "ok": True,
        "content": "enabled=true\n",
    }
