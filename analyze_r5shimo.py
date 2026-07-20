import pypdfium2 as pdfium
import pdfplumber
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
q_pdf_path = base + r"\list\20231029_co_second_q01.pdf"
a_pdf_path = base + r"\list\20231029_co_second_a01.pdf"
out_dir = base + r"\r5shimo_pages"
os.makedirs(out_dir, exist_ok=True)

pdf = pdfium.PdfDocument(q_pdf_path)
print(f"問題PDF ページ数: {len(pdf)}")
for i in range(len(pdf)):
    page = pdf[i]
    bm = page.render(scale=1)
    img = bm.to_pil()
    img.save(os.path.join(out_dir, f"page_{i:02d}.png"))
    print(f"  page_{i:02d}.png  size={img.size}")

print()
print("=== 解答PDF テキスト ===")
with pdfplumber.open(a_pdf_path) as pdf_a:
    print(f"解答PDF ページ数: {len(pdf_a.pages)}")
    for i, page in enumerate(pdf_a.pages):
        text = page.extract_text()
        if text:
            print(f"--- 解答 page {i} ---")
            print(text)

print()
print("=== 問題PDF テキスト（idx=4〜12）===")
with pdfplumber.open(q_pdf_path) as pdf_q:
    for i in range(4, min(16, len(pdf_q.pages))):
        text = pdf_q.pages[i].extract_text()
        if text:
            print(f"--- 問題 page idx={i} ---")
            print(text[:3000])
            print()
