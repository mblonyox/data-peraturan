import pathlib
import kreuzberg

config = kreuzberg.ExtractionConfig(
    ocr=kreuzberg.OcrConfig(
        language="eng+ind",
        backend="paddleocr",
        paddle_ocr_config=kreuzberg.PaddleOcrConfig(
            model_tier="server"
        ),
    ),
)


def convert(p: pathlib.Path) -> str:
    result = kreuzberg.extract_file_sync(p, mime_type="application/pdf", config=config)
    return result.content
