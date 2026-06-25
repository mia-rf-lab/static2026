with open('/Users/mia/Desktop/0522南亞ESG 2026/static2025/img/svg/diagram__commitment-to-sdgs__diagram.svg', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines[:100]):
    if 'y="56"' in line or 'y="139"' in line or 'y="222"' in line:
        print(f"--- Line {i+1} ---")
        start = max(0, i-5)
        end = min(len(lines), i+20)
        for j in range(start, end):
            print(f"{j+1}: {lines[j].strip()}")
