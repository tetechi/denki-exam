import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\20191006_co_second_q01.pdf"
out_dir = base + r"\r1shimo_images"
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
crop(4, 0.13, 0.32, 'q01.png')   # 問1  直流回路（a-b端子間合成抵抗）
crop(4, 0.51, 0.75, 'q04.png')   # 問4  正弦波交流回路（電流iの波形）
crop(4, 0.75, 0.99, 'q05.png')   # 問5  三相3線式（線電流I）

print("Page 6 idx=5 (Q6, Q7, Q9)...")
crop(5, 0.01, 0.33, 'q06.png')   # 問6  単相3線式断線（a-b間電圧）
crop(5, 0.33, 0.61, 'q07.png')   # 問7  三相3線式（電圧降下Vs-Vr）
crop(5, 0.72, 0.99, 'q09.png')   # 問9  低圧屋内幹線分岐（許容電流最小値）

print("Page 7 idx=6 (Q10, Q16)...")
crop(6, 0.01, 0.28, 'q10.png')   # 問10 分岐回路（電線・コンセント組合せ適切）
crop(6, 0.77, 0.99, 'q16.png')   # 問16 写真（銅線用裸圧着端子）

print("Page 8 idx=7 (Q17, Q18)...")
crop(7, 0.01, 0.33, 'q17.png')   # 問17 写真（タイムスイッチ）
crop(7, 0.33, 0.60, 'q18.png')   # 問18 写真（CVケーブルストリッパ）

print("Page 9 idx=8 (Q23)...")
crop(8, 0.28, 0.57, 'q23.png')   # 問23 金属管挿入方法（電磁的不平衡を生じない）

print("Page 10 idx=9 (Q27)...")
crop(9, 0.28, 0.57, 'q27.png')   # 問27 交流回路計器（a電流計,b電圧計,c電力計）

print("Page 11 idx=10 (Q35, Q37)...")
crop(10, 0.53, 0.63, 'q35.png')  # 問35 ペンダント図記号
crop(10, 0.73, 0.85, 'q37.png')  # 問37 コンセント極配置（刃受け）

print("Page 12 idx=11 (Q41-Q45)...")
crop(11, 0.01, 0.22, 'q41.png')  # 問41 リングスリーブ種類・個数
crop(11, 0.22, 0.43, 'q42.png')  # 問42 ケーブル種類
crop(11, 0.43, 0.62, 'q43.png')  # 問43 照明器具（埋込形・ペンダント等）
crop(11, 0.62, 0.81, 'q44.png')  # 問44 主幹取付機器（電磁接触器等）
crop(11, 0.81, 0.99, 'q45.png')  # 問45 負荷電流測定器具

print("Page 13 idx=12 (Q46-Q50)...")
crop(12, 0.01, 0.21, 'q46.png')  # 問46 点滅器（ホタルスイッチ等）
crop(12, 0.21, 0.44, 'q47.png')  # 問47 リングスリーブ小3個・圧着刻印
crop(12, 0.44, 0.62, 'q48.png')  # 問48 アウトレットボックス
crop(12, 0.62, 0.81, 'q49.png')  # 問49 差込形コネクタ種類・個数
crop(12, 0.81, 0.99, 'q50.png')  # 問50 配線図で使用されないスイッチ

print("Page 15 idx=14 (配線図)...")
crop(14, 0.01, 0.99, 'wiring_diagram.png')

print("Done!")
