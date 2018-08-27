#Answer to Day 13: Abstract Classes

class MyBook(Book):
    def __init__(self,title, author, price):
        Book.__init__(self,title,author)
        self.price=price
    def display(self):
        print("Title: "+self.title+"\nAuthor: "+self.author+"\nPrice: "+str(self.price))