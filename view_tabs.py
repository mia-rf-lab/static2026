with open('en/cleaner_production.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = '<ul class="split-tabs__content"'
end_marker = '</ul>\n        </div>\n\n        <div class="split-tabs js-switch-by-hover aos">'

start_idx = content.find(start_marker)
# end_idx = content.find(end_marker, start_idx) # wait, I don't know the exact end marker.
print(content[start_idx:start_idx+6000])
