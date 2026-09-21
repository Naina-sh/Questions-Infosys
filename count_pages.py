import os
out = r'C:/Users/naina/OneDrive/Desktop/OA/consult_prep_book.txt'
cnt = 0
with open(out, 'r', encoding='utf-8', errors='replace') as f:
    for line in f:
        if line.strip().startswith('===== PAGE '):
            cnt += 1
print('pages extracted:', cnt)