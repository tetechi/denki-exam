import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\20251026_co_second_q01.pdf"
out_dir = base + r"\r7shimo_images"
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
crop(4, 0.17, 0.31, 'q01.png')   # 問1 回路図（テーブルヘッダー含む）
crop(4, 0.52, 0.73, 'q04.png')   # 問4 交流回路（L・正弦波）
crop(4, 0.71, 0.97, 'q05.png')   # 問5 三相3線式回路

print("Page 6 idx=5 (Q6,Q7,Q8,Q9)...")
crop(5, 0.03, 0.27, 'q06.png')   # 問6 三相3線式・断線
crop(5, 0.28, 0.52, 'q07.png')   # 問7 単相3線式回路
crop(5, 0.53, 0.73, 'q08.png')   # 問8 合成樹脂管工事（表なし）
crop(5, 0.72, 0.97, 'q09.png')   # 問9 幹線分岐・50A

print("Page 7 idx=6 (Q10, Q16)...")
crop(6, 0.03, 0.24, 'q10.png')   # 問10 分岐回路（B遮断器4択）
crop(6, 0.79, 0.97, 'q16.png')   # 問16 写真（材料）

print("Page 8 idx=7 (Q17, Q18)...")
crop(7, 0.03, 0.27, 'q17.png')   # 問17 写真（器具）
crop(7, 0.27, 0.50, 'q18.png')   # 問18 写真（工具）

print("Page 9 idx=8 (Q23, Q24)...")
crop(8, 0.24, 0.47, 'q23.png')   # 問23 金属管への電線挿入図
crop(8, 0.47, 0.74, 'q24.png')   # 問24 低圧屋内配線検査手順図

print("Page 12 idx=11 (Q41-Q45 写真)...")
crop(11, 0.03, 0.22, 'q41.png')  # 問41 差込コネクタ
crop(11, 0.22, 0.40, 'q42.png')  # 問42 ボックス
crop(11, 0.40, 0.59, 'q43.png')  # 問43 器具
crop(11, 0.58, 0.78, 'q44.png')  # 問44 遮断器
crop(11, 0.78, 0.97, 'q45.png')  # 問45 ケーブル

print("Page 13 idx=12 (Q46-Q50 写真)...")
crop(12, 0.03, 0.30, 'q46.png')  # 問46 リングスリーブ
crop(12, 0.30, 0.50, 'q47.png')  # 問47 リングスリーブ
crop(12, 0.50, 0.65, 'q48.png')  # 問48 スイッチ（使用されていないもの）
crop(12, 0.65, 0.80, 'q49.png')  # 問49 工具（使用されていないもの）
crop(12, 0.80, 0.97, 'q50.png')  # 問50 材料（使用されることのないもの）

print("Page 15 idx=14 (配線図)...")
crop(14, 0.01, 0.99, 'wiring_diagram.png')

print("Done!")
