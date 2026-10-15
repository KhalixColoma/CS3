class Publication:
    def __init__(self,title,author):
        self.title = str(title)
        self.author = str(author)
    def get_title():
        return title
    def get_author():
        return author
    def set_title(self, title):
        self.title = title
    def set_author(self, author):
        self.author = author
    def dipslay_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
class Book(Publication):
    def __init__(self,title,author,number_of_pages):
        super().__init__(title, author)
        self.number_of_pages = int(number_of_pages)
        Book.setnumber_of_pages(self,pages)
    def get_number_of_pages():
     return (f"Number of pages: {self.number_of_pages}")
    def set_number_of_pages():
        if self.number_of_pages>0:
            self.number_of_pages=_number_of_pages
         else:
            print("Number of pages must be positive.")
            self.number_of_pages = abs(self.number_of_pages) 
class Magazine(Publication):
    def __init__(self,title,author,issue_number):
        super().__init__(title, author)
        self.issue_number=int(issue_number)
        Magazine.set_issue_number = issue_number
    def set_issue_number(self,issue_number):
        if issue_number > 0:
            self.issue_number = issue_number
        else:
            print("Issue Number must be positive.")
            self.issue_number = abs(self.issue_number)
    def get_issue_number(self):
        return f"Issue Number: {self.issue_number}"


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
