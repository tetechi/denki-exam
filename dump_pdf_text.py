"""各年度の問題PDFから全文テキストを抽出し JSON に保存する"""
import pypdfium2 as pdfium
import json, os

base = os.path.dirname(os.path.abspath(__file__))

PDFS = {
    'r1kami':       '20190602_co_second_q01.pdf',
    'r1shimo':      '20191006_co_second_q01.pdf',
    'r2shimo':      '20201004_co_second_q01.pdf',
    'r2shimo_gogo': '20201004_co_second_q02.pdf',
    'r3kami':       '20210530_co_second_q01.pdf',
    'r3kami_gogo':  '20210530_co_second_q02.pdf',
    'r3shimo':      '220211024_co_second_q01.pdf',
    'r3shimo_gogo': '220211024_co_second_q02.pdf',
    'r4kami':       '20220529_co_second_q01.pdf',
    'r4kami_gogo':  '20220529_co_second_q02.pdf',
    'r4shimo':      '20221030_co_second_q01.pdf',
    'r4shimo_gogo': '20221030_co_second_q02.pdf',
    'r5kami':       '20230528_co_second_q01.pdf',
    'r5shimo':      '20231029_co_second_q01.pdf',
    'r5shimo_gogo': '20231029_co_second_q02.pdf',
    'r6kami':       '20240526_co_second_q01.pdf',
    'r6shimo':      '20241027_co_second_q01.pdf',
    'r7kami':       '20250525_co_second_q01.pdf',
    'r7shimo':      '20251026_co_second_q01.pdf',
    'r8kami':       '20260524_co_second_q01.pdf',
}

out = {}
for key, fname in PDFS.items():
    path = os.path.join(base, 'list', fname)
    if not os.path.exists(path):
        print(f'{key}: PDFなし')
        continue
    pdf = pdfium.PdfDocument(path)
    parts = []
    for i in range(len(pdf)):
        parts.append(pdf[i].get_textpage().get_text_range())
    out[key] = '\n'.join(parts)
    print(f'{key}: {len(pdf)}ページ / {len(out[key])}文字')

dest = os.path.join(base, 'pdf_text.json')
with open(dest, 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False)
print('\n->', dest)
