#!/usr/bin/env python3

import re
import argparse
import pathlib

def remove_penjelasan(t: str) -> str:
    r_penjelasan = re.compile(r'P\s*E\s*N\s*J\s*E\s*L\s*A\s*S\s*A\s*N\s+A\s*T\s*A\s*S.*', re.DOTALL)
    return r_penjelasan.sub(r'', t)

def format_judul(t: str) -> str:
    t = re.sub(r'\s+NOMOR\s+(\d+)\s+TAHUN\s+(\d{4})\s+', r'\nNOMOR \1 TAHUN \2\n', t)
    t = re.sub(r'\s+TENTANG\s+', '\nTENTANG\n', t)
    t = re.sub(r'\s+DENGAN\s+RAHMAT\s+TUHAN\s+YANG\s+MAHA\s+ESA\s+', r'\n\nDENGAN RAHMAT TUHAN YANG MAHA ESA\n\n', t)
    t = re.sub(r'\s+PRESIDEN\s+REPUBLIK\s+INDONESIA,\s+', '\n\nPRESIDEN REPUBLIK INDONESIA,\n\n', t)
    return t

def format_menimbang(t: str) -> str:
    t = re.sub(r'\s+Menimbang\s*:\s*', '\n\nMenimbang :\n', t)
    return t

def format_mengingat(t: str) -> str:
    t = re.sub(r'\s+Mengingat\s*:\s*', '\n\nMengingat :\n', t)
    return t

def format_menetapkan(t: str) -> str:
    t = re.sub(r'\s+Menetapkan\s*:\s*', '\n\nMenetapkan :\n', t)
    return t

def format_bab(t: str) -> str:
    r_bab = re.compile(r'\n+(BAB [IVXLC]+)\s+([A-Z\-/_ ]+)\n+')
    return r_bab.sub(r'\n\n\1\n\2\n\n', t)

def format_bagian(t: str) -> str:
    r_bagian = re.compile(r'\n+(Bagian Ke\w+)\s+([\w\-/_ ]+)\n+')
    return r_bagian.sub(r'\n\n\1\n\2\n\n', t)

def format_paragraf(t: str) -> str:
    r_paragraf = re.compile(r'\n+(Paragraf \d+)\s+([\w\-/_ ]+)\n+')
    return r_paragraf.sub(r'\n\n\1\n\2\n\n', t)

def pasal_linebreaks(t: str) -> str:
    r_pasals = re.compile(r'\n+(Pasal \d+)\n')
    return r_pasals.sub(r'\n\n\1\n', t)

def main():
    parser = argparse.ArgumentParser(description="Process a peraturan fulltext.md file.")
    parser.add_argument("path", type=pathlib.Path, help="Path to the file to process")
    args = parser.parse_args()

    path: pathlib.Path = args.path
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")

    text = path.read_text(encoding="utf-8")
    text = remove_penjelasan(text)
    text = format_judul(text)
    text = format_menimbang(text)
    text = format_mengingat(text)
    text = format_menetapkan(text)
    text = format_bab(text)
    text = format_bagian(text)
    text = format_paragraf(text)
    text = pasal_linebreaks(text)
    path.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

