# %% Run
from setneg import api

response = api.produk_hukum(idjenis=[api.IdJenis.UU], tahun=[2024])
response
