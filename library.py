import mysql.connector

# Function to create a connection to the MySQL database
def create_connection():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mydatabase@99#",
        database="library"
    )
    return mydb

# Function to create the books table
def create_books_table(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            author VARCHAR(255),
            ISBN VARCHAR(255)
        )
    """)
    mycursor.close()

# Function to add a book to the books table
def add_book(mydb, title, author, ISBN):
    mycursor = mydb.cursor()
    sql = "INSERT INTO books (title, author, ISBN) VALUES (%s, %s, %s)"
    val = (title, author, ISBN)
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"Book '{title}' added successfully.")
    mycursor.close()

# Function to search for books by title
def search_books_by_title(mydb, title):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM books WHERE title LIKE %s"
    val = (f"%{title}%",)
    mycursor.execute(sql, val)
    results = mycursor.fetchall()
    if results:
        for book in results:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}")
    else:
        print(f"No books found with title containing '{title}'.")
    mycursor.close()

# Function to list all books
def list_all_books(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM books")
    results = mycursor.fetchall()
    if results:
        for book in results:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, ISBN: {book[3]}")
    else:
        print("No books found.")
    mycursor.close()

# Function to delete a book by ID
def delete_book_by_id(mydb, book_id):
    mycursor = mydb.cursor()
    sql = "DELETE FROM books WHERE id = %s"
    val = (book_id,)
    mycursor.execute(sql, val)
    mydb.commit()
    if mycursor.rowcount > 0:
        print(f"Book with ID {book_id} deleted successfully.")
    else:
        print(f"No book found with ID {book_id}.")
    mycursor.close()

# Main function
def main():
    mydb = create_connection()
    create_books_table(mydb)

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Search books by title")
        print("3. List all books")
        print("4. Delete a book by ID")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            ISBN = input("Enter the book ISBN: ")
            add_book(mydb, title, author, ISBN)
        elif choice == '2':
            title = input("Enter the title to search: ")
            search_books_by_title(mydb, title)
        elif choice == '3':
            list_all_books(mydb)
        elif choice == '4':
            book_id = int(input("Enter the book ID to delete: "))
            delete_book_by_id(mydb, book_id)
        elif choice == '5':
            print("Exiting the library management system.")
            break
        else:
            print("Invalid choice. Please try again.")

    mydb.close()

if __name__ == "__main__":
    main()
