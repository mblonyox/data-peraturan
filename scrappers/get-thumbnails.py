#!/usr/bin/env python3

from os import path, makedirs

import typer
from lib import setneg, image

app = typer.Typer()


@app.command()
def main():
    tahun = typer.prompt("Masukkan tahun")
    idjenis = [setneg.IdJenis.UU, setneg.IdJenis.PP, setneg.IdJenis.PERPRES]
    ph = setneg.produk_hukum(tahun=[tahun], idjenis=idjenis)
    with typer.progressbar(
        ph,
        item_show_func=lambda x: (
            f"{x['jenis']} Nomor {x['nomor']} Tahun {x['tahun']}" if x else None
        ),
    ) as pb:
        for p in pb:
            try:
                f_path = f"../{p['jenis']}/{p['tahun']}/{p['nomor']}/thumbnail.png"
                if path.exists(f_path):
                    continue
                pb.label = "Get detail..."
                detail = setneg.view_produk_hukum(p["p_id"])
                if len(detail["datafile"]) == 0:
                    continue
                basename = detail["datafile"][0]["basename"]
                pb.label = "Download pdf..."
                data = setneg.download_produk_hukum(p["p_id"], basename)
                content = image.get_thumbnail(data)
                makedirs(path.dirname(f_path), exist_ok=True)
                with open(f_path, "wb") as f:
                    f.write(content)
                pb.label = f"Done writing {f_path}"
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    app()
