import pdfplumber
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\20251026_co_second_q01.pdf"
out_path = base + r"\r7shimo_text.txt"

with pdfplumber.open(pdf_path) as pdf, open(out_path, 'w', encoding='utf-8') as f:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text:
            f.write(f"\n===== PAGE {i+1} =====\n")
            f.write(text)
            f.write("\n")

print(f"Written to {out_path}")
