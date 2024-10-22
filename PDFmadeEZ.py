import sys
import fitz  # pymupdf
import re
import base64

def clean_text(text):
    return re.sub(r'\s+', ' ', text).strip()

def convert_pdf_to_html(input_pdf, output_html):
    document = fitz.open(input_pdf)
    html_content = ""

    # Iterate through each page
    for page_number in range(len(document)):
        page = document.load_page(page_number)
        text_blocks = page.get_text("blocks")
        images = page.get_images(full=True)

        html_content += f"<div><h1><b>Page #{page_number + 1}</b></h1>\n"
        list_items = []
        
        # Process each text block, alternating colors
        for block_index, block in enumerate(text_blocks):
            try:
                x0, y0, x1, y1, text, block_number, another_index = block
                cleaned_text = clean_text(text)
                if cleaned_text and not cleaned_text.isdigit():
                    markers = ['', '', '*', '▪', "•"]
                    if any(char in cleaned_text for char in markers):
                        for marker in markers:
                            while marker in text:
                                text = text.replace(marker, '').strip()
                                list_items.append(f"<li style='color: blue;'>{text}</li>")
                    else:
                        color = "red" if block_index % 2 == 0 else "green"
                        html_content += f'<p style="color: {color};">{cleaned_text}</p>\n'
            except ValueError:
                print("Unexpected block structure")

        if list_items:
            html_content += "<ul>\n" + "\n".join(list_items) + "\n</ul>\n"

        # Process each image and append to the end of the page's content
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = document.extract_image(xref)
            image_bytes = base_image["image"]
            image_base64 = base64.b64encode(image_bytes).decode("utf-8")
            image_format = base_image["ext"]
            html_content += f'<img src="data:image/{image_format};base64,{image_base64}" alt="image_{page_number+1}_{img_index+1}">\n'

        html_content += f"</div>\n<hr>\n"

    document.close()

    with open(output_html, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"Conversion complete! The HTML file is saved as: {output_html}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_to_html.py <input_pdf> <output_html>")
        sys.exit(1)

    input_pdf = sys.argv[1]
    output_html = sys.argv[2]

    convert_pdf_to_html(input_pdf, output_html)
