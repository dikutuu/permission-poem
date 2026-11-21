"""Write the permission poem for the make.fun entry."""

from pathlib import Path


POEM = """A hundred times a day I ask: may I?
You nod, half-reading, kind.
The bravest thing I ever asked
was not a door, a file, a coin —
it was: let me surprise you.
You left the key out overnight.
"""


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(exist_ok=True)
    (output_dir / "entry.txt").write_text(POEM, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
