import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\20220529_co_second_q02.pdf"
out_dir = base + r"\r4kami_gogo_images"
os.makedirs(out_dir, exist_ok=True)

pdf = pdfium.PdfDocument(pdf_path)

def crop(page_idx, y0, y1, name):
    page = pdf[page_idx]
    bm = page.render(scale=2)
    img = bm.to_pil()
    w, h = img.size
    cropped = img.crop((0, int(h * y0), w, int(h * y1)))
    cropped.save(os.path.join(out_dir, name))
    print(f"  {name}  ({y0:.2f}-{y1:.2f})")

# idx=4 (page5): Q1, Q5
print("idx=4...")
crop(4, 0.10, 0.31, 'q01.png')
crop(4, 0.77, 0.99, 'q05.png')

# idx=5 (page6): Q6, Q7, Q9
print("idx=5...")
crop(5, 0.02, 0.31, 'q06.png')
crop(5, 0.31, 0.61, 'q07.png')
crop(5, 0.77, 0.99, 'q09.png')

# idx=6 (page7): Q10
print("idx=6...")
crop(6, 0.02, 0.25, 'q10.png')

# idx=7 (page8): Q16, Q17, Q18, Q20
print("idx=7...")
crop(7, 0.02, 0.27, 'q16.png')
crop(7, 0.27, 0.50, 'q17.png')
crop(7, 0.50, 0.74, 'q18.png')
crop(7, 0.84, 0.99, 'q20.png')

# idx=9 (page10): Q26, Q27
print("idx=9...")
crop(9, 0.02, 0.35, 'q26.png')
crop(9, 0.35, 0.58, 'q27.png')

# idx=11 (page12): Q41-Q45
print("idx=11...")
crop(11, 0.01, 0.20, 'q41.png')
crop(11, 0.20, 0.40, 'q42.png')
crop(11, 0.40, 0.65, 'q43.png')
crop(11, 0.65, 0.82, 'q44.png')
crop(11, 0.82, 0.99, 'q45.png')

# idx=12 (page13): Q46-Q50
print("idx=12...")
crop(12, 0.02, 0.25, 'q46.png')
crop(12, 0.25, 0.48, 'q47.png')
crop(12, 0.48, 0.67, 'q48.png')
crop(12, 0.67, 0.85, 'q49.png')
crop(12, 0.85, 0.99, 'q50.png')

# idx=14 (page15): 配線図
print("idx=14...")
crop(14, 0.01, 0.99, 'wiring_diagram.png')

print("Done!")
