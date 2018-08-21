# Note - had to edit populate.py, line 19 - set user_books to list on previous line as wouldn't accept as argument in add_user line
class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("The email address has been updated")

    def __repr__(self):
        num = len(self.books)
        msg = "User {name}, email: {email}, books read: {num}".format(name = self.name, email = self.email, num = num)
        return msg
    
    # caused an issue when creating user in add_user method
    '''def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False
'''
    def read_book(self, book, rating=None):
        self.books[book] = rating
        # Should it only add to ratings if rating isn't None?

    def get_average_rating(self):
        total = 0
        average = 0
        for key, value in self.books.items():
            if value != None:
                total += value
        average = total / len(self.books)
        return average
        

class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, newisbn):
        self.isbn = newisbn
        print("The ISBN for this book has been updated")

    def add_rating(self, rating):
        # Tweaked to accept None as default
        if rating in range(5) or rating == None:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False

    def get_average_rating(self):
        total = 0
        average = 0
        for value in self.ratings:
            # Only tallies numeric ratings (ignores default of None)
            if value != None:
                total += value
        average = total/len(self.ratings)
        return average

    def __hash__(self):
        return hash((self.title, self.isbn))

# Added as didn't print object appropriately in test lines
    def __repr__(self):
        return self.title

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        msg = "{title} by {author}".format(title = self.title, author = self.author)
        return msg


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        msg = "{title}, a {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)
        return msg
    
    
class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}


    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        key = self.users.get(email, "")
        if key == "":
            print ("No user with email {email}!".format(email = email))
        else:
            key.read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1

    def add_user(self, name, email, books=None):
        self.users[email] = User(name, email)
        if books != None:
            for book in books:
                self.add_book_to_user(book, email)
        
                
    def print_catalog(self):
        print("\nPrinting Catalog...")
        books = self.books.keys()
        for book in books:
            print(book)

    def print_users(self):
        print("\nPrinting Users...")
        for user in self.users:
            print(self.users.get(user))

    def most_read_book(self):
        mostbook = ""
        mostread = 0
        for key, value in self.books.items():
            if value > mostread:
                mostread = value
                mostbook = key
        return mostbook
    
    def highest_rated_book(self):
        books = self.books.keys()
        highestrating = 0
        highestbook = ""
        for book in books:
            result = book.get_average_rating()
            if result >highestrating:
                highestrating = result
                highestbook = book
        return highestbook

    def most_positive_user(self):
        users = self.users.keys()
        highestrating = 0
        highestuser = ""
        # need to get the object user and then get average rating
        for user in users:
            result = self.users[user].get_average_rating()
            if result >  highestrating:
                highestrating = result
                highestuser = user
        return highestuser
    
