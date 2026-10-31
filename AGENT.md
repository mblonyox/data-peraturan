# Panduan Agent: Struktur & Standardisasi Dokumen Fulltext Peraturan

Dokumen ini adalah panduan resmi bagi agen (AI/LLM) dan kontributor dalam mengelola, merapikan, memformat, dan memvalidasi file naskah lengkap peraturan perundang-undangan (`fulltext.md`) di repositori **data-peraturan**.

---

## 1. Arsitektur & Struktur Direktori

Setiap peraturan perundang-undangan disimpan dalam struktur direktori hierarkis berbasis jenis dokumen, tahun pengundangan, dan nomor urut peraturan:

```text
data-peraturan/
├── <jenis>/
│   └── <tahun>/
│       └── <nomor>/
│           ├── fulltext.md     # Naskah lengkap peraturan (Markdown standar bersih)
│           └── thumbnail.png    # Gambar sampul / halaman pertama dari PDF asli
├── json-schema.json            # Skema validasi metadata dokumen
├── database.sqlite             # Basis data metadata & relasi peraturan
├── file-server.sh              # Static server berbasis Deno untuk menyajikan dokumen
└── scrappers/                  # Script scraping (JDIH Setneg) & ekstraksi OCR (Kreuzberg)
```

### Jenis Dokumen yang Didukung
- `uu`: Undang-Undang
- `perpu`: Peraturan Pemerintah Pengganti Undang-Undang
- `pp`: Peraturan Pemerintah
- `perpres`: Peraturan Presiden
- `permenkeu`: Peraturan Menteri Keuangan

> **Catatan:** File `fulltext.md` tidak menggunakan frontmatter YAML. Metadata disimpan terpisah di `database.sqlite` dan `scrappers/_tmp/peraturan_<tahun>.csv`. File `fulltext.md` murni berisi teks naskah hukum dalam format Markdown yang rapi dan terstruktur.

---

## 2. Anatomi Struktur Dokumen `fulltext.md`

Struktur naskah dalam `fulltext.md` merefleksikan kaidah penyusunan peraturan perundang-undangan resmi di Indonesia (UU No. 12 Tahun 2011 jo. UU No. 13 Tahun 2022) yang diterjemahkan ke dalam elemen Markdown yang konsisten.

```
┌────────────────────────────────────────────────────────┐
│ 1. JUDUL & PEMBUKAAN (UPPERCASE)                       │
│    UNDANG-UNDANG REPUBLIK INDONESIA                    │
│    NOMOR ... TAHUN ...                                 │
│    TENTANG ...                                         │
│    DENGAN RAHMAT TUHAN YANG MAHA ESA                   │
│    PRESIDEN REPUBLIK INDONESIA,                        │
├────────────────────────────────────────────────────────┤
│ 2. KONSIDERANS (Menimbang) & DASAR HUKUM (Mengingat)   │
├────────────────────────────────────────────────────────┤
│ 3. PERSETUJUAN (Khusus UU) & DIKTUM                    │
│    MEMUTUSKAN:                                         │
│    Menetapkan : ...                                    │
├────────────────────────────────────────────────────────┤
│ 4. BATANG TUBUH (BUKU -> BAB -> Bagian -> Pasal)       │
│    - Rincian Butir (Indentasi 2 & 4 spasi)             │
│    - Container `:::` untuk Peraturan Perubahan         │
├────────────────────────────────────────────────────────┤
│ 5. PENUTUP                                             │
│    - Rumusan perintah pengundangan                     │
│    - Penetapan / Pengesahan (&nbsp; &nbsp; ttd.)       │
│    - Pengundangan (ttd.)                               │
│    - Lembaran Negara & Tambahan Lembaran Negara        │
├────────────────────────────────────────────────────────┤
│ 6. PENJELASAN (Opsional, atau di dalam <!-- ... -->)   │
├────────────────────────────────────────────────────────┤
│ 7. LAMPIRAN (Opsional)                                 │
└────────────────────────────────────────────────────────┘
```

---

## 3. Aturan Pemformatan Rinci Tiap Bagian

