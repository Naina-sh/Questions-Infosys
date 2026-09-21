import os, sys
from pypdf import PdfReader
target = r'C:/Users/naina/Downloads/Telegram Desktop/IIMA Consult Prep Book 2024-25.pdf'
out = r'C:/Users/naina/OneDrive/Desktop/OA/consult_prep_book.txt'
reader = PdfReader(target)
n = len(reader.pages)
# resume: find already-written page numbers
done = set()
if os.path.exists(out):
    with open(out, 'r', encoding='utf-8') as f:
        for line in f:
            if line.strip().startswith('===== PAGE '):
                try:
                    num = int(line.strip().split('PAGE ')[1].split(' ')[0])
                    done.add(num)
                except Exception:
                    pass
todo = [i for i in range(1, n+1) if i not in done]
print('pages:', n, 'todo:', len(todo))
mode = 'a' if done else 'w'
with open(out, mode, encoding='utf-8') as f:
    for i in todo:
        page = reader.pages[i-1]
        try:
            txt = page.extract_text() or ''
        except Exception as e:
            txt = f'[extract error: {e}]'
        f.write(f'\n\n===== PAGE {i} =====\n\n')
        f.write(txt)
        f.flush()
print('written', out, os.path.getsize(out), 'bytes')