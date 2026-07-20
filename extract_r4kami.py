import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\20220529_co_second_q01.pdf"
out_dir = base + r"\r4kami_images"
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
crop(4, 0.07, 0.30, 'q01.png')
crop(4, 0.54, 0.76, 'q04.png')
crop(4, 0.76, 0.99, 'q05.png')

# idx=5 (page6): Q6, Q7
print("idx=5...")
crop(5, 0.02, 0.44, 'q06.png')
crop(5, 0.44, 0.88, 'q07.png')

# idx=6 (page7): Q10
print("idx=6...")
crop(6, 0.02, 0.28, 'q10.png')

# idx=7 (page8): Q16, Q17, Q18, Q20
print("idx=7...")
crop(7, 0.02, 0.30, 'q16.png')
crop(7, 0.30, 0.57, 'q17.png')
crop(7, 0.57, 0.83, 'q18.png')
crop(7, 0.83, 0.99, 'q20.png')

# idx=8 (page9): Q21
print("idx=8...")
crop(8, 0.02, 0.28, 'q21.png')

# idx=9 (page10): Q27
print("idx=9...")
crop(9, 0.27, 0.50, 'q27.png')

# idx=10 (page11): Q39, Q40
print("idx=10...")
crop(10, 0.60, 0.76, 'q39.png')
crop(10, 0.76, 0.99, 'q40.png')

# idx=11 (page12): Q41-Q45
print("idx=11...")
crop(11, 0.01, 0.20, 'q41.png')
crop(11, 0.20, 0.42, 'q42.png')
crop(11, 0.42, 0.62, 'q43.png')
crop(11, 0.62, 0.81, 'q44.png')
crop(11, 0.81, 0.99, 'q45.png')

# idx=12 (page13): Q46-Q50
print("idx=12...")
crop(12, 0.02, 0.22, 'q46.png')
crop(12, 0.22, 0.42, 'q47.png')
crop(12, 0.42, 0.62, 'q48.png')
crop(12, 0.62, 0.82, 'q49.png')
crop(12, 0.82, 0.99, 'q50.png')

# idx=14 (page15): 配線図
print("idx=14...")
crop(14, 0.01, 0.99, 'wiring_diagram.png')

print("Done!")
