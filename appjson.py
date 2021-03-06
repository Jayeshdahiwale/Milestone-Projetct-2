from utils import databasejson
USER_CHOICE="""
Enter:
-'a' to add new book
-'l' to list all books
-'r' to make a book as read
-'d' to delete a book 
-'q' to quit
 Your choice:"""
def menu():
    databasejson.create_book_table()
    user_input=input(USER_CHOICE)
    while user_input!='q':
        if user_input=='a':
            prompt_add_book()
        elif user_input=='l':
            list_books()
        elif user_input=='r':
            prompt_read_book()
        elif user_input=='d':
            prompt_delete_book()
        else:
            print('Entered command is invalid .Please insert valid command')
        user_input=input(USER_CHOICE)
def prompt_add_book():
    name=input('enter the name of new book')
    author=input('enter the name of the author of the book')
    databasejson.add_book(name,author)
def list_books():
    books=databasejson.get_all_books()
    for book in books:
        read='YES YOU READ THIS BOOK' if book['read']==True else "YOU HAVEN'T READ THE BOOK YET"
        print(f"{book['name']} by author {book['author']},read:{read}")
def prompt_read_book():
    name=input('enter the name of the book you just finished reading:')
    databasejson.mark_book_as_read(name)
def prompt_delete_book():
    name=input('Enter the name of the book you want to delete:')
    databasejson.delete_book(name)



#def prompt_add_book() ask for book name and author
#def list_books() show all the books in our list
#def prompt_read_book() ask for the book name and change it to 'read' in our list
#def prompt_delete_book() ask for book name and remove book from list


menu()
