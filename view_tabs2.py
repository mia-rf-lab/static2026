with open('en/cleaner_production.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<ul class="split-tabs__content"'
start_idx = content.find(start_marker)

print(content[start_idx+6000:start_idx+12000])
