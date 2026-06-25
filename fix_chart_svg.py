import sys

filepath = '/Users/mia/Desktop/0522南亞ESG 2026/static2025/tw/commitment_to_sdgs.html'
with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

start_idx = 1574
end_idx = 1885

if '<svg width="942"' in lines[start_idx] and '</svg>' in lines[end_idx]:
    new_lines = lines[:start_idx] + ['            <img src="../img/svg/chart__commitment-to-sdgs__env-impact__single-column-v.svg" alt="南亞科技產品規劃與規格演進">\n'] + lines[end_idx+1:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Replaced successfully")
else:
    print("Mismatch")
    print("start_idx:", lines[start_idx].strip())
    print("end_idx:", lines[end_idx].strip())
