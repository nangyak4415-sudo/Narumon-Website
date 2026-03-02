#!/usr/bin/env python3
import os

os.chdir(r'c:\Users\Asus\Desktop\Website\Tiger Website Gemini')

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and replace the mangled line
# Look for the pattern where pillars-grid has mangled Thai data attributes
# We need to remove that mangled content and keep only the clean opening

# Find the position of the mangled line
idx = content.find('<div class="pillars-grid">')
if idx > 0:
    # Find the end of that line  
    newline_pos = content.find('\n', idx)
    next_line_start = newline_pos + 1
    next_line_end = content.find('\n', next_line_start)
    
    # Check if next line starts with mangled data (contains Thai characters after pillars-grid closing)
    if next_line_end > 0:
        next_line = content[next_line_start:next_line_end]
        # If the line has Thai text with mangled quotes, it's the bad line
        if 'ยกระดับระบบ' in next_line or 'Elevating HR' in next_line:
            # Delete this line
            content = content[:newline_pos] + content[next_line_end:]

# Write back
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Cleaned successfully')
