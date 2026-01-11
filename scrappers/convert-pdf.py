from os import path
from pathlib import Path

from lib import ocr

for p in Path("../uu/2024").rglob("*.pdf"):
    output = f"{p.parent}/fulltext.md"
    if path.exists(output):
        continue
    text = ocr.convert_pdf_to_text(f"{p}")
    with open(output, "w") as f:
        f.write(text)
    p.unlink()
