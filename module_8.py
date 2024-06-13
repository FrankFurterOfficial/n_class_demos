#make a basic class- Assign default values in constructor
class book():
    #Constructor to set information via parameters
    def __init__(self,input_title='',input_genre='',input_author='',input_pages=0):
        self.title = input_title
        self.author = input_author
        self.genre = input_genre
        self.pages = input_pages
    #override str function to print an object
    def __str__(self):
        return f'Title: \t{self.title}\nAuthor:\t{self.author}\nGenre: \t{self.genre}\nPages: \t{self.pages}'
    #Function to update the title of a book
    def change_title(self, new_title):
        self.title = new_title
    #Ovveride of gt function to see which book has more pages
    def __gt__(self, other):
        if self.pages > other.pages:
            return True
        else:
            return False

my_book = book()
my_book.title = 'Freddy Fazbear'
my_book.author = 'Tracy Deonn'
my_book.genre = 'Fartasy'
my_book.pages = 79125
# print(my_book.title)
my_other_book = book('Hellen Keller hate mail, part 1','Nonfiction','Martin Luther King',9581275)
# print(my_other_book.title)
# print(my_other_book)
library = [my_book,my_other_book]

for book in library:
    print(book)

my_book.change_title('Green Freggs and hamddy Fazbear')

for book in library:
    print(book)

print(my_book > my_other_book)