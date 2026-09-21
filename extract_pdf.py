from pypdf import PdfReader

r = PdfReader(r'C:\Users\naina\Downloads\Telegram Desktop\Diversity hiring __ 8th September 2026 (Tuesday).pdf')
import sys
sys.stdout.reconfigure(encoding='utf-8')
print('\n---PAGE---\n'.join(p.extract_text() for p in r.pages))