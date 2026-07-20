import pypdfium2 as pdfium
import os

pdf = pdfium.PdfDocument(r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam\list\20231029_co_second_q02.pdf")
out_dir = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam\r5shimo_gogo_pages"
os.makedirs(out_dir, exist_ok=True)

for i in range(len(pdf)):
    page = pdf[i]
    bm = page.render(scale=2)
    img = bm.to_pil()
    img.save(os.path.join(out_dir, f"page_{i+1:02d}.png"))
    print(f"Saved page_{i+1:02d}.png")

print("Done!")
