import re
    
def convert(markdownText):
    # Headers
    markdownText = re.sub(r'^# (.+)$', r'<h1>\1</h1>', markdownText, flags=re.M)
    markdownText = re.sub(r'^## (.+)$', r'<h2>\1</h2>', markdownText, flags=re.M)
    markdownText = re.sub(r'^### (.+)$', r'<h3>\1</h3>', markdownText, flags=re.M)

    # Bold
    markdownText = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', markdownText)

    # Italic
    markdownText = re.sub(r'\*(.+?)\*', r'<i>\1</i>', markdownText)

    # Numbered List
    markdownText = re.sub(r'(?<=\n)(\d+\.) (.+?)(?=\n\n|\n\s*\d+\.)', r'<li>\2</li>', markdownText, flags=re.S)
    markdownText = re.sub(r'(\n<li>.+?</li>)+', r'\n<ol>\g<0>\n</ol>', markdownText)

    # Image
    markdownText = re.sub(r'!\[([^\]]+)\]\(([^)]+)\)', r'<img src="\2" alt="\1"/>', markdownText)

    # Link
    markdownText = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', markdownText)

    return markdownText