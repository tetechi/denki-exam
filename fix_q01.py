import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
out_dir = base + r"\r7shimo_images"
pdf = pdfium.PdfDocument(base + r"\list\20251026_co_second_q01.pdf")

page = pdf[4]
bm = page.render(scale=2)
img = bm.to_pil()
w, h = img.size
print(f"Page size: {w}x{h}")

for y1 in [0.28, 0.32, 0.36, 0.40]:
    name = f"q01_try{int(y1*100)}.png"
    cropped = img.crop((0, int(h * 0.04), w, int(h * y1)))
    cropped.save(os.path.join(out_dir, name))
    print(f"Saved {name} ({cropped.size})")
