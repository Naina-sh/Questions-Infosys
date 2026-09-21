import os, sys

def find_pdf(root):
    hits = []
    for dp, dns, fns in os.walk(root):
        for f in fns:
            if f.lower().endswith('.pdf'):
                hits.append(os.path.join(dp, f))
        if len(hits) > 20:
            break
    return hits

roots = [
    r'C:/Users/naina/Downloads',
    r'C:/Users/naina/Desktop',
    r'C:/Users/naina/Documents',
    r'C:/Users/naina/OneDrive',
    r'C:/Users/naina/OneDrive/Desktop',
]

seen = set()
for r in roots:
    if os.path.isdir(r):
        for p in find_pdf(r):
            if p not in seen:
                seen.add(p)
                print(p)
