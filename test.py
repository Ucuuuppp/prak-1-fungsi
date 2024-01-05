# Inisialisasi data akun admin
admin_account = {"username": "admin", "password": "123456"}

# Inisialisasi data akun user
user_account = {"username": "Budi", "password": "123", "borrowed_books": []}
user_account1 = {"username": "Rani", "password": "456", "borrowed_books": []}
user_account2 = {"username": "Hani", "password": "789", "borrowed_books": []}
user_account3 = {"username": "Dani", "password": "999", "borrowed_books": []}

# Simpan data akun user dalam sebuah list
user_accounts = [user_account, user_account1, user_account2, user_account3]

# Inisialisasi data buku dan status peminjaman
books = [
    {"id": 1, "title": "Novel", "author": "Rudi", "is_available": True},
    {"id": 2, "title": "Cerita Pendek", "author": "Ani", "is_available": True},
    {"id": 3, "title": "Ilmu Pengetahuan", "author": "Banu", "is_available": True},
]

# Fungsi pure untuk mencari buku berdasarkan ID
def find_book_by_id(book_id, book_list):
    return next((book for book in book_list if book["id"] == book_id), None)

# Fungsi pure untuk meminjam buku
def borrow_book(user, book_id, book_list):
    book = find_book_by_id(book_id, book_list)
    if book and book["is_available"]:
        return [*book_list[:book_id - 1], {**book, "is_available": False}, *book_list[book_id:]]
    return book_list

# Fungsi pure untuk mengembalikan buku
def return_book(user, book_id, book_list):
    book = find_book_by_id(book_id, user["borrowed_books"])
    if book:
        return [*book_list[:book_id - 1], {**book, "is_available": True}, *book_list[book_id:]]
    return book_list

# Simulasi aplikasi
while True:
    print("\nSelamat datang di Perpustakaan Online")
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    if username == admin_account["username"] and password == admin_account["password"]:
        print("Selamat datang, Admin!")
        while True:
            print("\nMenu Admin:")
            print("1. Tambahkan Buku")
            print("2. Lihat Daftar Buku")
            print("3. Logout")
            choice = input("Pilih menu (1/2/3): ")
            if choice == "1":
                title = input("Masukkan judul buku: ")
                author = input("Masukkan nama penulis: ")
                book_id = len(books) + 1
                books = [*books, {"id": book_id, "title": title, "author": author, "is_available": True}]
                print(f"{title} berhasil ditambahkan ke perpustakaan.")
            elif choice == "2":
                print("Daftar Buku:")
                [print(f"{book['id']}. {book['title']} oleh {book['author']} - {'Tersedia' if book['is_available'] else 'Dipinjam'}") for book in books]
            elif choice == "3":
                print("Admin berhasil logout.")
                break
            else:
                print("Pilihan tidak valid.")

    else:
        user = next((user for user in user_accounts if user["username"] == username and user["password"] == password), None)
        if user:
            print(f"Selamat datang, {user['username']}!")
            while True:
                print("\nMenu User:")
                print("1. Pinjam Buku")
                print("2. Kembalikan Buku")
                print("3. Logout")
                choice = input("Pilih menu (1/2/3): ")
                if choice == "1":
                    print("Daftar Buku:")
                    [print(f"{book['id']}. {book['title']} oleh {book['author']} - {'Tersedia' if book['is_available'] else 'Dipinjam'}") for book in books]
                    book_id = int(input("Masukkan ID buku yang ingin dipinjam: "))
                    books = borrow_book(user, book_id, books)
                elif choice == "2":
                    if not user["borrowed_books"]:
                        print(f"{user['username']} belum meminjam buku apapun.")
                    else:
                        print(f"Daftar Buku yang Dipinjam oleh {user['username']}:")
                        [print(f"{book['id']}. {book['title']} oleh {book['author']}") for book in user["borrowed_books"]]
                        book_id = int(input("Masukkan ID buku yang ingin dikembalikan: "))
                        books = return_book(user, book_id, books)
                elif choice == "3":
                    print(f"{user['username']} berhasil logout.")
                    break
                else:
                    print("Pilihan tidak valid.")
        else:
            print("Username atau password salah. Coba lagi.")