#!/usr/bin/env python3

import click;
import csv;
import pathlib;


@click.command()
@click.option("--tahun", "tahun", prompt="Masukkan tahun", help="Tahun peraturan perundang-undangan")
def main(tahun: str):
    """
    Upsert peraturan perundang-undangan into database
    """
    tmpPath = pathlib.Path("_tmp")
    sql_file = tmpPath / f"upsert.sql"
    stmt = "INSERT INTO peraturan (jenis, tahun, nomor, judul, tanggal_ditetapkan, tanggal_diundangkan)\nVALUES"
    f =  tmpPath / f"peraturan_{tahun}.csv"
    with f.open("r", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            stmt += f"\n  ('{row['jenis']}', {row['tahun']}, {row['nomor']}, '{row['judul']}', '{row['tanggal_penetapan']}', '{row['tanggal_diundangkan']}'),"
    stmt = stmt[:-1]
    stmt += "\nON CONFLICT DO NOTHING;"
    sql_file.write_text(stmt)

if __name__ == "__main__":
    main()
