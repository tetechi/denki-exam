import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\20250525_co_second_q01.pdf"
out_dir = base + r"\r7kami_images"
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
crop(4, 0.15, 0.33, 'q01.png')   # 問1 回路図（S1閉・S2開, 4×30Ω）テーブルヘッダー含む
crop(4, 0.53, 0.76, 'q04.png')   # 問4 交流回路（102V, 90V, 48V）
crop(4, 0.73, 0.98, 'q05.png')   # 問5 三相3線式回路

print("Page 6 idx=5 (Q6,Q7,Q9)...")
crop(5, 0.03, 0.41, 'q06.png')   # 問6 単相2線式回路+抵抗表（22mm²まで）
crop(5, 0.41, 0.63, 'q07.png')   # 問7 単相3線式回路（206V）
crop(5, 0.75, 0.98, 'q09.png')   # 問9 幹線分岐（100A, 6m）

print("Page 7 idx=6 (Q10)...")
crop(6, 0.02, 0.28, 'q10.png')   # 問10 分岐回路4択（B遮断器＋コンセント）

print("Page 8 idx=7 (Q16,Q17,Q18)...")
crop(7, 0.04, 0.22, 'q16.png')   # 問16 写真（材料・TSカップリング）
crop(7, 0.22, 0.44, 'q17.png')   # 問17 写真（器具・配線用遮断器）
crop(7, 0.44, 0.61, 'q18.png')   # 問18 写真（工具・トーチランプ）

print("Page 9 idx=8 (Q25)...")
crop(8, 0.62, 0.98, 'q25.png')   # 問25 アナログ式絶縁抵抗計 4図

print("Page 10 idx=9 (Q27)...")
crop(9, 0.22, 0.43, 'q27.png')   # 問27 計器目盛板記号（永久磁石可動コイル形）

print("Page 12 idx=11 (Q41-Q45 写真)...")
crop(11, 0.03, 0.22, 'q41.png')  # 問41 漏電遮断器（MCB）4択
crop(11, 0.22, 0.45, 'q42.png')  # 問42 リングスリーブ圧着
crop(11, 0.45, 0.63, 'q43.png')  # 問43 ポンプ室内器具
crop(11, 0.63, 0.80, 'q44.png')  # 問44 ケーブル
crop(11, 0.80, 0.97, 'q45.png')  # 問45 工具（使用されないもの）

print("Page 13 idx=12 (Q46-Q50 写真)...")
crop(12, 0.03, 0.25, 'q46.png')  # 問46 工事材料
crop(12, 0.25, 0.50, 'q47.png')  # 問47 リングスリーブ
crop(12, 0.50, 0.67, 'q48.png')  # 問48 差込コネクタ
crop(12, 0.67, 0.83, 'q49.png')  # 問49 コンセント
crop(12, 0.83, 0.97, 'q50.png')  # 問50 スイッチ（使用されていないもの）

print("Page 15 idx=14 (配線図)...")
crop(14, 0.01, 0.99, 'wiring_diagram.png')

print("Done!")
