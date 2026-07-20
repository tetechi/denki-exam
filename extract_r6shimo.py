import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\20241027_co_second_q01.pdf"
out_dir = base + r"\r6shimo_images"
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
crop(4, 0.13, 0.30, 'q01.png')   # 問1 回路図（テーブルヘッダー含む）
crop(4, 0.50, 0.77, 'q04.png')   # 問4 正弦波交流回路（C回路）
crop(4, 0.77, 0.99, 'q05.png')   # 問5 三相誘導電動機の力率（数式選択肢）

print("Page 6 idx=5 (Q6,Q7,Q9)...")
crop(5, 0.03, 0.24, 'q06.png')   # 問6 単相2線式回路（99V）
crop(5, 0.24, 0.65, 'q07.png')   # 問7 単相3線式→単相2線式（図1・図2）
crop(5, 0.78, 0.99, 'q09.png')   # 問9 幹線分岐（125A, 10m）

print("Page 7 idx=6 (Q10,Q16)...")
crop(6, 0.03, 0.27, 'q10.png')   # 問10 分岐回路の組合せ（表）
crop(6, 0.77, 0.99, 'q16.png')   # 問16 写真（EEF/Fケーブル）

print("Page 8 idx=7 (Q17,Q18)...")
crop(7, 0.03, 0.22, 'q17.png')   # 問17 写真（漏電遮断器○部分）
crop(7, 0.22, 0.43, 'q18.png')   # 問18 写真（手動油圧式工具）

print("Page 9 idx=8 (Q24)...")
crop(8, 0.43, 0.74, 'q24.png')   # 問24 アナログ式回路計（測定レンジ）

print("Page 10 idx=9 (Q27)...")
crop(9, 0.22, 0.53, 'q27.png')   # 問27 クランプ形漏れ電流計（単相3線式）

print("Page 12 idx=11 (Q41-Q45 写真)...")
crop(11, 0.03, 0.37, 'q41.png')  # 問41 接地抵抗測定器（2×2写真）
crop(11, 0.37, 0.57, 'q42.png')  # 問42 リングスリーブ（種類・個数）
crop(11, 0.57, 0.76, 'q43.png')  # 問43 VVF差込コネクタ
crop(11, 0.76, 0.88, 'q44.png')  # 問44 点滅器取付工事 使用しない材料
crop(11, 0.88, 0.99, 'q45.png')  # 問45 コンセント図記号

print("Page 13 idx=12 (Q46-Q50 写真)...")
crop(12, 0.03, 0.26, 'q46.png')  # 問46 配線工事に必要なケーブル
crop(12, 0.26, 0.48, 'q47.png')  # 問47 トラフ
crop(12, 0.48, 0.65, 'q48.png')  # 問48 図記号の機器
crop(12, 0.65, 0.82, 'q49.png')  # 問49 電線接続作業に使用しないもの
crop(12, 0.82, 0.99, 'q50.png')  # 問50 電線管をモーターに接続する部品

print("Page 15 idx=14 (配線図)...")
crop(14, 0.01, 0.99, 'wiring_diagram.png')

print("Done!")
