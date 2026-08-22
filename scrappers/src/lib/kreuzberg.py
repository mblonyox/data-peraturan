from kreuzberg import ExtractionConfig, OcrConfig, extract_bytes_sync

config = ExtractionConfig(ocr=OcrConfig(backend="easyocr", language="id"))


def convert(data: bytes) -> str:
    result = extract_bytes_sync(data, mime_type="application/pdf", config=config)
    return result.content
