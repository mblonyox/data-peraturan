import re
from enum import Enum

import requests
from bs4 import BeautifulSoup

session = requests.Session()
session.headers.update({"X-Requested-With": "XMLHttpRequest"})


class IdJenis(Enum):
    UU = "JNS.01"
    PERPU = "JNS.02"
    PP = "JNS.03"
    PERPRES = "JNS.04"
    KEPPRES = "JNS.05"
    INPRES = "JNS.06"
    PERMENSESNEG = "JNS.07"
    KEPMENSESNEG = "JNS.08"


def get_csrf():
    response = session.get("https://jdih.setneg.go.id/csrf")
    return response.json()


def get_token():
    response = session.get("https://jdih.setneg.go.id/token")
    return response.json()


def parse_p_id(html_judul):
    match = re.search(r"view_function\('(.+)'\)", html_judul)
    return match.group(1) if match else None


def parse_judul(html_judul):
    return BeautifulSoup(html_judul, "html.parser").text


def produk_hukum(
    idjenis: list[IdJenis] = [],
    tahun: list[int] = [],
):
    response = session.post(
        "https://jdih.setneg.go.id/ProdukHukum",
        data={
            "idjenis": [jenis.value for jenis in idjenis],
            "tahun": tahun,
            "CSRFToken": get_csrf(),
            "Authorization": get_token(),
        },
    )
    response.raise_for_status()
    json = response.json()
    data = [
        {
            "p_id": parse_p_id(html_judul),
            "jenis": jenis,
            "nomor": nomor,
            "tahun": tahun,
            "judul": parse_judul(html_judul),
            "unduh": unduh,
        }
        for [_, jenis, nomor, tahun, html_judul, unduh] in json["data"]
    ]
    return data


def view_produk_hukum(p_id: str):
    response = session.get(
        f"https://jdih.setneg.go.id/front/Peraturan/ajaxview?id={p_id}"
    )
    response.raise_for_status()
    return response.json()


def download_produk_hukum(p_id: str, basename: str):
    response = session.post(
        f"https://jdih.setneg.go.id/downloadFile/{basename}",
        data={"CSRFToken": get_csrf(), "f": p_id, "ts": basename},
    )
    response.raise_for_status()
    return response.content
