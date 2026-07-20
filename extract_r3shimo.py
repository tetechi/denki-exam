import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\220211024_co_second_q01.pdf"
out_dir = base + r"\r3shimo_images"
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

print("Page 5 idx=4 (Q1,Q4,Q5)...")
crop(4, 0.04, 0.22, 'q01.png')   # 問1 回路図（S1閉S2開）
crop(4, 0.49, 0.73, 'q04.png')   # 問4 R-X直列回路
crop(4, 0.73, 0.99, 'q05.png')   # 問5 三相Y接続回路

print("Page 6 idx=5 (Q6,Q7,Q9)...")
crop(5, 0.01, 0.27, 'q06.png')   # 問6 単相2線式回路
crop(5, 0.27, 0.62, 'q07.png')   # 問7 単相3線式回路
crop(5, 0.74, 0.99, 'q09.png')   # 問9 幹線分岐・40A遮断器

print("Page 7 idx=6 (Q10)...")
crop(6, 0.01, 0.26, 'q10.png')   # 問10 分岐回路（B遮断器4択）

print("Page 8 idx=7 (Q16,Q17,Q18)...")
crop(7, 0.01, 0.34, 'q16.png')   # 問16 写真（材料：TS継手）
crop(7, 0.34, 0.66, 'q17.png')   # 問17 写真（器具：線付防水ソケット）
crop(7, 0.66, 0.99, 'q18.png')   # 問18 写真（測定器：絶縁抵抗計）

print("Page 11 idx=10 (Q37)...")
crop(10, 0.63, 0.75, 'q37.png')  # 問37 照明図記号（CL/CH/環形/ペンダント）

print("Page 12 idx=11 (Q41-Q45 写真)...")
crop(11, 0.01, 0.22, 'q41.png')  # 問41 3路スイッチ裏面配線
crop(11, 0.22, 0.43, 'q42.png')  # 問42 点滅器取付材料
crop(11, 0.43, 0.62, 'q43.png')  # 問43 コンセント器具
crop(11, 0.62, 0.81, 'q44.png')  # 問44 リングスリーブ圧着
crop(11, 0.81, 0.99, 'q45.png')  # 問45 差込形コネクタ

print("Page 13 idx=12 (Q46-Q50 写真)...")
crop(12, 0.01, 0.24, 'q46.png')  # 問46 配線用遮断器
crop(12, 0.24, 0.47, 'q47.png')  # 問47 リングスリーブ種類・個数
crop(12, 0.47, 0.68, 'q48.png')  # 問48 使用されていないスイッチ
crop(12, 0.68, 0.84, 'q49.png')  # 問49 使用されていないもの
crop(12, 0.84, 0.99, 'q50.png')  # 問50 使用されることのないもの

print("Page 15 idx=14 (配線図)...")
crop(14, 0.01, 0.99, 'wiring_diagram.png')

print("Done!")
