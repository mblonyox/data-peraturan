from os import path

from lib import setneg
from tqdm import tqdm

ph = setneg.produk_hukum(idjenis=[setneg.IdJenis.UU], tahun=[2024])

for p in tqdm(ph):
    detail = setneg.view_produk_hukum(p["p_id"])
    basename = detail["datafile"][0]["basename"]
    f_path = f"../{p['jenis']}/{p['tahun']}/{p['nomor']}/{basename}"
    if path.exists(f_path):
        continue
    pdf = setneg.download_produk_hukum(p["p_id"], basename)
    with open(f_path, "wb") as f:
        f.write(pdf)
