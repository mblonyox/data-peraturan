import pathlib
import kreuzberg

config = kreuzberg.ExtractionConfig(
    ocr=kreuzberg.OcrConfig(
        backend="easyocr",
        language="id"
    )
)


def convert(p: pathlib.Path) -> str:
    data = p.read_bytes()
    result = kreuzberg.extract_bytes_sync(data, mime_type="application/pdf", config=config)
    return result.content
