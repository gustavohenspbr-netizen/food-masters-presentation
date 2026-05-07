import re

files_to_update = [
    'v3/index.html',
    'v3/slides.html',
    'v4/index.html'
]

with open('/tmp/logos.html', 'r') as f:
    new_logos = f.read().strip()

# We want to replace the block starting with logo1.png and ending with logo15.jpg
pattern = re.compile(
    r'(<img src="\.\./assets/logos/logo1\.png".*?)(?:\n\s*<img src="\.\./assets/logos/.*?)*\n\s*<img src="\.\./assets/logos/logo15\.jpg"[^>]*>',
    re.DOTALL
)

for filename in files_to_update:
    with open(filename, 'r') as f:
        content = f.read()
    
    # Let's indent the new_logos to match the indentation of the first line
    def replacer(match):
        # Find the indentation of the matched string
        first_line = match.group(0).split('\n')[0]
        indentation = ' ' * (len(first_line) - len(first_line.lstrip()))
        
        # Indent each line of new_logos
        indented_new_logos = '\n'.join([indentation + line if i > 0 else line for i, line in enumerate(new_logos.split('\n'))])
        return indented_new_logos
        
    new_content = pattern.sub(replacer, content)
    
    with open(filename, 'w') as f:
        f.write(new_content)
    
    print(f"Updated {filename}")
