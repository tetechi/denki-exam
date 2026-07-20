import pypdfium2 as pdfium, os
base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf = pdfium.PdfDocument(base + r"\list\20250525_co_second_q01.pdf")
out = base + r"\r7kami_images"
for idx in [4, 6, 8, 10, 12, 14]:
    page = pdf[idx]
    bm = page.render(scale=1)
    img = bm.to_pil()
    img.save(os.path.join(out, f"page{idx+1}_preview.png"))
    print(f"  page{idx+1}_preview.png {img.size}")
