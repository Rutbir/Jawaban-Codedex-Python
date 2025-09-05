# Dari list buku:
# 1. tambahkan 'Pachinko' 
# 2. hapus 'The Fault in Our Stars' dan '1984' menggunakan remove() dan pop() pada salahh satunya
# 3. print list buku yang sudah diupdate

books = ['Harry Potter',
'1984',
'The Fault in Our Stars',
'The Mom Test',
'Life in Code']

books.append('Pachinko')
books.remove('The Fault in Our Stars')
books.pop(1)
print(books)