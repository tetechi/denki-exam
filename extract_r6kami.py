import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\20240526_co_second_q01.pdf"
out_dir = base + r"\r6kami_images"
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

print("Page 5 idx=4 (Q1,Q2,Q4,Q5)...")
crop(4, 0.09, 0.30, 'q01.png')   # 問1 回路図（8Ω，テーブルヘッダー含む）
crop(4, 0.30, 0.46, 'q02.png')   # 問2 導線の抵抗率（数式選択肢）
crop(4, 0.47, 0.64, 'q04.png')   # 問4 三相誘導電動機の力率（数式選択肢）
crop(4, 0.64, 0.88, 'q05.png')   # 問5 三相3線式回路

print("Page 6 idx=5 (Q6,Q7,Q9)...")
crop(5, 0.03, 0.37, 'q06.png')   # 問6 単相2線式回路（電圧降下）
crop(5, 0.37, 0.65, 'q07.png')   # 問7 単相3線式（電力損失）
crop(5, 0.78, 0.99, 'q09.png')   # 問9 電動機幹線回路

print("Page 7 idx=6 (Q10,Q13,Q16)...")
crop(6, 0.03, 0.28, 'q10.png')   # 問10 分岐回路の組合せ（表）
# 問13 は文章のみ（工具名テキスト選択肢）→ 画像不要
crop(6, 0.70, 0.92, 'q16.png')   # 問16 写真（金属ダクト）

print("Page 8 idx=7 (Q17,Q18,Q19)...")
crop(7, 0.03, 0.36, 'q17.png')   # 問17 写真（器具名称）
crop(7, 0.36, 0.60, 'q18.png')   # 問18 写真（工具用途）
crop(7, 0.60, 0.80, 'q19.png')   # 問19 リングスリーブ（表）

print("Page 10 idx=9 (Q27)...")
crop(9, 0.20, 0.50, 'q27.png')   # 問27 指示電気計器の目盛板（図）

print("Page 11 idx=10 (Q33,Q37)...")
crop(10, 0.30, 0.44, 'q33.png')  # 問33 コンセントの極配置（刃受）
crop(10, 0.60, 0.78, 'q37.png')  # 問37 器具の図記号

print("Page 12 idx=11 (Q41-Q45 写真)...")
crop(11, 0.03, 0.25, 'q41.png')  # 問41 差込コネクタ種類と個数
crop(11, 0.25, 0.48, 'q42.png')  # 問42 電線管相互を接続する部品
crop(11, 0.48, 0.67, 'q43.png')  # 問43 配線工事で使用されない工具
crop(11, 0.67, 0.82, 'q44.png')  # 問44 幹線の電流計測
crop(11, 0.82, 0.99, 'q45.png')  # 問45 点滅器の図記号

print("Page 13 idx=12 (Q46-Q50 写真)...")
crop(12, 0.03, 0.25, 'q46.png')  # 問46 接地線直線重ね接続の工具とスリーブ
crop(12, 0.25, 0.50, 'q47.png')  # 問47 器具の名称（図記号）
crop(12, 0.50, 0.68, 'q48.png')  # 問48 ボックス内リングスリーブ接続
crop(12, 0.68, 0.79, 'q49.png')  # 問49 ボックス内差込コネクタ
crop(12, 0.78, 0.99, 'q50.png')  # 問50 使用されないコンセント

print("Page 15 idx=14 (配線図)...")
crop(14, 0.01, 0.99, 'wiring_diagram.png')

print("Done!")
