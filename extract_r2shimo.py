import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\20201004_co_second_q01.pdf"
out_dir = base + r"\r2shimo_images"
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

print("Page 5 idx=4 (Q1, Q4, Q5, Q6)...")
crop(4, 0.08, 0.24, 'q01.png')   # 問1 直流回路（電流）
crop(4, 0.51, 0.66, 'q04.png')   # 問4 交流回路（力率）
crop(4, 0.66, 0.82, 'q05.png')   # 問5 三相誘導電動機（力率式）
crop(4, 0.82, 0.99, 'q06.png')   # 問6 三相3線式（電力損失）

print("Page 6 idx=5 (Q7, Q9, Q10)...")
crop(5, 0.01, 0.30, 'q07.png')   # 問7 単相3線式（電力損失）
crop(5, 0.52, 0.76, 'q09.png')   # 問9 三相電動機・電熱器（幹線電流）
crop(5, 0.76, 0.99, 'q10.png')   # 問10 分岐回路（遮断器・電線・コンセント組合せ）

print("Page 7 idx=6 (Q16)...")
crop(6, 0.75, 0.99, 'q16.png')   # 問16 写真（金属ダクト材料）

print("Page 8 idx=7 (Q17, Q18)...")
crop(7, 0.01, 0.33, 'q17.png')   # 問17 写真（電磁接触器・○で囲まれた部分）
crop(7, 0.33, 0.65, 'q18.png')   # 問18 写真（ホールソー用途）

print("Page 10 idx=9 (Q27)...")
crop(9, 0.22, 0.46, 'q27.png')   # 問27 直動式指示電気計器（記号・測定回路）

print("Page 12 idx=11 (Q41-Q45)...")
crop(11, 0.01, 0.14, 'q41.png')  # 問41 ①部分のケーブル種類
crop(11, 0.14, 0.52, 'q42.png')  # 問42 ②リングスリーブ種類・個数
crop(11, 0.52, 0.72, 'q43.png')  # 問43 ③差込形コネクタ種類・個数
crop(11, 0.72, 0.87, 'q44.png')  # 問44 ④図記号の器具（スイッチ接点）
crop(11, 0.87, 0.99, 'q45.png')  # 問45 ⑤図記号の器具（照明器具）

print("Page 13 idx=12 (Q46-Q50)...")
crop(12, 0.01, 0.22, 'q46.png')  # 問46 ⑥部分に取り付ける機器（遮断器）
crop(12, 0.22, 0.44, 'q47.png')  # 問47 ⑦配線工事で使用しない工具
crop(12, 0.44, 0.67, 'q48.png')  # 問48 ⑧圧着接続（リングスリーブ）
crop(12, 0.67, 0.84, 'q49.png')  # 問49 使用されないコンセント
crop(12, 0.84, 0.99, 'q50.png')  # 問50 施工に使用するものの組合せ（誤り）

print("Page 15 idx=14 (配線図)...")
crop(14, 0.01, 0.99, 'wiring_diagram.png')

print("Done!")
