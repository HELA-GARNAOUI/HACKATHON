from PyPDF2 import PdfReader

def extract_text(file):
    filename = file.filename.lower()
    if filename.endswith('.txt'):
        return file.read().decode('utf-8')
    elif filename.endswith('.pdf'):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    return ""
