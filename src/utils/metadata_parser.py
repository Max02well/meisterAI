from pathlib import Path
import re


def extract_metadata(pdf_path: Path):
    filename = pdf_path.stem

    brand = pdf_path.parent.parent.name.capitalize()
    category = pdf_path.parent.name.capitalize()

    engine = "Unknown"

    engine_match = re.search(
        r"(\d\.\dL?_?[A-Za-z0-9]+)",
        filename,
        re.IGNORECASE,
    )

    if engine_match:
        engine = engine_match.group(1).replace("_", " ")

    manual_match = re.search(
        r"SSP[_ ]?(\d+)",
        filename,
        re.IGNORECASE,
    )

    manual = (
        f"VWUSA SSP {manual_match.group(1)}"
        if manual_match
        else filename
    )

    return {
        "brand": brand,
        "model": "Unknown",
        "engine": engine,
        "year": "Unknown",
        "category": category,
        "manual": manual,
        "document": pdf_path.name,
        "source": str(pdf_path),
    }