import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
out_dir = base + r"\r7shimo_images"
pdf = pdfium.PdfDocument(base + r"\list\20251026_co_second_q01.pdf")
page = pdf[4]
bm = page.render(scale=2)
img = bm.to_pil()
w, h = img.size
cropped = img.crop((0, int(h * 0.04), w, int(h * 0.32)))
cropped.save(os.path.join(out_dir, "q01.png"))
print("q01.png saved", cropped.size)
