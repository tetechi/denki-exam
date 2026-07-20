import pdfplumber, sys

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
q_pdf = base + r"\list\20250525_co_second_q01.pdf"
a_pdf = base + r"\list\20250525_co_second_a01.pdf"

with open(base + r"\r7kami_text.txt", "w", encoding="utf-8") as f:
    f.write("=== 問題 ===\n\n")
    with pdfplumber.open(q_pdf) as pdf:
        for i, page in enumerate(pdf.pages):
            f.write(f"--- Page {i+1} ---\n")
            f.write(page.extract_text() or "")
            f.write("\n\n")
    f.write("\n=== 解答 ===\n\n")
    with pdfplumber.open(a_pdf) as pdf:
        for i, page in enumerate(pdf.pages):
            f.write(f"--- Page {i+1} ---\n")
            f.write(page.extract_text() or "")
            f.write("\n\n")

print("Done: r7kami_text.txt")
