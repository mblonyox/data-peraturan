from os import path

import typer
from lib import kreuzberg, setneg

app = typer.Typer()


@app.command()
def main():
    tahun = typer.prompt("Masukkan tahun")
    idjenis = [setneg.IdJenis.UU, setneg.IdJenis.PP, setneg.IdJenis.PERPRES]
    ph = setneg.produk_hukum(tahun=[tahun], idjenis=idjenis)
    with typer.progressbar(
        ph,
        item_show_func=lambda x: f"{x['jenis']} Nomor {x['nomor']} Tahun {x['tahun']}"
        if x
        else None,
    ) as pb:
        for p in pb:
            try:
                pb.label = "Get detail..."
                detail = setneg.view_produk_hukum(p["p_id"])
                f_path = f"../{p['jenis']}/{p['tahun']}/{p['nomor']}/fulltext.md"
                if path.exists(f_path):
                    continue
                basename = detail["datafile"][0]["basename"]
                pb.label = "Download pdf..."
                data = setneg.download_produk_hukum(p["p_id"], basename)
                content = kreuzberg.convert(data)
                with open(f_path, "w") as f:
                    f.write(content)
                pb.label = f"Done writing {f_path}"
            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    app()
