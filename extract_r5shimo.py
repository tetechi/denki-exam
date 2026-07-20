import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
pdf_path = base + r"\list\20231029_co_second_q01.pdf"
out_dir = base + r"\r5shimo_images"
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

# idx=4: Q1, Q4, Q5
print("idx=4 (Q1,Q4,Q5)...")
crop(4, 0.08, 0.29, 'q01.png')   # Q1 直流回路図（確認済みOK）
crop(4, 0.47, 0.68, 'q04.png')   # Q4 交流回路図
crop(4, 0.67, 0.99, 'q05.png')   # Q5 三相3線式断線回路図

# idx=5: Q6, Q7, Q9
print("idx=5 (Q6,Q7,Q9)...")
crop(5, 0.02, 0.28, 'q06.png')   # Q6 単相2線式回路図（確認済みOK）
crop(5, 0.25, 0.46, 'q07.png')   # Q7 単相3線式回路図
crop(5, 0.58, 0.99, 'q09.png')   # Q9 VVR分岐回路（Q8の末尾から含めて安全マージン）

# idx=6: Q10, Q16
print("idx=6 (Q10,Q16)...")
crop(6, 0.02, 0.36, 'q10.png')   # Q10 分岐回路の組合せ（確認済みOK）
crop(6, 0.79, 0.99, 'q16.png')   # Q16 写真（輪型端子）

# idx=7: Q17, Q18, Q20
print("idx=7 (Q17,Q18,Q20)...")
crop(7, 0.02, 0.27, 'q17.png')   # Q17 写真（水銀灯用安定器）
crop(7, 0.25, 0.60, 'q18.png')   # Q18 写真（ガストーチ）
crop(7, 0.72, 0.99, 'q20.png')   # Q20 施設場所×工事種類の表

# idx=8: Q21
print("idx=8 (Q21)...")
crop(8, 0.02, 0.29, 'q21.png')   # Q21 図記号と施工方法（確認済みOK）

# idx=11: Q41-Q45（逆算した境界）
# q41: Q41のみ（リングスリーブ2×2）
# q42: Q42のみ（VVFケーブル横並び）※q41末尾からQ42テキストが始まる
# q43: Q43のみ（差込コネクタ）※q42末尾に問題文、q43先頭に写真
# q44: Q44のみ（照明器具横並び）
# q45: Q45のみ（遮断器横並び）
print("idx=11 (Q41-Q45)...")
crop(11, 0.02, 0.34, 'q41.png')  # Q41
crop(11, 0.33, 0.42, 'q42.png')  # Q42（薄い帯）
crop(11, 0.40, 0.59, 'q43.png')  # Q43
crop(11, 0.57, 0.77, 'q44.png')  # Q44
crop(11, 0.75, 0.99, 'q45.png')  # Q45

# idx=12: Q46-Q50
print("idx=12 (Q46-Q50)...")
crop(12, 0.02, 0.21, 'q46.png')
crop(12, 0.20, 0.40, 'q47.png')
crop(12, 0.39, 0.59, 'q48.png')
crop(12, 0.57, 0.79, 'q49.png')
crop(12, 0.77, 0.99, 'q50.png')

# idx=14: 配線図
print("idx=14 (配線図)...")
crop(14, 0.01, 0.99, 'wiring_diagram.png')

print("Done!")
