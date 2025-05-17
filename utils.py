# utils.py
import PyPDF2
from io import BytesIO

def extract_text_from_pdf(pdf_bytes):
    """Extract text from PDF using PyPDF2"""
    text = ""
    try:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_bytes))
        
        # Get total number of pages
        num_pages = len(pdf_reader.pages)
        
        # Extract text from each page
        for page_num in range(num_pages):
            # Get the page
            page = pdf_reader.pages[page_num]
            # Extract text
            page_text = page.extract_text()
            if page_text:
                text += f"--- Page {page_num+1} ---\n"
                text += page_text + "\n\n"
        
        return text
    except Exception as e:
        return f"Error extracting text: {str(e)}" 