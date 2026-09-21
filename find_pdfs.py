import os
roots = [r'C:/Users/naina/Downloads', r'C:/Users/naina/Desktop', r'C:/Users/naina/Documents', r'C:/Users/naina/OneDrive']
seen=set()
for r in roots:
    if os.path.isdir(r):
        for dp,dns,fns in os.walk(r):
            for f in fns:
                if f.lower().endswith('.pdf'):
                    p=os.path.join(dp,f)
                    if p not in seen:
                        seen.add(p); print(p)