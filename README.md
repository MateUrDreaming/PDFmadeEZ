# PDF to HTML Converter
A Python-based application that converts PDF documents to HTML format using the PyMuPDF library. This tool extracts text and images from each page of the PDF, formats them into structured HTML, and preserves the layout as closely as possible.

## Motivation 
Extracting text from PDFs while retaining formatting can be a frustrating experience. This project was created to simplify that process, providing a straightforward Python application that converts PDF documents into HTML format, making the content easier to work with and present.

## Features
* Text Extraction: Efficiently extracts text from PDF documents while maintaining the original layout.
* Block Handling: Groups closely spaced text blocks to reduce unwanted line breaks and ensure a more readable output.
* Color Alternation: Alternates text color between red and green for visual distinction of content blocks.
* Image Support: Extracts images and encodes them in base64 format for seamless integration into the HTML output.
* Page Separation: Each page of the PDF is represented as a separate <div> in the HTML with a corresponding header and horizontal rule.
  
## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/pdf-to-html-converter.git
    ```
2.  Navigate to the project directory:
    ```bash
     cd pdf-to-html-converter
     ```
3.  Install required dependencies: 
     ```bash
     pip install pymupdf
     ```
## Usage
Run the application from the command line:
```bash
python pdf_to_html.py <input_pdf> <output_html>
```
### Example 
```bash
python pdf_to_html.py example.pdf output.html
```
