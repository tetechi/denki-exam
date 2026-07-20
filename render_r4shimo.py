import pypdfium2 as pdfium
import os

for suffix, tag in [('q01', 'r4shimo_pages'), ('a01', 'r4shimo_answers'), ('q02', 'r4shimo_gogo_pages'), ('a02', 'r4shimo_gogo_answers')]:
    pdf = pdfium.PdfDocument(rf"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam\list\20221030_co_second_{suffix}.pdf")
    out_dir = rf"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam\{tag}"
    os.makedirs(out_dir, exist_ok=True)
    for i in range(len(pdf)):
        page = pdf[i]
        bm = page.render(scale=2)
        img = bm.to_pil()
        img.save(os.path.join(out_dir, f"page_{i+1:02d}.png"))
        print(f"{tag}/page_{i+1:02d}.png")

print("Done!")
