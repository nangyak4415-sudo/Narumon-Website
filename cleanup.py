import os
os.chdir(r'c:\Users\Asus\Desktop\Website\Tiger Website Gemini')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the string with the mangled pillars-grid div that has the Thai text in attributes
# and replace it with clean version
search_pattern = '<div class="pillars-grid">"ยกระดับระบบบริหารทรัพยากรบุคคลสู่แพลตฟอร์มดิจิทัลเต็มรูปแบบ'
if search_pattern in content:
    # Find the full bad line
    start_idx = content.rfind('<div class="pillars-grid">', 0, content.find(search_pattern) + len(search_pattern))
    end_idx = content.find('\n', start_idx)
    
    if start_idx >= 0 and end_idx > start_idx:
        # Replace the whole bad line
        bad_line = content[start_idx:end_idx]
        replacement_line = '                <div class="pillars-grid">'
        content = content[:start_idx] + replacement_line + content[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Cleanup complete')
