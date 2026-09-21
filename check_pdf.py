import os, sys, subprocess
target = r'C:/Users/naina/Downloads/Telegram Desktop/IIMA Consult Prep Book 2024-25.pdf'
print('exists:', os.path.exists(target))
libs = {}
for name in ['fitz','pypdf','PyPDF2','pdfplumber']:
    try:
        __import__(name); libs[name]=True
    except Exception:
        libs[name]=False
print('libs:', libs)
# info about filename chars
print(repr(os.path.basename(target)))
