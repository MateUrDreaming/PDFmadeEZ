import sys
import fitz  
import re

# Simple regex method that removes all whitespace and line breaks
def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def extract_text_blocks_from_pdf(pdf_path):
    pages = []
    document = fitz.open(pdf_path)
    
    for page_number in range(len(document)):
        page = document.load_page(page_number)
        
        text_blocks = page.get_text("blocks")  
        page_blocks = []
        for block in text_blocks:
            try:
                x0, y0, x1, y1, text, block_index, another_index = block
                cleaned_text = clean_text(text)
                if cleaned_text:  # Only print non-empty cleaned text blocks
                    page_blocks.append(cleaned_text)
                    
            except ValueError:
                print("Unexpected block structure")
        page_blocks.append(f"\n-----END OF PAGE {page_number}  ----\n")
        pages.append(page_blocks)
    document.close()
    return pages

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <pdf_path>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    pages = extract_text_blocks_from_pdf(pdf_path)
    for lst in pages: 
        for block in lst: 
            print(block)  