#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install pymupdf')


# In[2]:


import fitz  # PyMuPDF
import os


# In[3]:


import os
os.listdir()

pdf_path = "Generative AI in Healthcare.pdf"
doc = fitz.open(pdf_path)



# In[4]:


#1 PyMuPDF is a Python library used to work with PDF files.With PyMuPDF, we can open PDF documents, read text, and save the text to a file.
# It is often used for document analysis, research papers, and healthcare documents.



#2 Advantages of PyMuPDF

#Easy to use with simple syntax
#Works well with large PDF files
#No internet connection required
#Useful for medical and research document processing


#2 Limitations of PyMuPDF

#Does not automatically perform OCR on scanned images
#Formatting of extracted text may not be perfect
#Requires correct file paths
#Works best with digital (not scanned) PDFs


#3 Step 1: Install and Import Library

# If not installed, run this in terminal:
# pip install pymupdf

import fitz  # PyMuPDF


# Step 2: Load the PDF File
#Replace the filename with any PDF you want
pdf_path = "Generative AI in Healthcare.pdf"

doc = fitz.open(pdf_path)

print("PDF successfully opened.")
print("Total number of pages:", doc.page_count)


# Step 3: Extract Text from All Pages

full_text = ""

for page_number in range(doc.page_count):
    page = doc.load_page(page_number)
    text = page.get_text()
    full_text += f"\n--- Page {page_number + 1} ---\n"
    full_text += text


# Step 4: Save Extracted Text to a File

output_file = "extracted_text.txt"

with open(output_file, "w", encoding="utf-8") as file:
    file.write(full_text)

print("Text extraction completed.")
print("Extracted text saved to:", output_file)

# Step 5: Display Sample Output

print("\nSample Extracted Text (First 1000 characters):\n")
print(full_text[:1000])


