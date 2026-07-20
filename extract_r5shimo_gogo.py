import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\20231029_co_second_q02.pdf"
out_dir = base + r"\r5shimo_gogo_images"
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

# idx=4: Q1, Q4, Q5
print("idx=4 (Q1,Q4,Q5)...")
crop(4, 0.08, 0.29, 'q01.png')   # Q1 並列回路図（200V, 20Ω/8Ω並列, 30Ω）
crop(4, 0.47, 0.68, 'q04.png')   # Q4 R+X直列回路図（100V, 8Ω, 6Ω）
crop(4, 0.67, 0.99, 'q05.png')   # Q5 三相Y結線回路図（6Ω×3, 20A）

# idx=5: Q6, Q7, Q9
print("idx=5 (Q6,Q7,Q9)...")
crop(5, 0.02, 0.28, 'q06.png')   # Q6 三相3線式回路図（0.15Ω, 10A）
crop(5, 0.25, 0.46, 'q07.png')   # Q7 単相3線式回路図（210/105V, 中性線断線）
crop(5, 0.58, 0.99, 'q09.png')   # Q9 VVR分岐回路（50A, a-b間）

# idx=6: Q10, Q16
print("idx=6 (Q10,Q16)...")
crop(6, 0.02, 0.36, 'q10.png')   # Q10 分岐回路の組合せ（遮断器+コンセント）
crop(6, 0.79, 0.99, 'q16.png')   # Q16 写真（硬質PVC管ソケット）

# idx=7: Q17, Q18
print("idx=7 (Q17,Q18)...")
crop(7, 0.02, 0.27, 'q17.png')   # Q17 写真（リモコン変圧器）
crop(7, 0.25, 0.60, 'q18.png')   # Q18 写真（パイプカッター）

# idx=11: Q41-Q45
print("idx=11 (Q41-Q45)...")
crop(11, 0.02, 0.34, 'q41.png')
crop(11, 0.33, 0.42, 'q42.png')
crop(11, 0.40, 0.59, 'q43.png')
crop(11, 0.57, 0.77, 'q44.png')
crop(11, 0.75, 0.99, 'q45.png')

# idx=12: Q46-Q50
print("idx=12 (Q46-Q50)...")
crop(12, 0.02, 0.21, 'q46.png')
crop(12, 0.20, 0.40, 'q47.png')
crop(12, 0.39, 0.59, 'q48.png')
crop(12, 0.57, 0.79, 'q49.png')
crop(12, 0.77, 0.99, 'q50.png')

# idx=14: 配線図
print("idx=14 (配線図)...")
crop(14, 0.01, 0.99, 'wiring_diagram.png')

print("Done!")
