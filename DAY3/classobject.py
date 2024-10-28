# class Book:
#   def __init__(self, title, author, publication_year, isbn):
#     self.title = title
#     self.author = author
#     self.publication_year = publication_year
#     self.isbn = isbn

# class Member:
#   def __init__(self, name):
#     self.name = name
#     self.renting_list = []

# class Rental:
#   def __init__(self,book,member,rental_date,return_date=None):
#     self.book = book
#     self.member = member
#     self.rental_date = rental_date
#     self.return_date = return_date

# class LibraryManagement:

#   def __init__(self):
#     self.book_list = []
#     self.member_list = []
#     self.rented_list = []
  
#   def add_book(self, title, author, publication_year, isbn):
#     new_book = Book(title,author,publication_year,isbn)
#     self.book_list.append(new_book)
#     print(f"{title} 도서가 추가 되었습니다!")
    
#   def add_member(self,name):
#     new_member = Member(name)
#     self.member_list.append(new_member)
#     print(f"{name}님, \n 회원으로 등록 되었습니다!")

#   def rent_book(self,isbn,member_name):
#     book = None
#     member = None
#     for b in self.book_list:
#       if b.isbn == isbn:
#         book = b
#         break
#     for m in self.member_list:
#       if m.name == member_name:
#         member = m
#         break
#     if book and member:
#       new_rental = Rental(book,member,"오늘")
#       self.rented_list.append(new_rental)
#       member.renting_list.append(book)
#       print("도서를 대여하였습니다.")
#     else:
#       print("도서 혹은 회원 정보가 일치하지 않습니다.")

#     def return_book(self,isbn,member_name):
#         book = None
#         member = None
#         for b in self.book_list:
#             book = b
#             break
#         for m in self.member_list:
#             member = m
#             break
#         if book and member:
#             if book in member.renting_list:
#                 member.renting_list.remove(book)
#         return_book = Rental(book,member,"오늘")
#         return_book.return_date = "오늘"
#         self.rented_list.remove(return_book)
#         print("반납이 완료되었습니다.")
#       else:
#             print("도서 혹은 회원 정보가 일치하지 않습니다.")

#     def print_books(self):
#         if not self.book_list:
#             print("도서가 없습니다!")
#         else:
#             for book in self.book_list:
#                 print(f"{book.title} - {book.author}지음,{book.publication_year},{book.isbn}")

#     def print_members(self):
#         for member in self.member_list:
#             if not self.member_list:
#                 print("회원으로 등록되지 않았습니다!")
#         else:
#             print(f"{member.name}회원 대여 중인 도서는 {member.renting_list if member.renting_list else '없음'}")

# library = LibraryManagement()
# library.add_book("1984", "조지 오웰", 1949, "978-0451524935")
# library.add_book("앵무새 죽이기", "하퍼 리", 1960, "978-0446310789")
# library.add_member("홍길동")

# print("\n")
# library.rent_book("978-0451524935", "홍길동")
# print("\n")
# library.print_books()
# print("\n")
# library.print_members()
# print("\n")
# library.return_book("978-0451524935", "홍길동")
# print("\n")
# library.print_members()
# print("\n")

class Book:
    def __init__(self, title, author, publication_year, isbn):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.isbn = isbn

class Member:
    def __init__(self, name):
        self.name = name
        self.renting_list = []

class Rental:
    def __init__(self, book, member, rental_date, return_date=None):
        self.book = book
        self.member = member
        self.rental_date = rental_date
        self.return_date = return_date

class LibraryManagement:
    def __init__(self):
        self.book_list = []
        self.member_list = []
        self.rented_list = []

    def add_book(self, title, author, publication_year, isbn):
        new_book = Book(title, author, publication_year, isbn)
        self.book_list.append(new_book)
        print(f"{title} 도서가 추가되었습니다!")

    def add_member(self, name):
        new_member = Member(name)
        self.member_list.append(new_member)
        print(f"{name}님이 회원으로 등록되었습니다!")

    def rent_book(self, isbn, member_name):
        book = None
        member = None
        for b in self.book_list:
            if b.isbn == isbn:
                book = b
                break
        for m in self.member_list:
            if m.name == member_name:
                member = m
                break
        if book and member:
            new_rental = Rental(book, member, "오늘")
            self.rented_list.append(new_rental)
            member.renting_list.append(book)
            print("도서를 대여하였습니다.")
        else:
            print("도서 혹은 회원 정보가 일치하지 않습니다.")

    def return_book(self, isbn, member_name):
        book = None
        member = None
        for b in self.book_list:
            if b.isbn == isbn:
                book = b
                break
        for m in self.member_list:
            if m.name == member_name:
                member = m
                break
        if book and member:
            if book in member.renting_list:
                member.renting_list.remove(book)
                for rental in self.rented_list:
                    if rental.book == book and rental.member == member:
                        rental.return_date = "오늘"
                        print("반납이 완료되었습니다.")
                        break
            else:
                print("이 회원이 이 도서를 대여하지 않았습니다.")
        else:
            print("도서 혹은 회원 정보가 일치하지 않습니다.")

    def print_books(self):
        if not self.book_list:
            print("도서가 없습니다!")
        else:
            for book in self.book_list:
                print(f"{book.title} - {book.author} 지음, {book.publication_year}, {book.isbn}")

    def print_members(self):
        if not self.member_list:
            print("회원으로 등록되지 않았습니다!")
        else:
            for member in self.member_list:
                print(f"{member.name} 회원, 대여 중인 도서: {[book.title for book in member.renting_list] if member.renting_list else '없음'}")

# 사용 예시
library = LibraryManagement()
library.add_book("1984", "조지 오웰", 1949, "978-0451524935")
library.add_book("앵무새 죽이기", "하퍼 리", 1960, "978-0446310789")
library.add_member("홍길동")
print("\n")
library.rent_book("978-0451524935", "홍길동")
print("\n")
library.print_books()
print("\n")
library.print_members()
print("\n")
library.return_book("978-0451524935", "홍길동")
print("\n")
library.print_members()
print("\n")