### 3.1 Judul dan Pembukaan (Header & Preamble)
- Semua teks judul ditulis dalam **HURUF KAPITAL PENUH (UPPERCASE)** tanpa heading markdown (`#`).
- Setiap bagian dipisah baris:
  1. Jenis & Lembaga Negara (`UNDANG-UNDANG REPUBLIK INDONESIA`)
  2. Nomor dan Tahun (`NOMOR 1 TAHUN 2024`)
  3. Kata `TENTANG`
  4. Judul Peraturan (dapat dipecah ke baris baru jika panjang)
  5. 1 baris kosong
  6. Frasa `DENGAN RAHMAT TUHAN YANG MAHA ESA`
  7. 1 baris kosong
  8. Jabatan Pembentuk Peraturan diakhiri tanda koma: `PRESIDEN REPUBLIK INDONESIA,`

Contoh:
```markdown
UNDANG-UNDANG REPUBLIK INDONESIA
NOMOR 1 TAHUN 2024
TENTANG
PERUBAHAN KEDUA ATAS UNDANG-UNDANG NOMOR 11 TAHUN 2008
TENTANG INFORMASI DAN TRANSAKSI ELEKTRONIK

DENGAN RAHMAT TUHAN YANG MAHA ESA

PRESIDEN REPUBLIK INDONESIA,
```

### 3.2 Konsiderans (Menimbang) dan Dasar Hukum (Mengingat)
- Judul bagian diawali `Menimbang :` dan `Mengingat :` pada baris tersendiri.
- Setiap butir pertimbangan diawali huruf abjad kecil `a.`, `b.`, dst. Kalimat diawali dengan `bahwa ...;`.
- Setiap butir dasar hukum diawali angka `1.`, `2.`, dst. (atau berupa satu kalimat utuh jika hanya ada satu dasar hukum).
- Antara blok `Menimbang` dan `Mengingat` dipisahkan oleh 1 baris kosong.

Contoh:
```markdown
Menimbang :
a. bahwa untuk menjaga ruang digital Indonesia yang bersih, sehat, beretika, produktif, dan berkeadilan, perlu diatur pemanfaatan Teknologi Informasi;
b. bahwa berdasarkan pertimbangan sebagaimana dimaksud dalam huruf a, perlu membentuk Undang-Undang...;

Mengingat :
1. Pasal 5 ayat (1) dan Pasal 20 Undang-Undang Dasar Negara Republik Indonesia Tahun 1945;
2. Undang-Undang Nomor 11 Tahun 2008 tentang Informasi dan Transaksi Elektronik...;
```

### 3.3 Persetujuan Bersama & Diktum
- Khusus untuk **Undang-Undang (UU)**, cantumkan frasa persetujuan:
```markdown
Dengan Persetujuan Bersama
DEWAN PERWAKILAN RAKYAT REPUBLIK INDONESIA
dan
PRESIDEN REPUBLIK INDONESIA
```
*(Untuk produk hukum era lampau, sesuaikan teks persetujuan aslinya, misal: `Dengan Persetujuan DEWAN PERWAKILAN RAKYAT`).*

- Kata `MEMUTUSKAN:` ditulis kapital penuh dengan tanda titik dua di baris tersendiri.
- Diikuti `Menetapkan :` di baris berikutnya.
- Diikuti judul penetapan (dalam huruf kapital penuh), misalnya: `UNDANG-UNDANG TENTANG ...` atau `PERATURAN PEMERINTAH TENTANG ...`.

Contoh:
```markdown
MEMUTUSKAN:
Menetapkan :
UNDANG-UNDANG TENTANG PERUBAHAN KEDUA ATAS UNDANG-UNDANG NOMOR 11 TAHUN 2008 TENTANG INFORMASI DAN TRANSAKSI ELEKTRONIK.
```

---

### 3.4 Batang Tubuh (Struktur Hirarki Peraturan)

Hirarki peraturan dari yang tertinggi hingga terendah:

1. **BUKU** (bila ada, misal KUHP):
   ```markdown
   BUKU KESATU
   ATURAN UMUM
   ```
2. **BAB**:
   - Angka Romawi, kapital penuh di baris pertama.
   - Nama BAB kapital penuh di baris berikutnya.
   - **Dilarang** menyatukan nomor bab dan nama bab dalam 1 baris (misal: `BAB I KETENTUAN UMUM` adalah format salah dari OCR).
   ```markdown
   BAB I
   KETENTUAN UMUM
   ```
3. **Bagian**:
   - Ditulis dalam *Title Case*.
   - Kata bilangan urut dieja (`Bagian Kesatu`, `Bagian Kedua`).
   ```markdown
   Bagian Kesatu
   Menurut Tempat
   ```
