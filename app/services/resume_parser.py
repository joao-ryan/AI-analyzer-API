import pdfplumber

def extract_text_from_pdf(file):
    """Extrai texto de um arquivo PDF usando pdfplumber."""
    with pdfplumber.open(file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text
