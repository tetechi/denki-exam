import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\20230528_co_second_q01.pdf"
out_dir = base + r"\r5kami_images"
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

# idx=4 (page5): Q1, Q4, Q5
print("idx=4...")
crop(4, 0.08, 0.27, 'q01.png')
crop(4, 0.46, 0.66, 'q04.png')
crop(4, 0.66, 0.99, 'q05.png')

# idx=5 (page6): Q6, Q7, Q9
print("idx=5...")
crop(5, 0.02, 0.28, 'q06.png')
crop(5, 0.28, 0.57, 'q07.png')
crop(5, 0.57, 0.99, 'q09.png')

# idx=6 (page7): Q10
print("idx=6...")
crop(6, 0.02, 0.42, 'q10.png')

# idx=7 (page8): Q16, Q17, Q18
print("idx=7...")
crop(7, 0.06, 0.28, 'q16.png')
crop(7, 0.275, 0.465, 'q17.png')
crop(7, 0.46, 0.66, 'q18.png')

# idx=8 (page9): Q21
print("idx=8...")
crop(8, 0.02, 0.29, 'q21.png')

# idx=9 (page10): Q27
print("idx=9...")
crop(9, 0.02, 0.42, 'q27.png')

# idx=11 (page12): Q41-Q45
print("idx=11...")
crop(11, 0.02, 0.22, 'q41.png')
crop(11, 0.21, 0.42, 'q42.png')
crop(11, 0.41, 0.60, 'q43.png')
crop(11, 0.59, 0.79, 'q44.png')
crop(11, 0.78, 0.99, 'q45.png')

# idx=12 (page13): Q46-Q50
print("idx=12...")
crop(12, 0.02, 0.22, 'q46.png')
crop(12, 0.21, 0.42, 'q47.png')
crop(12, 0.41, 0.60, 'q48.png')
crop(12, 0.59, 0.78, 'q49.png')
crop(12, 0.77, 0.99, 'q50.png')

# idx=14 (page15): 配線図
print("idx=14...")
crop(14, 0.01, 0.99, 'wiring_diagram.png')

print("Done!")
