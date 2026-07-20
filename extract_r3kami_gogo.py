import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\20210530_co_second_q02.pdf"
out_dir = base + r"\r3kami_gogo_images"
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

print("Page 5 idx=4 (Q1, Q4, Q5)...")
crop(4, 0.01, 0.24, 'q01.png')   # 問1 回路図
crop(4, 0.57, 0.77, 'q04.png')   # 問4 並列回路（R+XL）
crop(4, 0.77, 0.99, 'q05.png')   # 問5 三相3線式回路

print("Page 6 idx=5 (Q6, Q7, Q9)...")
crop(5, 0.01, 0.32, 'q06.png')   # 問6 単相2線式回路
crop(5, 0.32, 0.65, 'q07.png')   # 問7 単相3線式回路（断線）
crop(5, 0.79, 0.99, 'q09.png')   # 問9 幹線分岐（VVR）

print("Page 7 idx=6 (Q10)...")
crop(6, 0.01, 0.32, 'q10.png')   # 問10 分岐回路組合せ

print("Page 8 idx=7 (Q16, Q17, Q18)...")
crop(7, 0.01, 0.29, 'q16.png')   # 問16 写真（材料：矢印）
crop(7, 0.29, 0.59, 'q17.png')   # 問17 写真（器具用途）
crop(7, 0.59, 0.80, 'q18.png')   # 問18 写真（工具用途）

print("Page 9 idx=8 (Q21)...")
crop(8, 0.01, 0.40, 'q21.png')   # 問21 スイッチボックス配線図

print("Page 12 idx=11 (Q41-Q45)...")
crop(11, 0.01, 0.22, 'q41.png')  # 問41 写真（分電盤主幹等）
crop(11, 0.22, 0.46, 'q42.png')  # 問42 写真（リングスリーブ種類・個数）
crop(11, 0.46, 0.68, 'q43.png')  # 問43 写真（ポンプ室使用器具）
crop(11, 0.68, 0.83, 'q44.png')  # 問44 写真（ケーブル種類）
crop(11, 0.83, 0.99, 'q45.png')  # 問45 写真（使用されない工具）

print("Page 13 idx=12 (Q46-Q50)...")
crop(12, 0.01, 0.22, 'q46.png')  # 問46 写真（使用されない工具）
crop(12, 0.22, 0.46, 'q47.png')  # 問47 写真（差込形コネクタ）
crop(12, 0.46, 0.67, 'q48.png')  # 問48 写真（リングスリーブ）
crop(12, 0.67, 0.83, 'q49.png')  # 問49 写真（使用コンセント）
crop(12, 0.83, 0.99, 'q50.png')  # 問50 写真（使用されないスイッチ）

print("Page 15 idx=14 (配線図)...")
crop(14, 0.01, 0.99, 'wiring_diagram.png')

print("Done!")
