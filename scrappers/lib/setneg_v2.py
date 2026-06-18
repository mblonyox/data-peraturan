import requests
import enum

session = requests.Session()

class JenisProduk(enum.StrEnum):
  UU = "UU"
  PERPU = "PERPU"
  PP = "PP"
  PERPRES = "PERPRES"
  KEPPRES = "KEPPRES"
  INPRES = "INPRES"
  PERMENSESNEG = "PERMENSESNEG"
  KEPMENSESNEG = "KEPMENSESNEG"

class StatusProduk(enum.StrEnum):
  Semua = ""
  Dicabut = "Dicabut"
  Diubah = "Diubah"
  Mencabut = "Mencabut"
  Mengubah = "Mengubah"
  UjiMateril = "Uji_Materil"

class Terx(enum.StrEnum):
  Semua = "All"
  Terbaru = "Terbaru"
  PalingPopuler = "Terpopuler"

def produkhukum(tentang: str = "", status: StatusProduk = StatusProduk.Semua, terx: Terx = Terx.Semua, jns: list[JenisProduk] = None, thn: list[str] = None, start: int = 0, length: int = 10):
  """
  tentang: String containing keyword(s) to search for in the document title or content.
  status: Status Produk enum (Semua, Dicabut, Diubah, Mencabut, Mengubah, Uji_Materil).
  terx: Terx enum (All, Terbaru, Terpopuler).
  jns: List of JenisProduk enum values.
  thn: List of years (strings).
  start: Starting index for pagination (default: 0).
  length: Number of items per page (default: 10).
  """
  while True:
    json = {
      "jns": [jenis.value for jenis in jns] if jns else [],
      "thn": thn or [],
      "start": start,
      "length": length,
      "p_lihan": "semua",
      "terx": terx.value,
      "status": status.value,
      "tentang": tentang
    }
    response = session.post("https://jdih.setneg.go.id/api/hukumproduk/produkhukum", json=json)
    data = response.json()["data"]
    if len(data) == 0:
      break
    for row in data:
      yield row
    start += length

def detaildata(jns: JenisProduk, no: str, thn: str):
  json = {
    "jns": jns.value,
    "no": no,
    "thn": thn,
    "k": ""
  }
  response = session.post("https://jdih.setneg.go.id/api/hukumproduk/detaildata", json=json)
  return response.json()

def pdf(f: str, fl: str, l: str = "uploads"):
  params = {
    "f": f,
    "fl": fl,
    "l": l
  }
  response = session.get("https://jdih.setneg.go.id/api/hukumproduk/pdf", params=params)
  return response.content 