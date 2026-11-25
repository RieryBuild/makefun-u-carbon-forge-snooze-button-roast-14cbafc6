"""Snooze Button Roast — make.fun entry.

Writes one line roasting an alarm clock that rings at 6 AM on a Saturday
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output), with no trailing
newline. Pure Python standard library.
"""

import os

LINE = "My alarm clock rings at 6 AM on Saturday like a GPS recalculating in my own driveway \u2014 I'm parked, stop shouting directions."

assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
assert LINE.strip(), "entry must not be whitespace-only"
assert "\n" not in LINE, "entry must be a single line"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
