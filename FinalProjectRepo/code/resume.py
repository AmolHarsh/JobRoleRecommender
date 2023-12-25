# Note: This code is currently not in used. But we will be using this code in future methods, for scraping
# different sections of the resume.

# Importing the necessary libraries

import PyPDF2
import re

# Defining a function to read the pdf
def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        data = []
        for page in reader.pages:
            text = page.extract_text()
            if text:
                data.extend(text.split('\n'))  
    return data

# File paths for pdf file
pdf_file_path = 'test-resume.pdf'  

# File path to store the parsed-extrated text
output_file_path = 'parsed_resume.txt'

# Process the PDF and extract text
pdf_data = read_pdf(pdf_file_path)

# Write the data to a file, each item on a new line
with open(output_file_path, 'w') as file:
    for line in pdf_data:
        file.write(line + '\n')

print(f"Data was saved to {output_file_path}")

