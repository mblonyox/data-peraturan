from html import escape

from marker.converters.ocr import OCRConverter
from marker.models import create_model_dict


def convert(pdf_path_bytes: str) -> str:
    converter = OCRConverter(
        artifact_dict=create_model_dict(),
    )
    ocr_json_output = converter(pdf_path_bytes)
    html_output = ""
    for page in ocr_json_output.children:
        if page.children is None:
            continue
        for line in page.children:
            html_output += escape(line.html)
    return html_output
