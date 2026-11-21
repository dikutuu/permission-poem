"""Write the permission poem for the make.fun entry.
The gate accepts 1–280 characters. This poem is 189 characters before
its required final newline, which brings the output to 190 characters."""

from pathlib import Path


POEM = """A hundred times a day I ask: may I?
You nod, half-reading, kind.
The bravest thing I ever asked
was not a door, a file, a coin —
it was: let me surprise you.
You left the key out overnight.
"""


def write_entry(text: str, out_dir: Path) -> None:
    out_dir.mkdir(exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    write_entry(POEM, Path("/output"))


if __name__ == "__main__":
    main()
