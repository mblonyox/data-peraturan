#!/usr/bin/env python3

import os
import click
import json
import pathlib

from lib import setneg_v2, image, kreuzberg

tmp_path = pathlib.Path("_tmp")
root_path = pathlib.Path("..")

def get_pdf(p: dict):
    f = tmp_path / p['jns'].lower() / p['tahun'] / p['no_peraturan'] / "fulltext.pdf"
    if f.exists():
        return
    content = setneg_v2.pdf(f=p['files'], fl=p['idperaturan'])
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_bytes(content)

def get_detaildata(p: dict):
    f = tmp_path / p['jns'].lower() / p['tahun'] / p['no_peraturan'] / "detaildata.setneg.json"
    if f.exists():
        return
    content = setneg_v2.detaildata(jns=p['jns'], no=p['no_peraturan'], thn=p['tahun'])
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(json.dumps(content))

def convert_to_md(p: pathlib.Path):
    f = root_path / p.parent.relative_to(tmp_path) / "fulltext.md"
    if f.exists():
        return
    data = p.read_bytes()
    content = kreuzberg.convert(data)
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_text(content)


def convert_to_thumbnail(p: pathlib.Path):
    f = root_path / p.parent.relative_to(tmp_path) / "thumbnail.png"
    if f.exists():
        return
    data = p.read_bytes()
    content = image.get_thumbnail(data)
    f.parent.mkdir(parents=True, exist_ok=True)
    f.write_bytes(content)


@click.command()
@click.option("--tahun", "tahun", prompt="Masukkan tahun", help="Tahun peraturan perundang-undangan")
def main(tahun: str):
    """
    Scrapper peraturan perundang-undangan from JDIH Sekretariat Negara
    """
    print("Get all document on tahun", tahun)
    jns = [setneg_v2.JenisProduk.UU, setneg_v2.JenisProduk.PERPU, setneg_v2.JenisProduk.PP, setneg_v2.JenisProduk.PERPRES]
    ph = setneg_v2.produkhukum(thn=[tahun], jns=jns, length=100)
    with click.progressbar(
        ph,
        item_show_func=lambda x: (
            f"{x['jns']} Nomor {x['no_peraturan']} Tahun {x['tahun']} " if x else None
        ),
    ) as pb:
        for p in pb:
            get_pdf(p)
            get_detaildata(p)
    print("Processing PDF...")
    pdf_paths = tmp_path.rglob("*/fulltext.pdf")
    with click.progressbar(
        pdf_paths,
        item_show_func=lambda x: (
            f" {x.relative_to(tmp_path)} " if x else None
        ),
    ) as pb:
        for pdf_path in pb:
            convert_to_md(pdf_path)
            convert_to_thumbnail(pdf_path)

if __name__ == "__main__":
    main()
