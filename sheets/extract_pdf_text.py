
import sys

try:
    import pypdf
    reader_cls = pypdf.PdfReader
except ImportError:
    try:
        import PyPDF2
        reader_cls = PyPDF2.PdfReader
    except ImportError:
        print("Error: neither pypdf nor PyPDF2 is installed.")
        sys.exit(1)

def extract_text(pdf_path):
    try:
        reader = reader_cls(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_pdf_text.py <pdf_path>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    text = extract_text(pdf_path)
    print(text)