4. **Paragraf**:
   - Ditulis dalam *Title Case* dengan angka arab (`Paragraf 1`, `Paragraf 2`).
   ```markdown
   Paragraf 1
   Umum
   ```
5. **Pasal**:
   - Format: `Pasal 1`, `Pasal 2`, dst. (huruf P kapital, spasi, angka).
   - Selalu dipisahkan oleh 1 baris kosong sebelum dan sesudahnya.
   - Pada peraturan perubahan, gunakan angka Romawi: `Pasal I`, `Pasal II`.
6. **Ayat**:
   - Menggunakan tanda kurung: `(1)`, `(2)`, dst. di awal baris.
   - Jika pasal tidak memiliki pembagian ayat (hanya satu substansi tunggal), tulis langsung teksnya tanpa nomor `(1)`.
7. **Rincian Huruf dan Angka (Indentasi)**:
   - Rincian huruf (`a.`, `b.`) di bawah ayat/pasal diindentasi **2 spasi**.
   - Rincian angka (`1.`, `2.`) di bawah huruf diindentasi **4 spasi**.
   - Butir turunan berikutnya (`1)`, `a)`) diindentasi **6 spasi**.

Contoh format Batang Tubuh:
```markdown
BAB II
ASAS DAN TUJUAN

Pasal 2
Pelaku usaha di Indonesia dalam menjalankan kegiatan usahanya berasaskan demokrasi ekonomi.

Pasal 3
(1) Penyelenggaraan Sekolah Rakyat bertujuan untuk:
  a. memenuhi hak pendidikan bagi masyarakat miskin; dan
  b. memberikan layanan pendidikan yang mengedepankan karakter:
    1. integritas;
    2. kemandirian; dan
    3. gotong royong.
(2) Penyelenggaraan sebagaimana dimaksud pada ayat (1) dilaksanakan oleh Pemerintah.
```

---

### 3.5 Format Peraturan Perubahan (Container `:::`)

Untuk peraturan yang sifatnya mengubah peraturan sebelumnya (amendment), naskah pasal yang diubah/disisipkan harus dibungkus dengan container markdown tiga titik dua (`:::`):

```markdown
Pasal I
Beberapa ketentuan dalam Undang-Undang Nomor 11 Tahun 2008 diubah sebagai berikut:

1. Ketentuan Pasal 5 diubah sehingga berbunyi sebagai berikut:

:::
Pasal 5
(1) Informasi Elektronik dan/atau Dokumen Elektronik merupakan alat bukti hukum yang sah.
(2) Ketentuan sebagaimana dimaksud pada ayat (1) berlaku sesuai dengan hukum acara.
:::

2. Di antara Pasal 27 dan Pasal 28 disisipkan 2 (dua) pasal, yakni Pasal 27A dan Pasal 27B sehingga berbunyi sebagai berikut:

:::
Pasal 27A
Setiap Orang yang dengan sengaja menyerang kehormatan... dipidana...

Pasal 27B
(1) Setiap Orang yang dengan sengaja...
(2) Tindak pidana sebagaimana dimaksud...
:::

Pasal II
Undang-Undang ini mulai berlaku pada tanggal diundangkan.
```

**Alasan Penggunaan `:::`:**
Blok container `:::` memisahkan teks instruksi pengubah (misal: *"Ketentuan Pasal 5 diubah..."*) dengan teks hukum dari pasal itu sendiri, sehingga memudahkan parser web merender bagian tersebut sebagai kartu/kutipan pasal yang independen.

---

### 3.6 Konvensi Tautan Silang (Cross-References / Hyperlinks)

Jika naskah mengacu pada pasal atau ayat lain di dalam undang-undang tersebut (atau undang-undang terkait), gunakan link markdown relatif:

- **Format Pola URL**: `/<jenis>/<tahun>/<nomor>/pasal-<nomor>[/ayat-<nomor>]`
- **Slug**: Semua huruf kecil (lowercase), dipisahkan tanda strip (`-`).

Contoh tautan:
```markdown
Ketentuan sebagaimana dimaksud dalam [Pasal 1 ayat (1)](/uu/2023/1/pasal-1/ayat-1) tidak mengurangi...
sebagaimana dimaksud pada [ayat (1)](/uu/2023/1/pasal-2/ayat-1) berlaku dalam tempat...
sebagaimana dimaksud dalam [Pasal 608](/uu/2023/1/pasal-608)...
```

