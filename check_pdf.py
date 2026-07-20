import pypdfium2 as pdfium

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam\list"
a_pdf = pdfium.PdfDocument(base + r"\20251026_co_second_a01.pdf")
q_pdf = pdfium.PdfDocument(base + r"\20251026_co_second_q01.pdf")
print(f"Answer PDF pages: {len(a_pdf)}")
print(f"Question PDF pages: {len(q_pdf)}")
