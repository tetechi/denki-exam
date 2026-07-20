import pypdfium2 as pdfium
import pdfplumber
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
q_pdf_path = base + r"\list\20240526_co_second_q01.pdf"
a_pdf_path = base + r"\list\20240526_co_second_a01.pdf"
out_dir = base + r"\r6kami_pages"
os.makedirs(out_dir, exist_ok=True)

# ページ数確認＆プレビュー画像生成
pdf = pdfium.PdfDocument(q_pdf_path)
print(f"問題PDF ページ数: {len(pdf)}")
for i in range(len(pdf)):
    page = pdf[i]
    bm = page.render(scale=1)
    img = bm.to_pil()
    img.save(os.path.join(out_dir, f"page_{i:02d}.png"))
    print(f"  page_{i:02d}.png  size={img.size}")

print()

# 解答PDFのテキスト抽出
print("=== 解答PDF テキスト ===")
with pdfplumber.open(a_pdf_path) as pdf_a:
    print(f"解答PDF ページ数: {len(pdf_a.pages)}")
    for i, page in enumerate(pdf_a.pages):
        text = page.extract_text()
        if text:
            print(f"--- 解答 page {i} ---")
            print(text)

print()

# 問題PDFのテキスト抽出（一般問題ページ）
print("=== 問題PDF テキスト（idx=4〜12）===")
with pdfplumber.open(q_pdf_path) as pdf_q:
    for i in range(4, min(14, len(pdf_q.pages))):
        text = pdf_q.pages[i].extract_text()
        if text:
            print(f"--- 問題 page idx={i} ---")
            print(text[:2000])
            print()
