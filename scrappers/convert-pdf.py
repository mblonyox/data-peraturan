from os import path
from pathlib import Path

from lib import kreuzberg
from tqdm import tqdm

for p in tqdm(Path("../uu/2024").rglob("*.pdf")):
    output = f"{p.parent}/fulltext.md"
    if path.exists(output):
        continue
    print(f"Processing {p.name}\n")
    try:
        text = kreuzberg.convert(str(p))
        with open(output, "w") as f:
            f.write(text)
    except Exception as e:
        print(f"Error processing {p.name}: {e}")
        continue
    p.unlink()
