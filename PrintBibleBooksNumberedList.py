from BibleBooksIndex import *
import sys

l1 = books[1:40]
l2 = books[40:67]

for a,b in zip(l1,l2):
    sys.stdout.write('{}. {:<20s} {}. {}\n'.format(str(books.index(a)).zfill(2), a ,str(books.index(b)), b))

for i in range(28,40):
    print('{}. {}'.format(str(i), books[i]))
