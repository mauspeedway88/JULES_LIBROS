import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    current_paragraph = []

    def flush_paragraph():
        if current_paragraph:
            # Join with space, removing existing newlines
            joined = ' '.join(s.strip() for s in current_paragraph if s.strip())
            # Fix cases where a period was alone on a line like "..." \n "."
            joined = joined.replace(' .', '.')
            joined = joined.replace(' ,', ',')
            new_lines.append(joined + '\n')
            current_paragraph.clear()

    for line in lines:
        stripped = line.strip()
        
        # If it's an empty line, or a markdown header, list item, blockquote, or horizontal rule
        if not stripped or re.match(r'^(#|\*|-|>|---)', stripped) or stripped.startswith('**INTENCIÓN:**'):
            flush_paragraph()
            new_lines.append(line)
        else:
            current_paragraph.append(stripped)

    flush_paragraph()

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

process_file('expansion_capitulos.md')
