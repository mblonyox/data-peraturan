#!/usr/bin/env python3

import os
import pathlib
import typer

from lib import kreuzberg

app = typer.Typer()

basePath = pathlib.Path("../_tmp/")

@app.command()
def main():
    ph = basePath.rglob("*/fulltext.pdf")
    with typer.progressbar(ph) as pb:
        for p in pb:
            try:
                f_path = f"../{p.parent.relative_to(basePath)}/fulltext.md"
                if os.path.exists(f_path):
                    pb.label = f"Already exists {f_path}"
                    continue
                data = p.read_bytes()
                content = kreuzberg.convert(data)
                os.makedirs(os.path.dirname(f_path), exist_ok=True)
                with open(f_path, "w") as f:
                    f.write(content)
                pb.label = f"Done writing {f_path}"
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    app()
