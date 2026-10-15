class Publication:
    def __init__(self,title,author):
        self.title = str(title)
        self.author = str(author)
    def get_title():
        print(title)
    def get_author():
        print(author)
    def set_title():
        set_title=str(input("Set the ttitle for your book")
class Book:
    def __init__(self,title,author,number_of_pages_):
        self.number_of_pages=int(number_of_pages)
        self.title = str(title)
        self.author = str(author)
    def get_number_of_pages():
    def set_number_of_pages():
class Magazine:
    def __init__(self,title,author,issue_number):
        self.issue_number=int(Issue_number)
        self.title = str(title)
        self.author = str(author)

pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen,H.")
book1 = Book("The Hobbit, J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(-310)
book1.display_info()
print(book1.get_issue_number())

print("\nMagazine Information:")
mag1.display_info()
print(mag1.get_issue_number())
