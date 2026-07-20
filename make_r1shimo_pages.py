import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\20191006_co_second_q01.pdf"
out_dir = base + r"\r1shimo\pages"
os.makedirs(out_dir, exist_ok=True)

pdf = pdfium.PdfDocument(pdf_path)
for i in range(len(pdf)):
    page = pdf[i]
    bm = page.render(scale=1.5)
    img = bm.to_pil()
    img.save(os.path.join(out_dir, f"page_{i+1:02d}.png"))
    print(f"  page_{i+1:02d}.png")
print("Done!")
