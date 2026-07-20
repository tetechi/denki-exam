import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\20201004_co_second_q02.pdf"
out_dir = base + r"\r2shimo_gogo_images"
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
crop(4, 0.08, 0.27, 'q01.png')   # 問1 直流回路（a-b間電圧）
crop(4, 0.55, 0.77, 'q04.png')   # 問4 交流回路（負荷の力率）
crop(4, 0.77, 0.99, 'q05.png')   # 問5 三相3線式（線間電圧E）

print("Page 6 idx=5 (Q6, Q7)...")
crop(5, 0.01, 0.31, 'q06.png')   # 問6 単相2線式（電圧降下）
crop(5, 0.31, 0.62, 'q07.png')   # 問7 単相3線式（電力損失）

print("Page 7 idx=6 (Q10)...")
crop(6, 0.01, 0.38, 'q10.png')   # 問10 分岐回路（遮断器・電線・コンセント組合せ）

print("Page 8 idx=7 (Q16, Q17, Q18)...")
crop(7, 0.01, 0.26, 'q16.png')   # 問16 写真（ユニバーサル等の管接続材料）
crop(7, 0.26, 0.54, 'q17.png')   # 問17 写真（進相コンデンサの用途）
crop(7, 0.54, 0.80, 'q18.png')   # 問18 写真（照度計）

print("Page 9 idx=8 (Q23)...")
crop(8, 0.43, 0.70, 'q23.png')   # 問23 電磁的不平衡防止（電線挿入法）

print("Page 11 idx=10 (Q31)...")
crop(10, 0.17, 0.33, 'q31.png')  # 問31 ①コンセントの極配置（刃受）

print("Page 12 idx=11 (Q41-Q45)...")
crop(11, 0.01, 0.16, 'q41.png')  # 問41 ⑪図記号のもの（ライティングダクト等）
crop(11, 0.16, 0.51, 'q42.png')  # 問42 ⑫接続作業に使用される組合せ（スリーブ+工具）
crop(11, 0.51, 0.69, 'q43.png')  # 問43 ⑬図記号の器具（タイムスイッチ等）
crop(11, 0.69, 0.84, 'q44.png')  # 問44 ⑭図記号の器具（タイマー等）
crop(11, 0.84, 0.99, 'q45.png')  # 問45 ⑮差込形コネクタ種類・個数

print("Page 13 idx=12 (Q46-Q50)...")
crop(12, 0.01, 0.19, 'q46.png')  # 問46 ⑯部分のケーブル種類
crop(12, 0.19, 0.46, 'q47.png')  # 問47 ⑰圧着接続（リングスリーブ）
crop(12, 0.46, 0.65, 'q48.png')  # 問48 ⑱分電盤（金属製）穴あけに使用しないもの
crop(12, 0.65, 0.82, 'q49.png')  # 問49 使用されていないコンセント
crop(12, 0.82, 0.99, 'q50.png')  # 問50 使用されているプルボックスとその個数

print("Page 15 idx=14 (配線図)...")
crop(14, 0.01, 0.99, 'wiring_diagram.png')

print("Done!")
