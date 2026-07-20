import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
out_base = base + r"\r4kami_pages"
os.makedirs(out_base, exist_ok=True)

pdfs = [
    ("20220529_co_second_q01.pdf", "q01"),
    ("20220529_co_second_a01.pdf", "a01"),
    ("20220529_co_second_q02.pdf", "q02"),
    ("20220529_co_second_a02.pdf", "a02"),
]

for fname, prefix in pdfs:
    pdf = pdfium.PdfDocument(os.path.join(base, "list", fname))
    out_dir = os.path.join(out_base, prefix)
    os.makedirs(out_dir, exist_ok=True)
    for i in range(len(pdf)):
        page = pdf[i]
        bm = page.render(scale=1.5)
        img = bm.to_pil()
        img.save(os.path.join(out_dir, f"page_{i:02d}.png"))
        print(f"  {prefix}/page_{i:02d}.png")
    print(f"{prefix}: {len(pdf)} pages done")

print("All done!")
