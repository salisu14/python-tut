#!/usr/bin/env python3

def show_book(book_catalog):
    title = input("Enter the title for the book: ")
    if title in book_catalog:
        book = book_catalog[title]
        print("Title:    " + title)
        print("Author:   " + book["author"])
        print("Pub year: " + book["pubyear"])
    else:
	    print("Sorry,  " + title + " doesn't exist in the catalog.")

# def list_books(book_catalog):
#     if len(book_catalog) > 0:
#         for k, v in book_catalog.items():
#             if isinstance(v, dict):
#                 list_books(v)
#             else:
#                 print(f"{k} : {v}")
#         print()
#     else:
#         print("Books catalog empty!")

def list_books(book_catalog):
    '''Function that takes in a catalog of books and display it'''
    for book in book_catalog:
        print()
        print("Title:   ", book)
        print("Author:  ", book_catalog[book]["author"])
        print("Pub year:", book_catalog[book]["pubyear"])  

def add_edit_book(book_catalog, mode):
    ''' 
      Function to add/edit a given catalogs of books

      @params
      book_catalog - A dictionary of books
      mode - the add/edit flags that indicates whether to add or edit
    '''
	title = input("Enter title of the book: ")
	if mode == "add" and title in book_catalog:
	    print(title + " already exists in the catalog.")
	    response = input("Would you like to edit it? (y/n): ").lower()
	    if(response != "y"):
	        return
	elif mode == "edit" and title not in book_catalog:
	    print(title + " doesn't exist in the catalog.")
	    response = input("Would you like to add it? (y/n): ").lower()
	    if (response != "y"):
	        return
	
	# Get the book data and create a dictionary for the data
	author = input("Enter author name: ")
	pubyear = input("Enter publication year: ")
	book = {"author": author, "pubyear": pubyear}

	# Add the book data to the catalog using title as key
	book_catalog[title] = book
    #print(title + ' has been added/edited')

def delete_book(book_catalog):
    title = input("Title: ")
    if title in book_catalog:
        del book_catalog[title]
        print(title + " removed from catalog.")
    else:
        print(title + " doesn't exist in the catalog.")

def display_menu():
    print("The Book Catalog program")
    print()
    print("COMMAND MENU")
    print("show - Show book info")
    print("list - List books")
    print("add  - Add book")
    print("edit - Edit book")	
    print("del  - Delete book")
    print("exit - Exit program")

def main():
    book_catalog = {
       "Moby Dick":
           {"author" : "Herman Melville",
	        "pubyear" : "1851"},
        "The Hobbit":
	       {"author" : "J. R. R. Tolkien",
	        "pubyear" : "1937"},
        "Slaughterhous Five":

            {"author" : "Kurt Vonnegut",
	         "pubyear" : "1969"}
    }

    display_menu()

    while True:
        print()
        command = input("Command: ").lower()
        if command == "show":
            show_book(book_catalog)
        elif command == "list":
            list_books(book_catalog)
        elif command == "add":
            add_edit_book(book_catalog, mode="add")
        elif command == "edit":
            add_edit_book(book_catalog, mode="edit")
        elif command == "del":
            delete_book(book_catalog)
        elif command == "exit":
            print("Bye!")
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()