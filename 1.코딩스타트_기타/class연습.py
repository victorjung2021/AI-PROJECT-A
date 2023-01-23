#매직 매소드
class Book(object):
    count=0
    def __init__(self, auther, title, publisher, date):
        self.auther = auther
        self.title = title
        self.publisher = publisher
        self.date = date
        Book.count += 1
    
    def print_info(self):
        print("auther:", self.auther)
        print("title:", self.title)
        print("publisher:", self.publisher)
        print("date:", self.date)
book = Book("victor", "python program", "clab", "2024")
book.print_info()
print("Number of Books:", str(Book.count))



#class Book(object):
#    auther=""
#    title=""
#    publisher=""
#    date=""

#book = Book()
#book.auther="victor"
#print(book.auther)

#class Book(object):
#    auther=""
#    title=""
#    publisher=""
#    date=""
#    count = 0    
#method
#    def print_info(self):
#        print("auther:", self.auther)
#        print("title:", self.title)
#        print("publisher:", self.publisher)
#        print("date:", self.date)

#b1 = Book()
#Book.count += 1
#b1.auther = "victor"
#b1.title = "Python Programming"
#b1.publisher = "cobook"
#b1.date = "2021"
#b1.print_info()
#print("Number of Books:", str(Book.count))


#class속성과 instance속성 차이
#Book.auther = "victor"
#Book.title = "Python Programming"
#Book.publisher = "rebook"
#Book.date = "2021"
#b1.print_info()







#class BookReader():
#    def __init__(self, name):
#        self.name = name
#    
#    def read_book(self):
#        print(self.name,'님은 책을 읽는다')

#reader = BookReader('정형준')
#reader.read_book()
