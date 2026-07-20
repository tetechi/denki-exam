import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\20210530_co_second_q01.pdf"
out_dir = base + r"\r3kami_images"
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
crop(4, 0.01, 0.22, 'q01.png')   # 問1 回路図
crop(4, 0.57, 0.77, 'q04.png')   # 問4 抵抗並列回路
crop(4, 0.77, 0.99, 'q05.png')   # 問5 三相3線式回路

print("Page 6 idx=5 (Q6, Q7, Q9)...")
crop(5, 0.01, 0.35, 'q06.png')   # 問6 単相3線式回路
crop(5, 0.35, 0.64, 'q07.png')   # 問7 三相交流回路
crop(5, 0.80, 0.99, 'q09.png')   # 問9 幹線（電熱器+電動機）

print("Page 7 idx=6 (Q10)...")
crop(6, 0.01, 0.32, 'q10.png')   # 問10 分岐回路組合せ

print("Page 8 idx=7 (Q16, Q17, Q18, Q19)...")
crop(7, 0.01, 0.27, 'q16.png')   # 問16 写真（材料）
crop(7, 0.27, 0.54, 'q17.png')   # 問17 写真（器具）
crop(7, 0.54, 0.78, 'q18.png')   # 問18 写真（工具）
crop(7, 0.78, 0.99, 'q19.png')   # 問19 表（施設場所）

print("Page 9 idx=8 (Q21, Q25)...")
crop(8, 0.01, 0.40, 'q21.png')   # 問21 金属管接続方法（図）
crop(8, 0.78, 0.99, 'q25.png')   # 問25 絶縁抵抗表

print("Page 10 idx=9 (Q26, Q27)...")
crop(9, 0.01, 0.30, 'q26.png')   # 問26 接地極配置（図）
crop(9, 0.30, 0.68, 'q27.png')   # 問27 電圧計・電流計・電力計結線（図）

print("Page 11 idx=10 (Q35)...")
crop(10, 0.61, 0.73, 'q35.png')  # 問35 コンセント極配置（横長ストリップ）

print("Page 12 idx=11 (Q41-Q45)...")
crop(11, 0.01, 0.22, 'q41.png')  # 問41 写真（タイムスイッチ等）
crop(11, 0.22, 0.45, 'q42.png')  # 問42 写真（電線管類）
crop(11, 0.45, 0.68, 'q43.png')  # 問43 写真（照明器具）
crop(11, 0.68, 0.84, 'q44.png')  # 問44 写真（測定器）
crop(11, 0.84, 0.99, 'q45.png')  # 問45 写真（漏電遮断器）

print("Page 13 idx=12 (Q46-Q50)...")
crop(12, 0.01, 0.22, 'q46.png')  # 問46 リングスリーブ刻印
crop(12, 0.22, 0.45, 'q47.png')  # 問47 リングスリーブ個数
crop(12, 0.45, 0.68, 'q48.png')  # 問48 差込形コネクタ
crop(12, 0.68, 0.83, 'q49.png')  # 問49 使用コンセント
crop(12, 0.83, 0.99, 'q50.png')  # 問50 使用スイッチ

print("Page 15 idx=14 (配線図)...")
crop(14, 0.01, 0.99, 'wiring_diagram.png')

print("Done!")
