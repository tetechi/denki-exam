import pypdfium2 as pdfium, os
from PIL import Image

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf = pdfium.PdfDocument(base + r"\list\20250525_co_second_q01.pdf")
out = base + r"\r7kami_images"
os.makedirs(out, exist_ok=True)

print(f"Total pages: {len(pdf)}")
# Render key pages at half scale for preview
for idx in [3, 5, 7, 9, 11, 13]:
    page = pdf[idx]
    bm = page.render(scale=1)
    img = bm.to_pil()
    img.save(os.path.join(out, f"page{idx+1}_preview.png"))
    print(f"  page{idx+1}_preview.png {img.size}")
