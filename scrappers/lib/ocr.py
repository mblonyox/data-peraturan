from marker.converters.ocr import OCRConverter
from marker.models import create_model_dict
from marker.output import text_from_rendered


def convert_pdf_to_text(pdf_path: str) -> str:
    converter = OCRConverter(
        artifact_dict=create_model_dict(),
    )
    rendered = converter(pdf_path)
    text, _, images = text_from_rendered(rendered)
    return text
