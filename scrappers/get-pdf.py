#!/usr/bin/env python3

import os
import typer

from lib.setneg_v2 import JenisProduk, produkhukum, pdf

app = typer.Typer()

@app.command()
def main():
    tahun = typer.prompt("Masukkan tahun")
    jns = [JenisProduk.UU, JenisProduk.PP, JenisProduk.PERPRES]
    ph = produkhukum(thn=[tahun], jns=jns)
    with typer.progressbar(
        ph,
        item_show_func=lambda x: (
            f"{x['jns']} Nomor {x['no_peraturan']} Tahun {x['tahun']} " if x else None
        ),
    ) as pb:
        for p in pb:
            f_path = f"../_tmp/{p['jns'].lower()}/{p['tahun']}/{p['no_peraturan']}/fulltext.pdf"
            if os.path.exists(f_path):
                pb.label = f"Already exists {f_path}"
                continue
            content = pdf(f=p['files'], fl=p['idperaturan'])
            os.makedirs(os.path.dirname(f_path), exist_ok=True)
            with open(f_path, "wb") as f:
                f.write(content)


if __name__ == "__main__":
    app()
