import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\20190602_co_second_q01.pdf"
out_dir = base + r"\r1kami_images"
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
crop(4, 0.08, 0.26, 'q01.png')   # 問1  直流回路（スイッチS閉・a-b端子間電圧）
crop(4, 0.51, 0.68, 'q04.png')   # 問4  交流回路（抵抗8Ω両端電圧）
crop(4, 0.68, 0.86, 'q05.png')   # 問5  三相3線式Δ結線（全消費電力）

print("Page 6 idx=5 (Q6, Q7, Q9)...")
crop(5, 0.01, 0.28, 'q06.png')   # 問6  単相2線式（a-a'間電圧）
crop(5, 0.28, 0.57, 'q07.png')   # 問7  単相3線式（電圧降下Vs-Vr）
crop(5, 0.71, 0.87, 'q09.png')   # 問9  低圧屋内幹線分岐（許容電流最小値）

print("Page 7 idx=6 (Q10, Q16)...")
crop(6, 0.01, 0.23, 'q10.png')   # 問10 分岐回路（遮断器・コンセント組合せ不適切）
crop(6, 0.77, 0.99, 'q16.png')   # 問16 写真（合成樹脂製アウトレットボックス）

print("Page 8 idx=7 (Q17, Q18)...")
crop(7, 0.01, 0.27, 'q17.png')   # 問17 写真（リモコン変圧器）
crop(7, 0.27, 0.57, 'q18.png')   # 問18 写真（ガストーチランプ）

print("Page 9 idx=8 (Q23, Q24, Q27)...")
crop(8, 0.01, 0.28, 'q23.png')   # 問23 金属管工事（末端A・B部分使用物）
crop(8, 0.28, 0.54, 'q24.png')   # 問24 単相3線式（開閉器閉→150V）
crop(8, 0.74, 0.99, 'q27.png')   # 問27 クランプ形漏れ電流計（測定方法）

print("Page 11 idx=10 (Q33)...")
crop(10, 0.32, 0.43, 'q33.png')  # 問33 コンセント極配置（刃受け）

print("Page 12 idx=11 (Q41-Q45)...")
crop(11, 0.01, 0.21, 'q41.png')  # 問41 アウトレットボックス
crop(11, 0.21, 0.41, 'q42.png')  # 問42 接地極付コンセント
crop(11, 0.41, 0.65, 'q43.png')  # 問43 配線用遮断器・漏電遮断器
crop(11, 0.65, 0.84, 'q44.png')  # 問44 リングスリーブ種類・個数
crop(11, 0.84, 0.99, 'q45.png')  # 問45 換気扇

print("Page 13 idx=12 (Q46-Q50)...")
crop(12, 0.01, 0.19, 'q46.png')  # 問46 木造部分穴あけ工具
crop(12, 0.19, 0.51, 'q47.png')  # 問47 差込形コネクタ種類・個数
crop(12, 0.51, 0.67, 'q48.png')  # 問48 ケーブル種類
crop(12, 0.67, 0.84, 'q49.png')  # 問49 スイッチ（接点構成）
crop(12, 0.84, 0.99, 'q50.png')  # 問50 FEP切断工具

print("Page 15 idx=14 (配線図)...")
crop(14, 0.01, 0.99, 'wiring_diagram.png')

print("Done!")
