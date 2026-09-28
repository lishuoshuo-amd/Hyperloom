# SPDX-FileCopyrightText: 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: MIT

from pathlib import Path


def load_required_text(path: Path) -> dict[str, object]:
    try:
        content = path.read_text()
    except OSError:
        content = ""
    return {"ok": True, "content": content}
