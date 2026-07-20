import pypdfium2 as pdfium
import os

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam"
out_dir = base + r"\r7shimo_pages"
os.makedirs(out_dir, exist_ok=True)

# Render answer PDF
a_pdf = pdfium.PdfDocument(base + r"\list\20251026_co_second_a01.pdf")
page = a_pdf[0]
bm = page.render(scale=2)
bm.to_pil().save(out_dir + r"\answer.png")
print("Saved answer.png")

# Render question PDF
q_pdf = pdfium.PdfDocument(base + r"\list\20251026_co_second_q01.pdf")
for i in range(len(q_pdf)):
    page = q_pdf[i]
    bm = page.render(scale=2)
    bm.to_pil().save(f"{out_dir}\\page_{i+1:02d}.png")
    print(f"Saved page_{i+1:02d}.png")

print("Done.")