---

### 3.7 Bagian Penutup (Closing Section)

Bagian penutup memiliki struktur baku yang memuat perintah pengundangan, penetapan/pengesahan, pengundangan, serta nomor publikasi Lembaran Negara.

**Aturan Penulisan:**
1. **Rumusan Pengundangan:**
   `Agar setiap orang mengetahuinya, memerintahkan pengundangan [Jenis Peraturan] ini dengan penempatannya dalam Lembaran Negara Republik Indonesia.`
2. **Pemisah Blok:** Gunakan tag `<br/>` dengan baris kosong sebelum dan sesudahnya.
3. **Blok Pengesahan / Penetapan (Sisi Kanan / Indentasi):**
   - Tiap baris diawali dengan 4 entitas spasi HTML: `&nbsp;&nbsp;&nbsp;&nbsp;`
   - Tiap baris diakhiri dengan **2 spasi markdown newline** (`  `).
   - Memuat tempat & tanggal penetapan, jabatan, tanda tangan (`ttd.`), dan nama pejabat.
4. **Blok Pengundangan (Sisi Kiri):**
   - Tanpa `&nbsp;`.
   - Tiap baris diakhiri dengan 2 spasi markdown newline (`  `).
   - Memuat tempat & tanggal pengundangan, menteri/pejabat pengundang, `ttd.`, dan nama pejabat.
5. **Blok Lembaran Negara:**
   - Ditulis huruf kapital penuh: `LEMBARAN NEGARA REPUBLIK INDONESIA TAHUN ... NOMOR ...`
   - Jika ada tambahan lembaran negara: `TAMBAHAN LEMBARAN NEGARA REPUBLIK INDONESIA NOMOR ...`

Contoh Penutup:
```markdown
Agar setiap orang mengetahuinya, memerintahkan pengundangan Undang-Undang ini dengan penempatannya dalam Lembaran Negara Republik Indonesia.

<br/>

&nbsp;&nbsp;&nbsp;&nbsp;Disahkan di Jakarta  
&nbsp;&nbsp;&nbsp;&nbsp;pada tanggal 2 Januari 2024  
&nbsp;&nbsp;&nbsp;&nbsp;PRESIDEN REPUBLIK INDONESIA,  
&nbsp;&nbsp;&nbsp;&nbsp;ttd.  
&nbsp;&nbsp;&nbsp;&nbsp;JOKO WIDODO

<br/>

Diundangkan di Jakarta  
pada tanggal 2 Januari 2024  
MENTERI SEKRETARIS NEGARA  
REPUBLIK INDONESIA,  
ttd.  
PRATIKNO

<br/>

LEMBARAN NEGARA REPUBLIK INDONESIA TAHUN 2024 NOMOR 1
```

---

### 3.8 Penjelasan dan Lampiran

1. **Bagian Penjelasan**:
   - Diletakkan setelah blok Lembaran Negara.
   - Judul diawali `PENJELASAN ATAS [NAMA PERATURAN]`.
   - Terdiri dari:
     - `I. UMUM`
     - `II. PASAL DEMI PASAL`
     - Penjelasan tiap pasal diawali `Pasal X` dan baris berikutnya `Cukup jelas.` atau teks penjelasan pasal/ayat.
   - **Komentar HTML (`<!-- ... -->`)**: Jika naskah Penjelasan masih berantakan dari OCR dan belum sempat dirapikan secara manual, lingkupi seluruh bagian penjelasan dalam komentar HTML `<!--` dan `-->` agar tidak merusak rendering frontend.

2. **Bagian Lampiran**:
   - Diawali dengan `LAMPIRAN [NAMA PERATURAN]`.
   - Struktur tabel disajikan dalam tabel Markdown (`| kolom 1 | kolom 2 |`).

---

## 4. Pedoman Pembersihan Artefak OCR (OCR Cleanup)

Dokumen mentah hasil konversi PDF via Kreuzberg/PaddleOCR mengandung banyak noise pemindaian. Saat merapikan dokumen, aturan berikut **wajib** dipatuhi:

### 4.1 Elemen yang WAJIB Dihapus:
- **Tanda Salinan / Header Halaman:**
  - Hapus kata `SALINAN`, `PRESIDEN REPUBLIK INDONESIA` yang muncul di tengah teks sebagai header halaman.
  - Hapus nomor halaman PDF: `- 2 -`, `- 15 -`, `-t64-`.
