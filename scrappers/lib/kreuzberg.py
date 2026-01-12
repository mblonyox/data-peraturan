from kreuzberg import ExtractionConfig, OcrConfig, extract_file_sync

config = ExtractionConfig(ocr=OcrConfig(backend="easyocr", language="id"))


def convert(pdf_path: str) -> str:
    result = extract_file_sync(pdf_path, config=config)
    return result.content
