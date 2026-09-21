import os
p1 = r'C:/Users/naina/Downloads/Telegram Desktop/IIMA Consult Prep Book 2024-25.pdf'
p2 = r'C:/Users/naina/OneDrive/Desktop/OA/consult_prep_book.txt'
print('pdf bytes:', os.path.getsize(p1))
print('txt bytes:', os.path.getsize(p2) if os.path.exists(p2) else 'missing')