- **Running Head / Kata Sambung Antar-Halaman:**
  - Teks seperti `Pasal 1135. . .`, `10. Kementerian . . .`, `BABI...`, `Agar setiap...`.
- **Kode Keamanan Kertas / Nomor Registrasi:**
  - `SK No 270514 A`, `SK No248D4 A`, `SK No 065109 A`.
- **Stempel Autentikasi / Pengesahan Salinan di Akhir:**
  - Hapus teks stempel legalisir Setneg seperti:
    ```text
    Salinan sesuai dengan aslinya
    KEMENTERIAN SEKRETARIAT NEGARA REPUBLIK INDONESIA
    Perundang-undangan dan Administrasi Hukum,
    ttd
    Silvanna Djaman
    ```
- **Karakter liar OCR:**
  - Hapus artefak seperti `ffi`, `^`, `#p`, `. 'ir . \,' * r "`, tanda kutip cacat, dsb.

### 4.2 Kesalahan Ketik Tipikal OCR yang Harus Diperbaiki:
| Teks OCR Salah | Perbaikan yang Benar | Keterangan |
| :--- | :--- | :--- |
| `IO3`, `2OO8`, `2O22` | `103`, `2008`, `2022` | Huruf `O`/`o` terbaca padahal angka `0` |
| `Pasal I`, `(2l`, `(3t` | `Pasal 1`, `(2)`, `(3)` | Huruf `I`/`l`/`t` tertukar angka `1` atau kurung tutup `)` |
| `Pasal Ll26` | `Pasal 1126` | `Ll` terbaca padahal `11` |
| `Pasal59`, `Pasal62` | `Pasal 59`, `Pasal 62` | Spasi hilang antara kata Pasal dan nomor |
| `danlatau` | `dan/atau` | Tanda garis miring `/` terbaca huruf `l` |
| `I*mbaran`, `Irmbaran` | `Lembaran` | Kerusakan huruf L pada Lembaran Negara |
| `kuratil` | `kuratif` | Typo huruf pada istilah hukum |
| `bertanggungiawab` | `bertanggung jawab` | Spasi dan huruf i/j |

### 4.3 Kaidah Spasi dan Baris:
- **Hapus baris kosong berulang:** Maksimal 1 baris kosong di antara paragraf atau elemen Markdown.
- **Sambungkan kalimat yang terpenggal:** Jika kalimat terpotong karena ganti halaman atau ganti kolom pada PDF, satukan kembali menjadi satu baris/paragraf utuh.

---

## 5. Checklist Verifikasi untuk Agent

Sebelum menandai pekerjaan pembersihan dokumen selesai, lakukan validasi berikut:

- [ ] **Path File:** Apakah file berada di path yang benar `/<jenis>/<tahun>/<nomor>/fulltext.md`?
- [ ] **Header:** Apakah Judul dalam huruf kapital penuh dan dipisah per baris secara logis?
- [ ] **Konsiderans & Dasar Hukum:** Apakah `Menimbang :` dan `Mengingat :` memiliki pemisah baris dan butir yang rapi?
- [ ] **Diktum:** Apakah `MEMUTUSKAN:` dan `Menetapkan :` sudah sesuai format?
- [ ] **Struktur Bab & Pasal:** Apakah nomor Bab dan Judul Bab berada pada 2 baris terpisah?
- [ ] **Peraturan Perubahan:** Apakah setiap pasal yang diubah/disisipkan dibungkus dengan `:::`?
- [ ] **Indentasi:** Apakah butir huruf berindentasi 2 spasi dan butir angka berindentasi 4 spasi?
- [ ] **Artefak OCR:** Apakah semua nomor halaman (`- 2 -`), kode `SK No...`, running text, dan stempel salinan sudah dibersihkan?
- [ ] **Typo Angka:** Apakah semua angka tahun dan nomor (misal `2OO8` -> `2008`) sudah dikoreksi?
- [ ] **Penutup:** Apakah penutup menggunakan `<br/>`, `&nbsp;&nbsp;&nbsp;&nbsp;` pada penetapan, dan 2 spasi baris baru pada pengundangan?
- [ ] **Whitespace:** Tidak ada baris kosong berulang (double/triple empty lines).
