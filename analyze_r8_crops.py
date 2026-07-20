"""
r8_images の各 q??.png が page_XX.png のどこにあるか探し出し、
y0/y1 割合を逆算する（numpy不要版）。
"""
import os
from PIL import Image

base = r"C:\Users\user\Documents\Claude\Projects\Electrician Written Exam\r8_images"
pages = sorted([f for f in os.listdir(base) if f.startswith('page_') and f.endswith('.png')])
questions = sorted([f for f in os.listdir(base) if f.startswith('q') and f.endswith('.png')])

PAGE_H = 2064

def row_diff(img_a, img_b, y_a, y_b, width):
    """img_a のy_a行とimg_b のy_b行のピクセル差の平均"""
    total = 0
    pix_a = img_a.load()
    pix_b = img_b.load()
    for x in range(0, width, 8):  # 8px飛ばしで高速化
        ra, ga, ba = pix_a[x, y_a][:3]
        rb, gb, bb = pix_b[x, y_b][:3]
        total += abs(ra-rb) + abs(ga-gb) + abs(ba-bb)
    return total / (width // 8)

for qf in questions:
    qimg = Image.open(os.path.join(base, qf)).convert('RGB')
    qw, qh = qimg.size

    best_page = None
    best_y = 0
    best_score = 9999.0

    for pf in pages:
        pimg = Image.open(os.path.join(base, pf)).convert('RGB')
        pw, ph = pimg.size
        if qh > ph or qw > pw:
            continue
        w = min(qw, pw)

        # 上端行と下端行の両方を使って照合
        for y in range(0, ph - qh + 1, 2):
            s = row_diff(qimg, pimg, 0, y, w)
            if s < best_score:
                best_score = s
                best_page = pf
                best_y = y
            if s < 1.0:
                break
        if best_score < 1.0:
            break

    if best_page:
        y0_px = best_y
        y1_px = y0_px + qh
        print(f"{qf}: {best_page}  y0={y0_px/PAGE_H:.3f} y1={y1_px/PAGE_H:.3f}"
              f"  px={y0_px}-{y1_px}  score={best_score:.1f}  size={qw}x{qh}")

print("Done")
