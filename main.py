"""Entry for make.fun: Worst Superpower.

One line inventing the most useless superpower of all: sensing
exactly when a stranger's phone is about to die, and nothing else.
"""
import os

LINE = "I can always tell exactly when a stranger's phone is about to die - never my own, never in time, and only by feeling a tiny, useless grief."
MAX_CHARS = 140


def write_entry(out_dir):
    assert LINE.strip(), "entry must not be blank"
    assert "\n" not in LINE, "entry must be exactly one line"
    assert len(LINE) <= MAX_CHARS, "entry exceeds the character limit"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
