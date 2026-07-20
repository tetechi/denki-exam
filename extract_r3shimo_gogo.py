import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\220211024_co_second_q02.pdf"
out_dir = base + r"\r3shimo_gogo_images"
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

print("Page 5 idx=4 (Q1, Q5)...")
crop(4, 0.03, 0.22, 'q01.png')   # 問1 回路図
crop(4, 0.72, 0.99, 'q05.png')   # 問5 三相3線式回路

print("Page 6 idx=5 (Q6, Q7, Q9)...")
crop(5, 0.01, 0.28, 'q06.png')   # 問6 単相2線式回路
crop(5, 0.28, 0.57, 'q07.png')   # 問7 単相3線式回路
crop(5, 0.73, 0.99, 'q09.png')   # 問9 幹線分岐回路

print("Page 7 idx=6 (Q10, Q16)...")
crop(6, 0.01, 0.26, 'q10.png')   # 問10 分岐回路組合せ
crop(6, 0.75, 0.99, 'q16.png')   # 問16 写真（PF管カップリング）

print("Page 8 idx=7 (Q17, Q18)...")
crop(7, 0.01, 0.36, 'q17.png')   # 問17 写真（安定器）
crop(7, 0.36, 0.66, 'q18.png')   # 問18 写真（工具）

print("Page 11 idx=10 (Q39, Q40)...")
crop(10, 0.81, 0.92, 'q39.png')  # 問39 コンセント極配置（横長ストリップ）
crop(10, 0.92, 0.99, 'q40.png')  # 問40 モータブレーカ図記号（横長ストリップ）

print("Page 12 idx=11 (Q41-Q45 写真)...")
crop(11, 0.01, 0.25, 'q41.png')  # 問41 接地抵抗計
crop(11, 0.25, 0.47, 'q42.png')  # 問42 リングスリーブ種類・個数
crop(11, 0.47, 0.68, 'q43.png')  # 問43 差込形コネクタ種類・個数
crop(11, 0.68, 0.83, 'q44.png')  # 問44 点滅器取付材料
crop(11, 0.83, 0.99, 'q45.png')  # 問45 コンセント種類

print("Page 13 idx=12 (Q46-Q50 写真)...")
crop(12, 0.01, 0.23, 'q46.png')  # 問46 ケーブル種類
crop(12, 0.23, 0.46, 'q47.png')  # 問47 トラフ
crop(12, 0.46, 0.67, 'q48.png')  # 問48 機器の図記号
crop(12, 0.67, 0.83, 'q49.png')  # 問49 金属管支持材料
crop(12, 0.83, 0.99, 'q50.png')  # 問50 使用されることのない工具

print("Page 15 idx=14 (配線図)...")
crop(14, 0.01, 0.99, 'wiring_diagram.png')

print("Done!")
